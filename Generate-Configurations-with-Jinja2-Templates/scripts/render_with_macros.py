#!/usr/bin/env python3

import os
import yaml
from jinja2 import Environment, FileSystemLoader


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    templates_dir = os.path.join(base_dir, "templates/cisco")
    data_file = os.path.join(base_dir, "data/devices/router1.yml")
    output_file = os.path.join(base_dir, "output/router1_macro_config.txt")

    env = Environment(
        loader=FileSystemLoader(templates_dir),
        trim_blocks=True,
        lstrip_blocks=True
    )

    with open(data_file, 'r') as f:
        device_data = yaml.safe_load(f)

    template = env.get_template("router_with_macros.j2")
    config = template.render(device_data)

    with open(output_file, 'w') as f:
        f.write(config)

    print(f"Configuration generated: {output_file}")


if __name__ == "__main__":
    main()
