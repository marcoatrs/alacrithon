import os


def get_default_config(system: str) -> dict:

    if system == 'Windows':
        wd_path = r"C:\\Users\\{0}".format(os.getenv('USERNAME'))
    elif system == 'Linux':
        wd_path = '/home/alacritty'

    default_yaml = {
        "colors": {
            "primary": {
                "background": "#1e2127",
                "foreground": "#D8DEE9"
            }
        },
        "font": {
            "normal": {
                "family": "Consolas",
                "style": "Regular"
            },
            "bold": {
                "family": "Consolas",
                "style": "Regular"
            },
            "italic": {
                "family": "Consolas",
                "style": "Regular"
            },
            "bold_italic": {
                "family": "Consolas",
                "style": "Regular"
            },
            "size": 12
        },
        "window": {
            "padding": {
                "x": 5,
                "y": 5
            },
            "startup_mode": "Windowed"
        },
        "draw_bold_text_with_bright_colors": True,
        "live_config_reload": True,
        "scrolling": {
            "history": 2000,
            "multiplier": 10
        },
        "cursor": {
            "style": {
                "shape": "Underline",
                "blinking": "on"
            }
        },
        "working_directory": str(wd_path)
    }
    return default_yaml
