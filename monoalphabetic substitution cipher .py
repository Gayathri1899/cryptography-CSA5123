import random
import string
def generate_cipher():
    alphabet = string.ascii_lowercase
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))
def encrypt(plaintext, cipher):
    return ''.join(cipher.get(char, char) for char in plaintext.lower())
cipher = generate_cipher()
plaintext = "hello world"
ciphertext = encrypt(plaintext, cipher)
print("Cipher:", cipher)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
