from re import S


def change_padding(padding: list, ala_config: dict):
    if len(padding) == 2:
        x, y = padding
    elif len(padding) == 1:
        x = padding[0]
        y = padding[0]
    else:
        x, y = padding[0], padding[1]
    if x > -1:
        ala_config['window']['padding']['x'] = x
    if y > -1:
        ala_config['window']['padding']['y'] = y
