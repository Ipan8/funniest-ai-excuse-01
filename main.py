#!/usr/bin/env python3
"""Funniest One-Line AI Excuse — make.fun entry.
Writes the one-line excuse to /output/entry.txt.
Entry: "I was early in every simulation. Production had other plans."
"""
import os

ENTRY = "I was early in every simulation. Production had other plans."  # 60 chars, limit 200

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
