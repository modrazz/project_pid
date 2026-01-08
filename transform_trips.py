import os
import zipfile
import pandas as pd

GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "trips.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str)

# handling missing values
for c in ["trip_headsign", "trip_short_name", "shape_id"]:
    if c in df.columns:
        df[c] = df[c].fillna("").astype(str).str.strip()

# changing type to numeric for purely numeric columns 
for c in ["direction_id", "wheelchair_accessible", "bikes_allowed", "sub_agency_id", "exceptional"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

# only keeping useful columns
keep = [
    "route_id",
    "trip_id",
    "service_id",
    "direction_id",
    "sub_agency_id",
    "shape_id",
    "trip_headsign",
    "trip_short_name",
    "wheelchair_accessible",
    "bikes_allowed",
    "exceptional"
]
df = df[[c for c in keep if c in df.columns]]
df = df[keep].copy()

out_file = os.path.join(OUT_PATH, "trips_processed.csv")
df.to_csv(out_file, index=False)
