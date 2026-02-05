#!/usr/bin/env python3
"""Stub for syncing hardware inventory with asset management DB."""

ASSET_DB = "https://assets.internal.local/api/v2"

def sync_inventory():
    # TODO: implement SNMP walk + asset DB POST
    print("inventory_sync: not yet implemented")

if __name__ == "__main__":
    sync_inventory()

# Phase 2: batch mode
BATCH_SIZE = 50
