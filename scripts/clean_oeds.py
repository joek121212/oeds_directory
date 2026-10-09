# ######################################################
# Clean OEDS Data and Output Latest Copy
# ######################################################
#
# Purpose:
# Describe what the script does
#
# Inputs:
# - 
#
# Outputs:
# - 
#
# Notes:
# - 
#
# ######################################################

# %%
# =========================================
# Imports
# =========================================
"""Copy raw OEDS snapshot files into data/latest, adding source and date columns.

How to use:
  1. Create a folder named for the day you ran the OEDS report, e.g. data/snapshots/2026-10-09/
  2. Put the raw CSVs from OEDS in it.
  3. In the terminal, from the repo folder, run:  python publish_oeds.py
The script automatically uses the newest dated folder.
"""
from pathlib import Path

import pandas as pd

# %%
# =========================================
# Configuration
# =========================================

# %%
# =========================================
# Transformations
# =========================================
repo = Path(__file__).parent.parent
# %%
snapshots_root = repo / "data" / "snapshots"
latest_dir = repo / "data" / "latest"

# Use the newest dated folder (YYYY-MM-DD names sort correctly as text).
# The folder name IS the retrieved date, so there is nothing to edit.
folders = sorted(p for p in snapshots_root.glob("*") if p.is_dir()) if snapshots_root.exists() else []
if not folders:
    raise SystemExit(
        f"No snapshot folders found in:\n  {snapshots_root}\n"
        "Create one named for today (e.g. 2026-10-09) and put your raw CSVs inside."
    )
snapshot_dir = folders[-1]
SNAPSHOT_DATE = snapshot_dir.name
print(f"Using snapshot folder: {snapshot_dir.name}")
# %%
csv_files = sorted(snapshot_dir.glob("*.csv"))
if not csv_files:
    raise SystemExit(f"No .csv files found in:\n  {snapshot_dir}")

latest_dir.mkdir(parents=True, exist_ok=True)

for raw_file in csv_files:
    # Read everything as text so codes like 012345 keep their leading zeros.
    # utf-8-sig quietly handles the invisible marker some exports start with.
    df = pd.read_csv(raw_file, dtype=str, keep_default_na=False, encoding="utf-8-sig", header = 1)

    df.insert(0, "source_file", raw_file.name)
    df.insert(1, "retrieved_date", SNAPSHOT_DATE)

    out_file = latest_dir / raw_file.name
    df.to_csv(out_file, index=False, encoding="utf-8")
    print(f"{raw_file.name}: wrote {len(df)} rows -> {out_file}")
# %%
