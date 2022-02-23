import os
import json

settings = json.load(open('settings.json', encoding="utf8"))

ext = settings["ext"]
directory = "./" + settings["album"] + "/"

# iterate over files in that directory
dir_list = os.listdir(directory)

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

for i in range(len(dir_list)):
    current_file = os.path.join(directory, dir_list[i])

    if os.path.isfile(current_file) and current_file[len(current_file) - len(ext):] == ext:
        print(current_file)
        id = input("id >")

        os.rename(current_file, directory + alphabet[int(id) - 1] + " - " + current_file[len(directory):])
