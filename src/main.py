import webview as wv
import json
import sys
import pathlib
import argparse

def get_resource_path(relative_path):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return pathlib.Path(sys._MEIPASS) / relative_path
    return pathlib.Path(__file__).parent / relative_path

def window():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Run in development mode")
    args = parser.parse_args()

    if args.dev:
        pkg_path = get_resource_path("package.json")
        url = "http://localhost:5173"
    else:
        pkg_path = get_resource_path("src/package.json")
        dist_path = get_resource_path("web/dist/index.html")
        url = f"file:///{dist_path.as_posix()}"

    with open(pkg_path) as f:
        package = json.load(f)

    wv.create_window(
        title=package["name"],
        url=url
    )

    wv.start(
        private_mode=True,
        debug=args.dev,
    )

if __name__ == "__main__":
    window()