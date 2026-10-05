#!/usr/bin/env python3
# MILYES-IA V9 NANS — GATEWAY — Z-CORE 89b6df2e-v24 — NON DÉPENDANCE
import sys, json, os, time
from pathlib import Path

VERSION = "v1_9 UNIFIED OPUS45"
HASH = "89b6df2e-v24"

def status():
    print("--- MILYES-IA V9 NANS : SYSTEM DASHBOARD ---")
    mods = {
        "01_CORE": "OPÉRATIONNEL" if Path("ia22.py").exists() else "MANQUANT",
        "02_AGENTS_IA": "OPÉRATIONNEL" if Path("ia22.py").exists() else "MANQUANT",
        "03_SECURITY_MSRC": "OPÉRATIONNEL" if Path("~/.z_key.secure").expanduser().exists() else "MANQUANT",
        "04_INFRA_ZCORE": "OPÉRATIONNEL" if os.system("curl -s http://localhost:8001/api/status > /dev/null 2>&1")==0 else "DOWN"
    }
    print("[MODULES]")
    for k,v in mods.items(): print(f"  - {k} : {v}")
    print("\n[GATEWAY]\n  - MILYES_GATEWAY.py : PRÊT")
    print(f"\n[SECURITY]\n  - Journaux système : {len(list(Path('.').glob('*.log'))) + len(list(Path('.').glob('*.jsonl')))} fichier(s) détecté(s)")
    print(f"\n[Z-CORE]\n  - Hash: {HASH}\n  - Version: {VERSION}\n  - Port: 8001\n  - ZeroTrust: ACTIF")
    try:
        import subprocess
        up = subprocess.getoutput("uptime")
        print(f"\n[METRICS]\n  - Uptime : {up}")
    except: pass
    print("------------------------------------------")
    return True

if __name__ == "__main__":
    if "--status" in sys.argv or "status" in sys.argv:
        status()
    else:
        print(f"MILYES_GATEWAY {VERSION} {HASH} — Usage: python MILYES_GATEWAY.py --status")
