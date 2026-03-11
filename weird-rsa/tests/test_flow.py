# tests/test_flow.py

from receiver.keygen import generate_keys
from sender.encrypt import encrypt
from receiver.decrypt import decrypt


def test_toy_mode_round_trip():
    message = "hello"
    data = generate_keys(mode="toy", bits=16)

    cipher = encrypt(data["public_key"], message)
    recovered = decrypt(data["private_key"], cipher)

    assert recovered == message


def test_text_mode_round_trip():
    message = "physics"
    data = generate_keys(mode="text", bits=16, text="quantum")

    cipher = encrypt(data["public_key"], message)
    recovered = decrypt(data["private_key"], cipher)

    assert recovered == message


def test_file_mode_round_trip(tmp_path):
    seed_file = tmp_path / "seed.txt"
    seed_file.write_text("file based seed")

    message = "cryptography"
    data = generate_keys(mode="file", bits=16, path=str(seed_file))

    cipher = encrypt(data["public_key"], message)
    recovered = decrypt(data["private_key"], cipher)

    assert recovered == message


def test_system_mode_round_trip():
    message = "entropy"
    data = generate_keys(mode="system", bits=16)

    cipher = encrypt(data["public_key"], message)
    recovered = decrypt(data["private_key"], cipher)

    assert recovered == message
