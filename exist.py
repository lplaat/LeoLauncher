import hashlib
from os.path import exists

#checks the hash of the file
def check(path, hash):
    if exists(path):
        with open(path, 'rb') as f:
            sha1 = hashlib.sha1()

            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                sha1.update(chunk)

        return sha1.hexdigest() == hash
    else:
        return False
