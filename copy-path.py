"""Nautilus extension: adds "Copy Path" to the right-click menu of files and folders."""

import gi

gi.require_version("Gdk", "4.0")
from gi.repository import Gdk, GObject, Nautilus


def _path_of(file_info):
    location = file_info.get_location()
    return location.get_path() or location.get_uri()


def _copy(text):
    Gdk.Display.get_default().get_clipboard().set(text)


class CopyPathExtension(GObject.GObject, Nautilus.MenuProvider):
    def get_file_items(self, files):
        if not files:
            return []
        label = "Copy Path" if len(files) == 1 else f"Copy {len(files)} Paths"
        item = Nautilus.MenuItem(name="CopyPath::files", label=label)
        item.connect("activate", lambda _item: _copy("\n".join(_path_of(f) for f in files)))
        return [item]

    def get_background_items(self, current_folder):
        item = Nautilus.MenuItem(name="CopyPath::folder", label="Copy Current Folder Path")
        item.connect("activate", lambda _item: _copy(_path_of(current_folder)))
        return [item]
