import hashlib

def get_hash(current_file, method="md5"):
    with open(current_file, "rb") as file_to_check:
        data = file_to_check.read()    
        
        if method == "sha1":
            hash = hashlib.sha1(data).hexdigest()
        else:
            hash = hashlib.md5(data).hexdigest()
            
    return hash