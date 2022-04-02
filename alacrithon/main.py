import change_theme
import cli
import yaml_loader
from alacritty_path import get_alacritty_path

if __name__ == '__main__':

    yaml_path = get_alacritty_path()
    ala_config = yaml_loader.load_yaml(yaml_path)

    args = cli.get_cli_args()

    if args.size is not None:
        if args.size <= 0:
            raise "Size must be greater than 0"
        ala_config['font']['size'] = args.size
    if args.theme is not None:
        change_theme.charge_theme_config(args.theme, ala_config)

    yaml_loader.save_yaml(yaml_path, ala_config)
