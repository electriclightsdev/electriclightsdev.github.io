#!/usr/bin/env python3
"""
generate_manifest.py
Run this from your repo root whenever you add/remove memes.
It scans assets/memes/ and writes memes.json to the repo root.

Usage:
    python generate_manifest.py
"""

import os
import json

MEMES_DIR = os.path.join("assets", "memes")
OUTPUT_FILE = "memes.json"

SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".webm"}

def generate():
    if not os.path.isdir(MEMES_DIR):
        print(f"ERROR: Directory '{MEMES_DIR}' not found.")
        print("Make sure you run this script from your repo root.")
        return

    files = []
    for fname in sorted(os.listdir(MEMES_DIR)):
        ext = os.path.splitext(fname)[1].lower()
        if ext in SUPPORTED_EXTENSIONS:
            files.append(fname)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(files, f, indent=2)

    print(f"✅ memes.json written with {len(files)} file(s):")
    for f in files:
        print(f"   - {f}")

if __name__ == "__main__":
    generate()
