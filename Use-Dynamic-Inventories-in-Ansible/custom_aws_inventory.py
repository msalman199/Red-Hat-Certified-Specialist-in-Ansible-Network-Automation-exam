#!/usr/bin/env python3
"""
Custom AWS Dynamic Inventory Script
Provides additional functionality beyond standard plugins
"""

import json
import boto3
import argparse
import sys
from botocore.exceptions import ClientError, NoCredentialsError

class AWSInventory:
    def __init__(self):
        self.inventory = {}
        self.read_cli_args()
        
        # Initialize AWS clients
        try:
            self.ec2_client = boto3.client('ec2')
            self.ec2_resource = boto3.resource('ec2')
        except NoCredentialsError:
            print("AWS credentials not found!", file=sys.stderr)
            sys.exit(1)
    
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--host', action='store')
        self.args = parser.parse_args()
    
    def get_instances(self):
        """Get all EC2 instances"""
        try:
            response = self.ec2_client.describe_instances(
                Filters=[
                    {'Name': 'instance-state-name', 'Values': ['running']}
                ]
            )
            return response['Reservations']
        except ClientError as e:
            print(f"Error fetching instances: {e}", file=sys.stderr)
            return []
    
    def add_host_to_group(self, group, host):
        """Add host to inventory group"""
        if group not in self.inventory:
            self.inventory[group] = {'hosts': [], 'vars': {}}
        self.inventory[group]['hosts'].append(host)
    
    def get_host_info(self, instance):
        """Extract host information from instance"""
        tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        
        return {
            'ansible_host': instance.get('PublicIpAddress', instance.get('PrivateIpAddress')),
            'ec2_instance_id': instance['InstanceId'],
            'ec2_instance_type': instance['InstanceType'],
            'ec2_region': instance['Placement']['AvailabilityZone'][:-1],
            'ec2_zone': instance['Placement']['AvailabilityZone'],
            'ec2_vpc_id': instance.get('VpcId'),
            'ec2_subnet_id': instance.get('SubnetId'),
            'ec2_state': instance['State']['Name'],
            'ec2_tags': tags,
            'ansible_user': self.get_ansible_user(tags, instance)
        }
    
    def get_ansible_user(self, tags, instance):
        """Determine appropriate ansible user"""
        os_tag = tags.get('OS', '').lower()
        image_id = instance.get('ImageId', '')
        
        if 'ubuntu' in os_tag or 'ami-' in image_id:
            return 'ubuntu'
        elif 'rhel' in os_tag or 'redhat' in os_tag:
            return 'ec2-user'
        else:
            return 'ec2-user'  # default
    
    def build_inventory(self):
        """Build the complete inventory"""
        self.inventory = {
            '_meta': {
                'hostvars': {}
            }
        }
        
        reservations = self.get_instances()
        
        for reservation in reservations:
            for instance in reservation['Instances']:
                tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
                
                # Use Name tag or instance ID as hostname
                hostname = tags.get('Name', instance['InstanceId'])
                
                # Get host information
                host_info = self.get_host_info(instance)
                self.inventory['_meta']['hostvars'][hostname] = host_info
                
                # Add to 'all' group
                self.add_host_to_group('all', hostname)
                
                # Group by environment
                env = tags.get('Environment', 'untagged')
                self.add_host_to_group(f'env_{env}', hostname)
                
                # Group by role
                role = tags.get('Role', 'generic')
                self.add_host_to_group(f'role_{role}', hostname)
                
                # Group by instance type
                instance_type = instance['InstanceType']
                self.add_host_to_group(f'type_{instance_type}', hostname)
                
                # Group by availability zone
                az = instance['Placement']['AvailabilityZone']
                self.add_host_to_group(f'az_{az}', hostname)
                
                # Custom business logic groups
                if 'web' in role.lower():
                    self.add_host_to_group('webservers', hostname)
                if 'db' in role.lower() or 'database' in role.lower():
                    self.add_host_to_group('databases', hostname)
                if 'lb' in role.lower() or 'load' in role.lower():
                    self.add_host_to_group('loadbalancers', hostname)
    
    def get_host_vars(self, hostname):
        """Get variables for a specific host"""
        return self.inventory['_meta']['hostvars'].get(hostname, {})
    
    def run(self):
        """Main execution method"""
        if self.args.list:
            self.build_inventory()
            print(json.dumps(self.inventory, indent=2))
        elif self.args.host:
            self.build_inventory()
            print(json.dumps(self.get_host_vars(self.args.host), indent=2))
        else:
            print("Usage: --list or --host <hostname>")

if __name__ == '__main__':
    inventory = AWSInventory()
    inventory.run()
