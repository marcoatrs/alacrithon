import argparse


def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    return parser.parse_args()


"""
-f font
-s size
-t theme
-c cursor

"""