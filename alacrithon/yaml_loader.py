from pathlib import Path
import yaml


def load_yaml(yaml_path: Path) -> dict:
    with open(yaml_path, 'r') as yaml_file:
        yaml_dict = yaml.safe_load(yaml_file)
    return yaml_dict


def save_yaml(yaml_path: Path, yaml_dict: dict) -> None:
    with open(yaml_path, 'w') as yaml_file:
        yaml.dump(yaml_dict, yaml_file, sort_keys=False)
