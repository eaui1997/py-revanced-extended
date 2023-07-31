import argparse

from src.build import Build

app_name = "youtube"
exclude_patches = "custom-branding-icon-revancify-blue,custom-branding-youtube-name"

args = argparse.Namespace(app_name=app_name, exclude_patches=exclude_patches)

build = Build(args)
build.run_build()
