import alacritty_path as ap
import change_theme
import cli
import font
import padding
import yaml_loader

if __name__ == '__main__':

    yaml_path = ap.get_alacritty_path()
    ala_config = yaml_loader.load_yaml(yaml_path)

    args = cli.get_cli_args()

    if args.size is not None:
        if args.size <= 0:
            raise "Size must be greater than 0"
        ala_config['font']['size'] = args.size
    if args.theme is not None:
        change_theme.charge_theme_config(args.theme, ala_config)
    if args.font is not None:
        font.change_font(args.font, ala_config)
    if args.padding is not None:
        padding.change_padding(args.padding, ala_config)

    yaml_loader.save_yaml(yaml_path, ala_config)
