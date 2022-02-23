import os
import hashlib
import unicodedata
import json
import music_tag
from PIL import Image

import directory_iterator
import formatter
import file_reader

settings = json.load(open('settings.json', encoding="utf8"))

ext = settings["ext"]
directory = "./" + settings["album"] + "/"
info_file = directory + settings["info"]
cover_file = directory + settings["cover"]

# iterate over files in that directory
dir_list = directory_iterator.list_by_ext(directory, ext)

track_id = 0
tracklist = []

for i in range(len(dir_list)):
    current_file = dir_list[i]

    track_id = i + 1

    # replace "1" by "01", "2" by "02", from 1 to 9
    display_track_id = formatter.extend_int(track_id)

    music = music_tag.load_file(current_file)
    length = music['#length'].values[0]
    size = os.path.getsize(current_file)

    #tags 
    music["tracktitle"] = str(music["tracktitle"]).lower().capitalize()

    track = {}

    track["id"] = str(track_id)
    track["title"] = formatter.clean_display_name(str(music["tracktitle"]))
    track["display_duration"] = str(formatter.convert(length))
    track["duration"] = str(length)

    track["file"] = {}
    track["file"]["name"] = formatter.clean_file_name(str(display_track_id) + " - " + str(music["tracktitle"])) + "." + ext
    track["file"]["ext"] = str(ext)
    track["file"]["size"] = str(size)
    track["file"]["md5"] = str(file_reader.get_hash(current_file, "md5"))
    track["file"]["sha1"] = str(file_reader.get_hash(current_file, "sha1"))

    tracklist.append(track)

# Cover edition
cover = {}
width, height = Image.open(cover_file).size

if width == 1000 and height == 1000:
    cover["name"] = "cover.jpg"
    cover["md5"] = file_reader.get_hash(cover_file, "md5")
    cover["sha1"] = file_reader.get_hash(cover_file, "md5")

infos = {
    "title": settings["album"],
    "artist": settings["artist"],
    "cover": cover,
    "tracklist": tracklist
}

# display in console
print()
print("Artiste : " + infos["artist"])
print("Album : " + infos["title"])
print("Nombre de titres : " + str(len(infos["tracklist"])))
print()

ask_to_display = input("Voulez-vous afficher le json (Y/N) ? ")

with open(info_file, 'w', encoding='utf8') as json_file:
    json.dump(infos, json_file, ensure_ascii=False, indent=4)

    if ask_to_display.lower() == "y":
        print(json.dumps(infos, indent=4))