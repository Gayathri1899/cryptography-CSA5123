# Write a python program for Encrypt and decrypt in counter mode using S-DES
def sdes_encrypt(plaintext, key):
    return encrypted_text

def sdes_decrypt(ciphertext, key):
    return decrypted_text

def counter_mode_encrypt(plaintext, key, counter):
    ciphertext = []
    for i in range(len(plaintext)):
        keystream = sdes_encrypt(counter + i, key)
        ciphertext.append(plaintext[i] ^ keystream)
    return ciphertext

def counter_mode_decrypt(ciphertext, key, counter):
    plaintext = []
    for i in range(len(ciphertext)):
        keystream = sdes_encrypt(counter + i, key)
        plaintext.append(ciphertext[i] ^ keystream)
    return plaintext

plaintext = [0b00000001, 0b00000010, 0b00000100]
key = 0b0111111101
counter = 0b00000000

ciphertext = counter_mode_encrypt(plaintext, key, counter)
print("Ciphertext:", ciphertext)

decrypted_text = counter_mode_decrypt(ciphertext, key, counter)
print("Decrypted Text:", decrypted_text)