#storage.py
#for storing data

import json
from utils.codec import cipher_to_string, string_to_cipher

def save_keys(public_key,private_key,filename="keys.json"):
    e,n1 = public_key
    d,n2 = private_key

    data = {
        "public_key": {
            "e":e,
            "n":n1
        },
        "private_key": {
            "d":d,
            "n":n2
        }
    }

    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def load_keys(filename="keys.json"):
    with open(filename,"r",encoding="utf-8") as f:
        data = json.load(f)

    public_key = (
        data["public_key"]["e"],
        data["public_key"]["n"]
    )
    private_key = (
        data["private_key"]["d"],
        data["private_key"]["n"]
    )

    return public_key, private_key

def save_cipher(cipher, public_key, filename="cipher.json"):
    _,n = public_key
    
    data = {
        "cipher_string":cipher_to_string(cipher,n)
    }

    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def load_cipher(public_key, filename="cipher.json"):
    _,n = public_key

    with open(filename,"r",encoding="utf-8") as f:
        data = json.load(f)

    return string_to_cipher(data["cipher_string"],n)
    
