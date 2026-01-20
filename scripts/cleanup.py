#!/usr/bin/env python3
"""Cleanup old temp files from deployment staging areas."""
import os, glob, time

STAGING = r"C:\Staging\Updates"
MAX_AGE_DAYS = 30

def cleanup():
    cutoff = time.time() - (MAX_AGE_DAYS * 86400)
    for f in glob.glob(os.path.join(STAGING, "*.tmp")):
        if os.path.getmtime(f) < cutoff:
            os.remove(f)
            print(f"Removed: {f}")

if __name__ == "__main__":
    cleanup()
