import os
import json
import hashlib

import core.file_reader

settings = json.load(open("./core/settings.json", encoding="utf8"))
directory = "./" + settings["album"] + "/"

def list_folder(directory):
    # listing all files from the given directory
    dir_list = os.listdir(directory)
    dir_list.sort()

    return dir_list

def list_by_ext(directory, ext):
    result = []
    
    dir_list = list_folder(directory)

    # iterate over files in that directory
    for i in range(len(dir_list)):
        current_file = os.path.join(directory, dir_list[i])

        if os.path.isfile(current_file) and current_file[len(current_file) - len(ext):] == ext:
            result.append(current_file)

    return result

def hash_file_list(file_list, method="md5"):
    result = []

    for i in range(len(file_list)):
        result.append(file_reader.get_hash(file_list[i], method))

    return result