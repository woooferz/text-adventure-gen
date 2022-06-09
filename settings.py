import json


VERSION = "v0.1 alpha"
VERSION_ID = 1
SETTINGS_FILE = "settings.json"

try:
    with open(SETTINGS_FILE, "r") as f:
        SETTINGS = json.load(f)
except json.decoder.JSONDecodeError:
    print("Error loading JSON.")
    exit(1)

    # SETTINGS = json.loads("settings.json")

# print(SETTINGS)
