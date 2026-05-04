import webview as wv
import json
import sys
import pathlib
import argparse
from API import API

appName = "Bun X Python"

def getResourcePath(relative_path):
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return pathlib.Path(sys._MEIPASS) / relative_path
    return pathlib.Path(__file__).parent / relative_path

def window():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Run in development mode")
    args = parser.parse_args()

    if args.dev:
        url = "http://localhost:5173"
    else:
        distPath = getResourcePath("web/dist/index.html")
        url = f"file:///{distPath.as_posix()}"

    wv.create_window(
        title=appName,
        url=url,
        js_api=API()
    )

    wv.start(
        private_mode=True,
        debug=args.dev,
        icon=str(getResourcePath("web/public/vite.ico"))
    )

if __name__ == "__main__":
    window()