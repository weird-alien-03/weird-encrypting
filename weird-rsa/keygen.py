#keygen.py

from math_utils import gcd, mod_inverse

def key_gen():
    p=37
    q=73

    n = p*q
    phi = (p-1)*(q-1)

    for e in range(2,phi):
        if gcd(e,phi)==1:
            break

    d = mod_inverse(e,phi)

    return (e,n),(d,n)


if __name__=="__main__":
    public_key,private_key = key_gen()
    print("Public key:", public_key)
    print("Private key:", private_key)
