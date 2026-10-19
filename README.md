# Mera Aaina Render

Public render infrastructure for Mera Aaina videos.

## How it works

1. Content (scripts) lives in the private `mera-aaina-content` repo
2. This repo holds the render workflow (public = unlimited Actions minutes)
3. Trigger via Actions tab → "Render Mera Aaina Video" → enter episode ID

## Setup

Add `GH_PAT` secret (Settings → Secrets → Actions):
- Personal Access Token with `repo` scope
- Used to checkout the private content repo
