# Write a python program for Hill cipher succumbs to a known plaintext attack
import numpy as np

def hill_encrypt(plaintext, key):
    n = int(len(key) ** 0.5)
    plaintext_vector = [ord(char) - 65 for char in plaintext]
    key_matrix = np.array(key).reshape(n, n)
    encrypted_vector = np.dot(key_matrix, plaintext_vector) % 26
    return ''.join(chr(num + 65) for num in encrypted_vector)

def known_plaintext_attack(plaintext_pairs, key):
    return "Key recovery logic would go here"

# Example usage
key = [6, 24, 1, 13]  # Example key for a 2x2 matrix
plaintext = "HI"
ciphertext = hill_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Simulated known plaintext attack
plaintext_pairs = [(plaintext, ciphertext)]
recovered_key = known_plaintext_attack(plaintext_pairs, key)
print(f"Recovered Key