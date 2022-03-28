import os
import platform
from pathlib import Path

import yaml_loader as yaml
from default_config import get_default_config


def get_alacritty_path() -> Path:
    system = platform.system()
    if system == 'Windows':
        alathon = Path(os.getenv('APPDATA')) / 'alacritty' / 'alacritty.yml'
    elif system == 'Linux':
        alathon = Path("aqui")
    if not alathon.exists():
        yaml_dict = get_default_config(system)
        yaml.save_yaml(alathon, yaml_dict)
    return alathon


if __name__ == '__main__':
    print(get_alacritty_path())
