# Write a python program for set of blocks encoded with the RSA algorithm
from math import gcd

def rsa_common_factor(n, e, block):
    common_factor = gcd(n, block)
    if common_factor > 1:
        print(f"Common factor found: {common_factor}")
        return common_factor
    else:
        print("No common factor found.")
        return None

n = 55
e = 3
block = 15
rsa_common_factor(n, e, block)