#!/usr/bin/env python3

import os
import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


def load_device_data(data_file):
    """Load device data from a YAML file."""
    try:
        with open(data_file, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: Data file {data_file} not found")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None


def generate_configuration(template_dir, template_name, data, output_file):
    """Render a Jinja2 template with the given data and write it to a file."""
    try:
        env = Environment(
            loader=FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )
        template = env.get_template(template_name)

        if 'generation_date' not in data:
            data['generation_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        config = template.render(data)

        with open(output_file, 'w') as file:
            file.write(config)

        print(f"Configuration generated successfully: {output_file}")
        return True

    except Exception as e:
        print(f"Error generating configuration: {e}")
        return False


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    template_dir = os.path.join(base_dir, "templates/cisco")
    template_name = "basic_router.j2"
    data_dir = os.path.join(base_dir, "data/devices")
    output_dir = os.path.join(base_dir, "output")

    os.makedirs(output_dir, exist_ok=True)

    for filename in sorted(os.listdir(data_dir)):
        if filename.endswith(('.yml', '.yaml')):
            print(f"\nProcessing {filename}...")

            data_file = os.path.join(data_dir, filename)
            device_data = load_device_data(data_file)

            if device_data and device_data.get('vendor') == 'cisco':
                device_name = os.path.splitext(filename)[0]
                output_file = os.path.join(output_dir, f"{device_name}_config.txt")
                generate_configuration(template_dir, template_name, device_data, output_file)


if __name__ == "__main__":
    main()
