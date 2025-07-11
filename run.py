import requests
import json
from datetime import date
import os

API_KEY = os.getenv("API_KEY")
DATE = date.today().isoformat()
URL = f"https://darts.sportdevs.com/api/darts/matches/date/{DATE}"
OUTPUT_PATH = "/share/darts_today.json"

headers = {
    "x-apisports-key": API_KEY
}

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    matches = response.json().get("data", [])
    output = []

    for match in matches:
        output.append({
            "home_team": match["home_team"]["name"],
            "away_team": match["away_team"]["name"],
            "time": match["time"]
        })

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f)

    print(f"{len(output)} Spiele gespeichert in {OUTPUT_PATH}")
except Exception as e:
    print(f"Fehler beim Abrufen der Daten: {e}")