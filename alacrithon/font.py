import json
from pathlib import Path


with open(Path().parent / 'templates' / 'fonts.json', 'r') as json_file:
    fonts = json.load(json_file)


def change_font(font, ala_conf: dict):
    font = fonts.get(font, font)
    for font_type in ['bold', 'bold_italic', 'italic', 'normal']:
        ala_conf['font'][font_type]['family'] = font
