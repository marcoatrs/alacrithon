from pathlib import Path

import yaml_loader


def charge_theme_config(theme:str, ala_config:dict):
    themes_path = Path(__file__).parents[1] / 'templates'
    if not theme.endswith('yml'):
        theme += '.yml'
    themes_path /= theme
    if not themes_path.exists():
        print('Theme not found')
        return
    ala_config['colors'] = yaml_loader.load_yaml(themes_path).get('colors')
