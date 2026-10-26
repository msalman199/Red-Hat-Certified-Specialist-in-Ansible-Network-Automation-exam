#!/usr/bin/env python3

import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warnings for testing
urllib3.disable_warnings(InsecureRequestWarning)

# Controller configuration
CONTROLLER_HOST = "https://your-controller.example.com"
USERNAME = "admin"
PASSWORD = "your-password"

def test_controller_connection():
    """Test basic connectivity to Ansible Controller"""
    
    try:
        # Test basic connectivity
        auth_url = f"{CONTROLLER_HOST}/api/v2/me/"
        
        response = requests.get(
            auth_url,
            auth=(USERNAME, PASSWORD),
            verify=False,
            timeout=10
        )
        
        if response.status_code == 200:
            user_info = response.json()
            print(f"✓ Successfully connected to controller")
            print(f"✓ Authenticated as: {user_info.get('username')}")
            return True
        else:
            print(f"✗ Connection failed with status: {response.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Ansible Controller connectivity...")
    test_controller_connection()
