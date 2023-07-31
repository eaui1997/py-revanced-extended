import argparse

from src.build import Build

app_name = "youtube"
exclude_patches = ""
include_patches = ""

args = argparse.Namespace(app_name=app_name, exclude_patches=exclude_patches, include_patches=include_patches)

build = Build(args)
build.run_build()
