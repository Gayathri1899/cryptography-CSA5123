#Write a python program for ciphertext has been generated with an affine cipher. The most frequent letter of the ciphertext is “B,” and the second most frequent letter of the ciphertext is “U.”Break this code.
from collections import Counter
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None
    result = ''
    for c in ciphertext:
        if c.isalpha():
            x = ord(c.upper()) - 65
            decrypted_char = chr(((a_inv * (x - b)) % 26) + 65)
            result += decrypted_char
        else:
            result += c
    return result

def break_affine(ciphertext):
    possible_a = [a for a in range(1, 26) if mod_inverse(a, 26) is not None]
    print("Trying all valid keys (a, b)...\n")
    for a in possible_a:
        for b in range(26):
            decrypted = affine_decrypt(ciphertext, a, b)
            print(f"a={a}, b={b} → {decrypted}")

# Example ciphertext (use uppercase letters only)
ciphertext = "YOURCIPHERTEXTHERE"  # Replace this
break_affine(ciphertext)
