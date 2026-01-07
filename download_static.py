#tento subor stahuje staticke data z PID OpenData na nasledujucich 14 dni
#dokumentacia je na https://pid.cz/en/opendata/, zalozka Documentation
import requests
import os

GTFS_URL = "http://data.pid.cz/PID_GTFS.zip"
STOPS_URL = "https://data.pid.cz/stops/xml/StopsByName.xml"

GTFS_PATH = "data/raw/PID_GTFS.zip"
STOPS_PATH = "data/raw/STOPS_GROUPS.xml"

def download(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, mode="wb") as file:
        file.write(response.content)
        
download(GTFS_URL, GTFS_PATH)
download(STOPS_URL, STOPS_PATH)