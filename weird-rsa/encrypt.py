#encrypt.py

from math_utils import mod_pow
from keygen import key_gen
from codec import cipher_to_string

def encrypt(public_key,plaintext:str):
    e,n = public_key
    cipher = []

    for ch in plaintext:
        m = ord(ch)
        if m>=n:
            raise ValueError("Character code must be smaller than n")
        c = mod_pow(m,e,n)
        cipher.append(c)

    return cipher

if __name__=="__main__":
    public_key,private_key=key_gen()
    e,n=public_key
    message=input("Enter message:")
    cipher = encrypt(public_key,message)
    encrypted_str=cipher_to_string(cipher,n)
    print("Message:",message)
    print("Encrypted:",encrypted_str)
