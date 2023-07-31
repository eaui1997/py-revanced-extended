import os

from src.build import Build

# Use a dictionary to store the app names and their corresponding patches
app_info = {
    "youtube": {
        "exclude_patches": "custom-branding-icon-revancify-blue,custom-branding-youtube-name",
        "include_patches": "custom-branding-icon-revancify-red"
    },
    "youtube-music": {
        "exclude_patches": ""
        "include_patches": ""
    },

# Loop through the dictionary and build each app with its patches
for app_name, patches in app_info.items():
    # Create a new namespace object for each app name and its patches
    args = argparse.Namespace(app_name=app_name, exclude_patches=patches["exclude_patches"], include_patches=patches["include_patches"])
    build = Build(args)
    build.run_build()
    
