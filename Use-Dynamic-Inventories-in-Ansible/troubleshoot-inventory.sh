#!/bin/bash

INVENTORY_FILE="${1:-aws_ec2.yml}"

echo "Troubleshooting Dynamic Inventory: $INVENTORY_FILE"
echo "=================================================="

echo "1. Checking inventory file syntax..."
if ansible-inventory -i "$INVENTORY_FILE" --list > /dev/null 2>&1; then
    echo "   ✓ Inventory file syntax is valid"
else
    echo "   ✗ Inventory file has syntax errors:"
    ansible-inventory -i "$INVENTORY_FILE" --list
    exit 1
fi

echo "2. Testing AWS connectivity..."
if aws sts get-caller-identity > /dev/null 2>&1; then
    echo "   ✓ AWS credentials are working"
else
    echo "   ✗ AWS credentials issue"
    echo "   Check ~/.aws/credentials and ~/.aws/config"
fi

echo "3. Checking discovered hosts..."
HOST_COUNT=$(ansible-inventory -i "$INVENTORY_FILE" --list | jq '._meta.hostvars | keys | length' 2>/dev/null || echo "0")
echo "   Discovered hosts: $HOST_COUNT"

if [ "$HOST_COUNT" -eq 0 ]; then
    echo "   ⚠ No hosts discovered. Check:"
    echo "     - AWS regions in inventory file"
    echo "     - Instance filters"
    echo "     - Instance states (running/stopped)"
fi

echo "4. Testing host connectivity..."
ansible all -i "$INVENTORY_FILE" -m ping --one-line 2>/dev/null | head -5

echo "5. Checking groups..."
ansible-inventory -i "$INVENTORY_FILE" --graph | head -20

echo "Troubleshooting complete!"
