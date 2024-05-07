from pathlib import Path

serve = {
    "__trame_bbox": str(Path(__file__).with_name("serve").resolve()),
}
scripts = [
    "__trame_bbox/trame-bbox.umd.js",
]
vue_use = [
    "trame_bbox",
]
