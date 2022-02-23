import os
import json

DIR_PATH = "./cores/music/"
CORE_SETTINGS = json.load(open(DIR_PATH + 'settings.json', encoding="utf8"))

directory = CORE_SETTINGS["storage_path"]
dir_list = os.listdir(directory)

def refresh_artist_list():
    base = json.load(open(directory + "category_infos.json", encoding="utf8"))
    new_list = []

    # tags
    for i in range(len(dir_list)):
        current_item = os.path.join(directory, dir_list[i])

        if os.path.isdir(current_item):
            try:
                artist_infos = json.load(open(current_item + "/infos.json", encoding="utf8"))
                
                new_list.append({"name": artist_infos["name"], "slug": artist_infos["slug"]})

            except FileNotFoundError:
                print("Error : ", current_item)


    base["artists"] = new_list

    with open(directory + "category_infos.json", 'w', encoding='utf8') as json_file:
        json.dump(base, json_file, ensure_ascii=False, indent=4)