import argparse

from src.build import Build


def main():
    parser = argparse.ArgumentParser("revanced_build")

    # Exclude Patches: patch1,patch2,patch3
    parser.add_argument(
        "--exclude-patches",
        help="Exclude patches from build",
        type=str,
        default="none",
    )

    args = parser.parse_args()

    build_args = {"exclude_patches": "custom-branding-icon-afn-red,custom-branding-name,custom-video-speed,hide-mix-playlists"}

    build = Build("youtube", **build_args)

    build.run_build()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(1)