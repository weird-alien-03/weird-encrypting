# seed_utils.py
# this file is for generating the seed

import hashlib as hl
import secrets

def seed_from_text(text:str) -> bytes:
    return hl.sha256(text.encode("utf-8")).digest()

def seed_from_file(path:str) -> bytes:
    hasher = hl.sha256()
    with open(path,"rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.digest()

def seed_from_system(nbytes:int=32) -> bytes:
    return secrets.token_bytes(nbytes)
