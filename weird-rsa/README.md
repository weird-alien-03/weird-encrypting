# Weird RSA-like

A small educational RSA-like encryptor written in Python.

This project was built to understand how public-key style encryption works from the ground up, including key generation, modular arithmetic, seeded prime generation, encryption, and decryption.

It is a learning project and **not** intended for real-world secure communication.

## Project overview

Weird Encrypting is a simplified RSA-style project made for learning the mathematical and structural ideas behind public-key cryptography.

The project currently supports:
- Toy key generation with fixed small primes
- Manual toy-prime input mode
- Text-based seed mode for prime generation
- File-based seed mode for prime generation
- System-random seed mode using Python's `secrets` module
- Encryption of text messages
- Decryption back into plaintext
- Save/load support for keys and cipher data
- Demo script for full round-trip testing
- Pytest test suite

## How it works

The project follows an RSA-like flow:

1. Generate two primes `p` and `q`
2. Compute `n = p * q`
3. Compute `phi = (p - 1) * (q - 1)`
4. Choose a valid public exponent `e`
5. Compute the private exponent `d`
6. Encrypt with the public key
7. Decrypt with the private key

For the seeded modes, the project does not treat text or files directly as primes. Instead, it:
- turns the input into seed bytes,
- converts those bytes into prime candidates,
- and searches upward until probable primes are found.

## Modes

The demo currently supports these modes:

- `toy` — uses fixed small primes for debugging and learning
- `user` — lets the user manually enter small toy primes
- `text` — uses typed text as the deterministic seed
- `file` — uses file contents as the deterministic seed
- `system` — uses secure random bytes from Python's `secrets` module

## Files

- `math_utils.py` — gcd, modular inverse, modular exponentiation helpers
- `seed_utils.py` — seed generation from text, files, and system randomness
- `prime_utils.py` — candidate generation and Miller–Rabin probable-prime testing
- `keygen.py` — key generation for all supported modes
- `encrypt.py` — encrypts plaintext into cipher data
- `decrypt.py` — decrypts cipher data back into plaintext
- `codec.py` — helper formatting for cipher output
- `storage.py` — save/load helpers for keys and cipher data
- `demo.py` — full interactive demo flow
- `tests/` — pytest test suite
- `pytest.ini` — pytest import-path configuration

## Requirements

- Python 3
- `pytest` for running tests

## Run the demo

From inside the project folder:

```bash
python3 demo.py
```

You will be prompted to:

- choose a mode,
- optionally enter seed text or a file path,
- enter a message to encrypt.

The demo then:

- generates keys,
- encrypts the message,
- saves and reloads key/cipher data,
- decrypts the message,
- and checks whether the round trip succeeded.

## Run tests

Install pytest if needed:

```bash
pip install pytest
```

Run the tests:

```bash
pytest -q
```

## Notes

- This project is intentionally simplified.
- It is designed for learning, experimentation, and understanding the math behind RSA-like encryption.
- Seeded prime generation here is educational, not a substitute for production cryptographic key generation.
- The system mode uses Python's secrets module, which draws secure random bytes from the operating system.
- This project should not be used for real secure communication or production cryptographic systems.

## Why I built this

I built this project to understand:
- modular arithmetic in practice,
- modular inverse and modular exponentiation in practice
- how Python's built-in pow() can simplify modular arithmetic implementations
- probable-prime testing using Miller-Rabin method,
- RSA-like key generation,
- and the difference between educational cryptography and real-world secure cryptographic systems.

## Possible next steps

- Improve command-line structure
- Extend it to experiment with file encryption for formats such as images or WAV files.
- Add cleaner key/cipher file formats
- Add stronger validation and error handling
- Compare this educational version with real cryptographic libraries
