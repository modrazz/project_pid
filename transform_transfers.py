import os
import zipfile
import pandas as pd


GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "transfers.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str, on_bad_lines="warn")

# changing type to numeric for purely numeric columns 
for c in ["transfer_type", "min_transfer_time", "max_waiting_time"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

# keep only useful columns
keep = [
    "from_stop_id",
    "to_stop_id",
    "from_trip_id",
    "to_trip_id",
    "transfer_type",
]
keep = [c for c in keep if c in df.columns]
df = df[keep].copy()

out_file = os.path.join(OUT_PATH, "transfers_processed.csv")
df.to_csv(out_file, index=False)
