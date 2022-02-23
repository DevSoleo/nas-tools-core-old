import json
import cores.common.settings as settings

# MODEL

def get_artists_list():
    return json.load(open(settings.get("music", "database_path"), encoding="utf8"))

def get_artist_info(artist, info):
    artist_infos = json.load(open(settings.get("music", "storage_path") + artist + "/infos.json", encoding="utf8"))
    return artist_infos[info]
