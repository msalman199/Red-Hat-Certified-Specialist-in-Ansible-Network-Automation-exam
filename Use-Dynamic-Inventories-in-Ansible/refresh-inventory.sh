#!/bin/bash

INVENTORY_FILE="aws_ec2_cached.yml"
CACHE_DIR="/tmp/ansible-inventory-cache"

echo "Dynamic Inventory Cache Management"
echo "=================================="

case "$1" in
    "refresh")
        echo "Clearing cache and refreshing inventory..."
        rm -rf "$CACHE_DIR"
        ansible-inventory -i "$INVENTORY_FILE" --list > /dev/null
        echo "Cache refreshed successfully!"
        ;;
    "status")
        if [ -d "$CACHE_DIR" ]; then
            echo "Cache directory exists: $CACHE_DIR"
            echo "Cache files:"
            ls -la "$CACHE_DIR"
        else
            echo "No cache found"
        fi
        ;;
    "clear")
        echo "Clearing cache..."
        rm -rf "$CACHE_DIR"
        echo "Cache cleared!"
        ;;
    *)
        echo "Usage: $0 {refresh|status|clear}"
        echo "  refresh - Clear cache and reload inventory"
        echo "  status  - Show cache status"
        echo "  clear   - Clear cache only"
        exit 1
        ;;
esac
