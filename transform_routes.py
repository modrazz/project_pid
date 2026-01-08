import os
import zipfile
import pandas as pd


GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "routes.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str)

# dealing with missing long names
df["route_long_name"] = df["route_long_name"].fillna("")

# changing type to numeric for 0/1 flag columns and route_type
for c in ["route_type", "is_night", "is_regional", "is_substitute_transport"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

# only keeping useful columns
keep = [
    "route_id",
    "route_short_name",
    "route_long_name",
    "route_type",
    "is_night",
    "is_regional",
    "is_substitute_transport",
]
keep = [c for c in keep if c in df.columns]
df = df[keep].copy()

out_file = os.path.join(OUT_PATH, "routes_processed.csv")
df.to_csv(out_file, index=False)


