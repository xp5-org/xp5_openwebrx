import shutil
from pathlib import Path

src_root = Path("/src")

file_map = {
    "htdocs/lib/MapManager.js": "/usr/lib/python3/dist-packages/htdocs/lib/MapManager.js",
    "htdocs/map-leaflet.js": "/usr/lib/python3/dist-packages/htdocs/map-leaflet.js",
    "owrx/config/defaults.py": "/usr/lib/python3/dist-packages/owrx/config/defaults.py",
    "owrx/connection.py": "/usr/lib/python3/dist-packages/owrx/connection.py",
    "owrx/controllers/settings/general.py": "/usr/lib/python3/dist-packages/owrx/controllers/settings/general.py",
}

for rel_path, target_path in file_map.items():
    src_file = src_root / rel_path
    tgt_file = Path(target_path)
    if src_file.exists():
        tgt_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, tgt_file)
        print(f"updated {tgt_file}")
    else:
        print(f"source file missing: {src_file}")