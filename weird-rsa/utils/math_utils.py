#math_utils.py

#gcd or HCF as in maths
#using Euclid method
def gcd(a:int, b:int) -> int:
    while b!=0:
        a,b = b,a%b
    return abs(a)

#this one uses extended Euclid method
def extended_gcd(a:int, b:int) -> tuple[int,int,int]:
    if a == 0:
        return b,0,1

    g,x1,y1 = extended_gcd(b%a,a)
    x = y1 - (b//a)*x1
    y = x1
    return g,x,y

#mod inverse function
def mod_inverse(e: int, phi: int) -> int:
        return pow(e, -1, phi)

#mod power function
def mod_pow(base:int, exp:int, mod:int) -> int:
    return pow(base, exp, mod)
