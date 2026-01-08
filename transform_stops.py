import os
import zipfile
import pandas as pd


GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "stops.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str)

# location_type normalization
df["location_type"] = df["location_type"].replace({"": "0"}).fillna("0")
df["location_type"] = pd.to_numeric(df["location_type"], errors="coerce").fillna(0).astype(int)

# keep only 0 (stop) / 1 (station)
df = df[df["location_type"].isin([0, 1])].copy()

# setting parent station (if exists -> parent_station, if not -> fallback to stop_id )
df["parent_station"] = df["parent_station"].replace({"": pd.NA})
df["parent_station"] = df["parent_station"].fillna(df["stop_id"])

# does parent exist? if not -> fallback to stop_id
valid_ids = set(df["stop_id"].astype(str))
bad_parent = ~df["parent_station"].astype(str).isin(valid_ids)
df.loc[bad_parent, "parent_station"] = df.loc[bad_parent, "stop_id"]

# more general grouping 
df["stop_num"] = df["stop_id"].str.extract(r"^U(\d+)[ZN]", expand=False)
df["stop_num"] = pd.to_numeric(df["stop_num"], errors="coerce").astype("Int64")

# only keeping useful columns
keep = [
    "stop_id",
    "stop_name",
    "stop_lat",
    "stop_lon",
    "zone_id",
    "location_type",
    "parent_station",
    "stop_num",
    "wheelchair_boarding",
    "platform_code",
]
keep = [c for c in keep if c in df.columns]
df = df[keep].copy()

out_file = os.path.join(OUT_PATH, "stops_processed.csv")
df.to_csv(out_file, index=False)
