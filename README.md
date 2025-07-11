# SportsDevs Darts Add-on for Home Assistant

Dieses Add-on holt täglich die tagesaktuellen Darts-Spiele über die [SportDevs Darts API](https://docs.sportdevs.com/docs/sportdetect_authentication_darts) und speichert sie in einer JSON-Datei, die Home Assistant über einen `file`-Sensor auslesen kann.

## 🔧 Funktionen

- Abruf der Spiele des aktuellen Tages
- Speicherung im `/share/darts_today.json`
- Integration über Datei-Sensor in Home Assistant
- Keine Cloud-Kommunikation außer zum API-Anbieter

## 🧰 Installation

1. Entpacke den Ordner in dein Home Assistant `addons`-Verzeichnis (`/addons/sportsdevs_darts_addon`)
2. Starte Home Assistant neu
3. Installiere das Add-on über die Benutzeroberfläche
4. Trage deinen API-Key in die Konfiguration ein

## 📡 Integration als Sensor

```yaml
sensor:
  - platform: file
    name: Darts Spiele Heute
    file_path: /share/darts_today.json
    value_template: "{{ value_json[0].home_team }} vs {{ value_json[0].away_team }}"
    scan_interval: 3600
```

## 💬 Beispielausgabe

```json
[
  {
    "home_team": "Michael Smith",
    "away_team": "Gerwyn Price",
    "time": "19:00"
  },
  {
    "home_team": "Peter Wright",
    "away_team": "Jonny Clayton",
    "time": "20:30"
  }
]
```

## 📃 Lizenz

MIT License – frei nutzbar, aber ohne Garantie.