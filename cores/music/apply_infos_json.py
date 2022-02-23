import os
import hashlib
import json
import music_tag
import json

settings = json.load(open('settings.json', encoding="utf8"))

ext = settings["ext"]
directory = "./" + settings["album"] + "/"
info_file = directory + settings["info"]
cover_file = directory + settings["cover"]

infos = json.load(open(info_file, "r", encoding="utf-8"))

tracklist = {}
for i in range(len(infos["tracklist"])):
    tracklist[infos["tracklist"][i]['file']["md5"]] = infos["tracklist"][i]['file']['name']
    
dir_list = os.listdir(directory)

# rename
for i in range(len(dir_list)):
    current_file = os.path.join(directory, dir_list[i])

    # checking if it is a file and if it has the correct extension
    if os.path.isfile(current_file) and current_file[len(current_file) - len(ext):] == ext:
        with open(current_file, "rb") as file_to_check:
            data = file_to_check.read()    
            md5 = hashlib.md5(data).hexdigest()

        try:
            os.rename(current_file, directory + tracklist[md5])
            print("[RENAME][DONE] " + current_file + " -> " + directory + tracklist[md5])
        except:
            print("[RENAME][ERROR] " + current_file + " -> " + directory + tracklist[md5])
            pass

# check and apply cover
with open(cover_file, "rb") as coverfile:
    data = coverfile.read()    
    md5 = hashlib.md5(data).hexdigest()

    if infos["cover"]["md5"] == md5:
        # iterate over files in that directory
        for filename in os.listdir(directory):
            current_file = os.path.join(directory, filename)

            if os.path.isfile(current_file) and current_file[len(current_file) - len(ext):] == ext:
                print("[COVER][DONE] " + current_file + " -> Fait.")

                music = music_tag.load_file(current_file)

                music["artwork"] = data

                music.save()
    else:
        print("Le MD5 de l'image fournie ne correspond pas !")

'''
# tags
for i in range(len(dir_list)):

    current_file = os.path.join(directory, dir_list[i])

    # checking if it is a file and if it has the correct extension
    if os.path.isfile(current_file) and current_file[len(current_file) - len(ext):] == ext:
        music = music_tag.load_file(current_file)
        music["album"] = infos["title"]
        print("[TAG][DONE] " + current_file + "#album -> " + infos["title"])

        music.save()
'''