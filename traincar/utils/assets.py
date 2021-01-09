import os
import pathlib

def build_asset_path(name):
    path = pathlib.Path(__file__).parent.parent
    return os.path.join(path, "assets", name)
