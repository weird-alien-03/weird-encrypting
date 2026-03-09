# Weird Encrypting

A small educational RSA-like encryptor written in Python.

This project is for learning how public-key style encryption works.
It is not intended for real-world secure communication.

## What this project does

This project currently:

- Generates a toy public/private key pair
- Encrypts text messages character by character
- Decrypts the encrypted output back into text
- Uses modular arithmetic, modular inverse, and fast modular exponentiation
- Includes a small demo script
- Includes a pytest test file

## Project goal

The goal of this project is to understand the mathematics and structure behind RSA-like encryption by building a simplified version from scratch.

This is a learning project, not production cryptography.

## Files

- `math_utils.py` — helper math functions like gcd, extended gcd, modular inverse, and modular exponentiation
- `keygen.py` — generates the toy public and private keys
- `encrypt.py` — encrypts plaintext into cipher data
- `decrypt.py` — decrypts cipher data back into plaintext
- `codec.py` — optional helper utilities for cipher formatting
- `demo.py` — runs the full encrypt/decrypt flow
- `tests/test_crypto.py` — basic pytest tests

## Requirements

Right now, the project only needs Python 3 to run.

Optional:
- `pytest` if you want to run tests

## How to run

Run the demo:

```
python3 demo.py

You will be asked to enter a message.

The script will then:

    Generate keys

    Encrypt the message

    Print the encrypted data

    Decrypt it back

    Print the recovered message
```

##Running tests

If you want to run tests later:
```
pip install pytest
pytest -q
```

##Notes

- This project is intentionally small and simplified
- The encryption is text-only for now
- It is designed for learning, experimentation, and understanding the math
- It should not be used for real secure data protection

##Future ideas
###Possible future improvements:
- Better key generation
- Save/load keys from files
- Save/load cipher from files
- Seed experiments from files or machine data
- Support for other data types later
- Better command-line interface
