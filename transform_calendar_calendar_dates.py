import os
import zipfile
import pandas as pd


GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
CAL_NAME  = "calendar.txt"
CAL_DATES_NAME = "calendar_dates.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(CAL_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str)

# changing type to numeric for flag 0/1 columns
day_cols = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for c in day_cols:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

out_file = os.path.join(OUT_PATH, "calendar_processed.csv")
df.to_csv(out_file, index=False)




#same process but for calendar_dates.txt
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(CAL_DATES_NAME) as file_txt:
        cd = pd.read_csv(file_txt, dtype=str)


cd["exception_type"] = pd.to_numeric(cd["exception_type"], errors="coerce").astype("Int64")

dates_out = os.path.join(OUT_PATH, "calendar_dates_processed.csv")
cd.to_csv(dates_out, index=False)
