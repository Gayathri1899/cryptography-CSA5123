# Write a C program for one-time pad version of the Vigenère cipher
def encrypt(plaintext, key):
    return ''.join(chr((ord(p) - 97 + k) % 26 + 97) for p, k in zip(plaintext, key))

def decrypt(ciphertext, key):
    return ''.join(chr((ord(c) - 97 - k) % 26 + 97) for c, k in zip(ciphertext, key))

# Part (a)
plaintext_a = "sendmorenmoney"
key_a = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]
ciphertext_a = encrypt(plaintext_a, key_a)

# Part (b)
ciphertext_b = ciphertext_a
plaintext_b = "cashnotneeded"
key_b = [(ord(c) - ord(p)) % 26 for c, p in zip(ciphertext_b, plaintext_b)]
decrypted_b = decrypt(ciphertext_b, key_b)

# Output
print("Ciphertext A:", ciphertext_a)
print("Derived Key B:", key_b)
print("Decrypted B:", decrypted_b)