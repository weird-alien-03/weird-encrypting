#demo.py

from keygen import key_gen
from encrypt import encrypt
from decrypt import decrypt
from codec import cipher_to_string
from storage import save_keys, load_keys, save_cipher, load_cipher

def main():
    public_key,private_key=key_gen()
    message =input("Enter your message:")

    save_keys(public_key,private_key)

    cipher = encrypt(public_key,message)
    save_cipher(cipher, public_key)

    loaded_public, loaded_private = load_keys()
    loaded_cipher = load_cipher(loaded_public)

    _,n=loaded_public
    decrypted = decrypt(loaded_private, loaded_cipher)
    
    print("Public key:",loaded_public)
    print("Private key:",loaded_private)
    print("Encrypted:",cipher_to_string(loaded_cipher,n))
    print("Decrypted:",decrypted)

if __name__=="__main__":
    main()
