#!/usr/bin/env python3

import os
import yaml
from jinja2 import Environment, FileSystemLoader
from datetime import datetime


class ConfigurationGenerator:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.templates_dir = os.path.join(base_dir, "templates")
        self.data_dir = os.path.join(base_dir, "data/devices")
        self.output_dir = os.path.join(base_dir, "output")

        os.makedirs(self.output_dir, exist_ok=True)

        self.vendor_templates = {
            'cisco': {
                'router': 'cisco/basic_router.j2',
            },
            'juniper': {
                'router': 'juniper/basic_router.j2',
            },
        }

    def load_device_data(self, data_file):
        try:
            with open(data_file, 'r') as file:
                data = yaml.safe_load(file)
            if 'generation_date' not in data:
                data['generation_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return data
        except FileNotFoundError:
            print(f"Error: Data file {data_file} not found")
            return None
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return None

    def get_template_path(self, vendor, device_type):
        vendor = vendor.lower()
        device_type = device_type.lower()
        vendor_map = self.vendor_templates.get(vendor)
        if not vendor_map:
            return None
        return vendor_map.get(device_type, next(iter(vendor_map.values())))

    def generate_configuration(self, template_path, data, output_file):
        try:
            template_full_path = os.path.join(self.templates_dir, template_path)
            template_dir = os.path.dirname(template_full_path)
            template_name = os.path.basename(template_full_path)

            env = Environment(
                loader=FileSystemLoader(template_dir),
                trim_blocks=True,
                lstrip_blocks=True
            )

            template = env.get_template(template_name)
            config = template.render(data)

            with open(output_file, 'w') as file:
                file.write(config)

            print(f"Configuration generated: {output_file}")
            return True

        except Exception as e:
            print(f"Error generating configuration: {e}")
            return False

    def process_device(self, data_file):
        print(f"\nProcessing {os.path.basename(data_file)}...")

        device_data = self.load_device_data(data_file)
        if not device_data:
            return False

        vendor = device_data.get('vendor', 'cisco')
        device_type = device_data.get('device_type', 'router')

        print(f"  Vendor: {vendor}")
        print(f"  Device Type: {device_type}")

        template_path = self.get_template_path(vendor, device_type)
        if not template_path:
            print(f"  No template found for {vendor} {device_type}")
            return False

        print(f"  Template: {template_path}")

        device_name = os.path.splitext(os.path.basename(data_file))[0]
        output_file = os.path.join(self.output_dir, f"{device_name}_config.txt")

        return self.generate_configuration(template_path, device_data, output_file)

    def process_all_devices(self):
        print("Starting configuration generation...")

        success_count = 0
        total_count = 0

        for filename in sorted(os.listdir(self.data_dir)):
            if filename.endswith(('.yml', '.yaml')):
                total_count += 1
                data_file = os.path.join(self.data_dir, filename)
                if self.process_device(data_file):
                    success_count += 1

        print("\nSummary:")
        print(f"  Total devices: {total_count}")
        print(f"  Successful: {success_count}")
        print(f"  Failed: {total_count - success_count}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    generator = ConfigurationGenerator(base_dir)
    generator.process_all_devices()


if __name__ == "__main__":
    main()
