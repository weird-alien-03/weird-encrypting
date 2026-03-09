#decrypt.py

from math_utils import mod_pow
from keygen import key_gen
from encrypt import encrypt
from codec import *

def decrypt(private_key, cipher:list):
    d,n = private_key
    decrypted_chars = []

    for c in cipher:
        m = mod_pow(c,d,n)
        
        decrypted_chars.append(chr(m))

    message="".join(decrypted_chars)

    return message

if __name__=="__main__":
    public_key,private_key=key_gen()
    e,n=public_key
    message=input("Enter your message:")
    cipher = encrypt(public_key,message)
    encrypted_str=cipher_to_string(cipher,n)
    decrypted = decrypt(private_key,cipher)
    
    print("Message:",message)
    print("Encrypted:",encrypted_str)
    print("Decrypted:",decrypted)
