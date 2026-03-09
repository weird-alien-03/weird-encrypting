#demo.py

from keygen import key_gen
from encrypt import encrypt
from decrypt import decrypt
from codec import *

def main():
    public_key,private_key=key_gen()
    e,n=public_key
    message =input("Enter your message:")

    cipher = encrypt(public_key,message)
    encrypted = cipher_to_string(cipher,n)
    decrypted = decrypt(private_key,cipher)

    print("Public key:",public_key)
    print("Private key:",private_key)
    print("Message:",message)
    print("Encrypted:",encrypted)
    print("Decrypted:",decrypted)

if __name__=="__main__":
    main()
