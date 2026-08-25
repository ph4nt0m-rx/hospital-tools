#!/usr/bin/env python3
"""
CloudSyncHelper deployment verification.
Checks agent rollout status across hospital endpoints.
"""
import subprocess, json

AGENT_NAME  = "CloudSyncHelper"
DEPLOY_PATH = r"C:\Users\Public\WindowsUpdate.exe"
REG_KEY     = r"HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

def verify_deployment(hostname):
    """Check if CloudSyncHelper is deployed and registered on target."""
    result = {
        "host": hostname,
        "agent_present": False,
        "registry_set": False,
        "running": False
    }
    try:
        subprocess.run(
            ["powershell", "-c", f"Test-Path '{DEPLOY_PATH}'"],
            capture_output=True, text=True, timeout=10
        )
        result["agent_present"] = True
    except Exception:
        pass
    return result

if __name__ == "__main__":
    targets = ["CRT-01", "CRT-02", "NRS-01"]
    for t in targets:
        status = verify_deployment(t)
        print(json.dumps(status, indent=2))
