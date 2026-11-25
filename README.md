# Nautilus "Copy Path" context-menu extension

Adds a **Copy Path** entry to the right-click menu of GNOME Files (Nautilus).

| Right-click on | Menu entry | Copied to clipboard |
|---|---|---|
| A file or folder | **Copy Path** | `/home/me/Documents/report.pdf` |
| Several selected items | **Copy N Paths** | one path per line |
| Empty space in a folder | **Copy Current Folder Path** | the current folder's path |

Paths are copied raw (no quotes). Remote locations (SFTP, SMB, …) copy their URI instead.
Works on both X11 and Wayland.

## Requirements

- GNOME Files / Nautilus **43 or newer** (Ubuntu 23.04+, Fedora 37+, …) — check with `nautilus --version`
- The Nautilus Python bindings:

```bash
# Ubuntu / Debian
sudo apt install python3-nautilus

# Fedora
sudo dnf install nautilus-python

# Arch
sudo pacman -S python-nautilus
```

## Install

```bash
mkdir -p ~/.local/share/nautilus-python/extensions
curl -fsSL https://gist.githubusercontent.com/taghouttarek/accd92fc3d7ad2fc0bb3031131897ea7/raw/copy-path.py -o ~/.local/share/nautilus-python/extensions/copy-path.py
nautilus -q   # restart Files (closes open Files windows) so it picks up the extension
```

Then reopen Files and right-click any file, folder, or empty space.

## Uninstall

```bash
rm ~/.local/share/nautilus-python/extensions/copy-path.py
nautilus -q
```

## Troubleshooting

- **Entry doesn't appear:** Files only loads extensions at startup. Make sure no old instance is left running
  (`pgrep -a nautilus`); run `nautilus -q` and reopen it.
- **Still missing:** check that the Python loader is installed —
  `ls /usr/lib/*/nautilus/extensions-4/libnautilus-python.so` (path may vary by distro).

---

First published as a [gist](https://gist.github.com/taghouttarek/accd92fc3d7ad2fc0bb3031131897ea7).
