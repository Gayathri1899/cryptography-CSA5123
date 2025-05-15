def affine_cipher(p, a, b):
    if a % 2 == 0 or a % 13 == 0:  # a must be coprime to 26
        raise ValueError("Invalid value for a. Must be coprime to 26.")
    return (a * p + b) % 26
# Limitations
def allowed_values():
    return [a for a in range(1, 26) if gcd(a, 26) == 1]
from math import gcd
# Example usage
plaintext = 0  # 'A'
a, b = 5, 8
ciphertext = affine_cipher(plaintext, a, b)
print(f"Ciphertext: {ciphertext}")  # Output for 'A' with a=5, b=8
print(f"Allowed values for a: {allowed_values()}")
