# prime_utils.py
# "Autobots Roll Out!" 
# miller-rabin as the prime test

import hashlib as hl
import secrets

SMALL_PRIMES=[
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97
]

def bytes_to_candidate(seed:bytes,bits:int=16) -> int:
    if bits < 2:
        raise ValueError("bits must be at least 2")
    
    value = int.from_bytes(seed,"big")
    mask = (1 << bits) - 1
    value = value & mask
    value |= (1 << (bits - 1))
    value |= 1
    return value

def is_probable_prime(n:int,rounds:int=20) -> bool:
    if n<2:
        return False

    for p in SMALL_PRIMES:
        if n==p:
            return True
        if n%p == 0:
            return False

    d = n-1
    s = 0
    while d%2 == 0:
        d //= 2
        s += 1

    for _ in range(rounds):
        a = secrets.randbelow(n-3) + 2
        x = pow(a,d,n)

        if x == 1 or x == n-1:
            continue

        for _ in range(s-1):
            x = pow(x,2,n)
            if x == n-1:
                break
        else:
            return False
    return True

def next_prime_from_seed(seed:bytes, bits:int=16) -> int:
    candidate = bytes_to_candidate(seed,bits)

    while not is_probable_prime(candidate):
        candidate += 2

    return candidate

def derive_second_seed(seed:bytes, label:bytes=b"q") -> bytes:
    return hl.sha256(seed+label).digest()
