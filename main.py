import argparse

from src.build import Build

app_names = ["youtube", ""]
exclude_patches = ["custom-branding-icon-revancify-blue,custom-branding-youtube-name", ""]
include_patches = ["custom-branding-icon-revancify-red", ""]

for i in range(len(app_names)):
  
    app_name = app_names[i]
    exclude_patch = exclude_patches[i]
    include_patch = include_patches[i]


    args = argparse.Namespace(app_name=app_name, exclude_patches=exclude_patch, include_patches=include_patch)

    build = Build(args)

    build.run_build()
  
