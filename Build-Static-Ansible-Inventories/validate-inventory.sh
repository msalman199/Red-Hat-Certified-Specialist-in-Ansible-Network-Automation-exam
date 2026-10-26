#!/bin/bash

INVENTORY_FILE="$1"

if [ -z "$INVENTORY_FILE" ]; then
    echo "Usage: $0 <inventory-file>"
    exit 1
fi

if [ ! -f "$INVENTORY_FILE" ]; then
    echo "Error: Inventory file '$INVENTORY_FILE' not found"
    exit 1
fi

echo "Validating inventory file: $INVENTORY_FILE"
echo "========================================="

# Test syntax
echo "1. Testing YAML syntax..."
if ansible-inventory -i "$INVENTORY_FILE" --list > /dev/null 2>&1; then
    echo "   ✓ YAML syntax is valid"
else
    echo "   ✗ YAML syntax error detected"
    ansible-inventory -i "$INVENTORY_FILE" --list
    exit 1
fi

# List all hosts
echo "2. Listing all hosts..."
ansible-inventory -i "$INVENTORY_FILE" --list-hosts all

# Test connectivity
echo "3. Testing connectivity..."
if ansible -i "$INVENTORY_FILE" all -m ping > /dev/null 2>&1; then
    echo "   ✓ All hosts are reachable"
else
    echo "   ⚠ Some hosts may not be reachable"
    ansible -i "$INVENTORY_FILE" all -m ping
fi

echo "========================================="
echo "Validation complete"
