#codec.py
def cipher_to_string(cipher: list[int], n: int) -> str:
    width = len(str(n - 1))
    return "".join(str(x).zfill(width) for x in cipher)


def string_to_cipher(s: str, n: int) -> list[int]:
    width = len(str(n - 1))

    if len(s) % width != 0:
        raise ValueError("Invalid cipher string length")

    return [int(s[i:i+width]) for i in range(0, len(s), width)]
