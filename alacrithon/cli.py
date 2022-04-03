import argparse


def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--size', type=int)
    parser.add_argument('-t', '--theme', type=str)
    parser.add_argument('-f', '--font', type=str)
    parser.add_argument('-p', '--padding', nargs='+', type=int)
    return parser.parse_args()


"""
-f font
-s size
-t theme
-c cursor
-p padding
"""