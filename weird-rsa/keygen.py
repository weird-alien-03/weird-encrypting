#keygen.py

from math_utils import gcd, mod_inverse
import seed_utils as su
import prime_utils as pu

def choose_e(phi:int) -> int:
    e = 65537
    if gcd(e,phi)==1:
        return e

    e = 3
    while e < phi:
        if gcd(e,phi)==1:
            return e
        e+=2

    raise ValueError("Could not find valid e")

def generate_toy_primes():
    return 61,53

def generate_user_input_toy_primes():
    p = int(input("Enter toy prime p:"))
    q = int(input("Enter toy prime q:"))

    if p == q:
        raise ValueError("p and q must be distinct")

    if not pu.is_probable_prime(p) or not pu.is_probable_prime(q):
        raise ValueError("p and q must be primes")

    return p,q

def seeded_primes_from_text(text:str,bits:int):
    seed = su.seed_from_text(text)
    p = pu.next_prime_from_seed(seed, bits)
    q_seed = pu.derive_second_seed(seed, b"q")
    q = pu.next_prime_from_seed(q_seed,bits)

    while q==p:
        q_seed = pu.derive_second_seed(q_seed,b"retry")
        q = pu.next_prime_from_seed(q_seed,bits)

    return p,q

def seeded_primes_from_file(path:str,bits:int):
    seed = su.seed_from_file(path)
    p = pu.next_prime_from_seed(seed, bits)
    q_seed = pu.derive_second_seed(seed, b"q")
    q = pu.next_prime_from_seed(q_seed,bits)
    
    while q==p:
        q_seed = pu.derive_second_seed(q_seed,b"retry")
        q = pu.next_prime_from_seed(q_seed,bits)

    return p,q

def seeded_primes_from_system(bits:int):
    seed = su.seed_from_system()
    p = pu.next_prime_from_seed(seed, bits)
    q_seed = pu.derive_second_seed(seed, b"q")
    q = pu.next_prime_from_seed(q_seed,bits)
    
    while q==p:
        q_seed = pu.derive_second_seed(q_seed,b"retry")
        q = pu.next_prime_from_seed(q_seed,bits)

    return p,q

def generate_keys(mode:str="system", bits:int=16, text:str=None, path:str=None):
    if mode == "toy":
        p,q = generate_toy_primes()

    elif mode == "user":
        p,q = generate_user_input_toy_primes()

    elif mode == "file":
        p,q = seeded_primes_from_file(path, bits)

    elif mode == "text":
        p,q = seeded_primes_from_text(text,bits)

    elif mode == "system":
        p,q = seeded_primes_from_system(bits)

    else:
        raise ValueError("Unknown mode")
        return "Modes avaliable are:\ntoy,user,file,text,default=system"

    n = p*q
    phi = (p-1)*(q-1)
    e = choose_e(phi)
    d = mod_inverse(e,phi)

    public_key = (e,n)
    private_key = (d,n)

    return {
        "p":p,
        "q":q,
        "n":n,
        "phi":phi,
        "e":e,
        "d":d,
        "public_key":public_key,
        "private_key":private_key
    } 
