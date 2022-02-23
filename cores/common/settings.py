import json

def get(core, key):
    settings = json.load(open(f"./cores/{core}/settings.json", encoding="utf8"))
    return settings[key]