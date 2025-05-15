# Write a python program to Encrypt the message using the Hill cipher
import numpy as np

def mod26(x):
    return x % 26

def encrypt(message, key):
    message = message.replace(" ", "").lower()
    n = len(key)
    padded_length = n * ((len(message) + n - 1) // n)
    message += 'x' * (padded_length - len(message))
    message_matrix = np.array([ord(c) - ord('a') for c in message]).reshape(-1, n)
    encrypted_matrix = (message_matrix @ key) % 26
    return ''.join(chr(num + ord('a')) for num in encrypted_matrix.flatten())

def decrypt(ciphertext, key):
    key_inv = np.linalg.inv(key) * np.linalg.det(key)
    key_inv = np.round(key_inv).astype(int) % 26
    ciphertext_matrix = np.array([ord(c) - ord('a') for c in ciphertext]).reshape(-1, key.shape[0])
    decrypted_matrix = (ciphertext_matrix @ key_inv) % 26
    return ''.join(chr(num + ord('a')) for num in decrypted_matrix.flatten())

key = np.array([[9, 4], [5, 7]])
message = "meet me at the usual place at ten rather than eight oclock"
ciphertext = encrypt(message, key)
decrypted_message = decrypt(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)