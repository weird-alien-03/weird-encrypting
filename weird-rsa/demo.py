#demo.py

from keygen import generate_keys
from encrypt import encrypt
from decrypt import decrypt
from codec import cipher_to_string
from storage import save_keys, load_keys, save_cipher, load_cipher

def main():
    print("Weird Encrypting Demo")
    print("Modes: toy, user, text, file, system\n")

    mode = input("Choose your mode: ").strip().lower()

    text_seed = None
    file_path = None

    if mode == "text":
        text_seed=input("Enter seed text: ")

    elif mode == "file":
        file_path=input("Enter file path: ") 

    message =input("Enter your message: ")

    key_data = generate_keys(
        mode=mode,
        bits=16,
        text=text_seed,
        path=file_path
    )

    public_key = key_data["public_key"]
    private_key = key_data["private_key"]

    save_keys(public_key,private_key)

    
    
    cipher = encrypt(public_key,message)
    save_cipher(cipher, public_key)

    loaded_public, loaded_private = load_keys()
    loaded_cipher = load_cipher(loaded_public)

    _,n=loaded_public
    decrypted = decrypt(loaded_private, loaded_cipher)

    print("\nGenerated key data:")
    print("Public key:",loaded_public)
    print("Private key:",loaded_private)
    print("\nEncrypted:",cipher_to_string(loaded_cipher,n))
    print("Decrypted:",decrypted)

    if message==decrypted:
        print("\nRound-trip succesful.")
    else:
        print("\nRound-trip failed.")


if __name__=="__main__":
    main()
