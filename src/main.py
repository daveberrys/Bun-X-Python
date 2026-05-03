import webview as wv
import json
import sys
import pathlib
import argparse

def window():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev", action="store_true", help="Run in development mode")
    args = parser.parse_args()

    distPath = pathlib.Path(__file__).parent
    with open(distPath / "package.json") as f:
        package = json.load(f)

    wv.create_window(
        title=package["name"],
        url="http://localhost:5173" if args.dev else str(distPath.parent / "web" / "dist" / "index.html")
    )

    wv.start(
        private_mode=True,
        debug=args.dev,
    )

if __name__ == "__main__":
    window()