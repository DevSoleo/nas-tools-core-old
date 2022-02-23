import unicodedata
import re
import math

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
      
def clean_file_name(name, replace_space_with=None):
    # remove : /, \, ?, %, *, :, |, ", <, >
    name = ''.join(ch for ch in name if unicodedata.category(ch)[0] != 'C')

    cleaned_name = re.sub(r'[/\\?%*:|"<>]', '', name).strip().replace("’", "'")
    
    if replace_space_with is not None:
        return cleaned_name.replace(' ', replace_space_with)
    
    return cleaned_name

def clean_display_name(name):
    return name.replace("’", "'")

def extend_int(number):
    result = number

    if result <= 9: result = "0" + str(number)

    return result