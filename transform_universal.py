import os
import zipfile
import pandas as pd

# change NAME_OF_THE_TEXT_FILE.txt to the name of the file you wish to transform from .txt to .csv

GTFS_PATH = "data/raw/PID_GTFS.zip"
OUT_PATH  = "data/processed"
TXT_NAME  = "NAME_OF_THE_TEXT_FILE.txt"

# read txt file from zip
with zipfile.ZipFile(GTFS_PATH, "r") as gtfs_zip:
    with gtfs_zip.open(TXT_NAME) as file_txt:
        df = pd.read_csv(file_txt, dtype=str, on_bad_lines="warn")

changeNum = False
# if there are purely numeric columns and you wish to change the type from string to int, then
# flip changeNum to True, and insert the names of the desired columns into the list in the for loop below

# changing type to numeric for purely numeric columns
if changeNum:
    for c in ["INSERT","NAMES","OF","COLUMNS"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("Int64")

keepCol = False
# if you only wish to keep certain columns and get rid of the rest, then flip keepCol to True,
# and insert the names of the desired columns into the list below

# keep only useful columns
keep = [
    "INSERT",
    "NAMES",
    "OF",
    "COLUMNS",
]
if keepCol:
    keep = [c for c in keep if c in df.columns]
    df = df[keep].copy()

# fill out the desired name of the output file in the line below
# keep in mind the file naming restrictions and the NECESSARY .csv file extension

out_file = os.path.join(OUT_PATH, "EXAMPLE_NAME.csv")
df.to_csv(out_file, index=False)
