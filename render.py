#!/usr/bin/env python3
"""Placeholder render script - to be replaced with actual storybook renderer."""
import argparse
import os

p = argparse.ArgumentParser()
p.add_argument("--episode", required=True)
p.add_argument("--content-dir", required=True)
args = p.parse_args()

os.makedirs("output", exist_ok=True)
print(f"Would render {args.episode} from {args.content_dir}")
print("TODO: copy actual render_chunked.py logic here")
