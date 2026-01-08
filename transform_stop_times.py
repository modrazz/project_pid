import os
import zipfile
import pandas as pd


GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "stop_times.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str)

# changing type to numeric for purely numeric columns 
for c in ["stop_sequence", "pickup_type", "drop_off_type"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

# only keeping useful columns
keep = [
    "trip_id",
    "stop_id",
    "stop_sequence",
    "arrival_time",
    "departure_time",
    "pickup_type",
    "drop_off_type",
]
keep = [c for c in keep if c in df.columns]
df = df[keep].copy()

out_file = os.path.join(OUT_PATH, "stop_times_processed.csv")
df.to_csv(out_file, index=False)
