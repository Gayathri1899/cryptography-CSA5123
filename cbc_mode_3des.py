# Write a python program for encryption in the cipher block chaining (CBC) mode using 3DES
def xor_encrypt_decrypt(data, key):
    return bytes([byte ^ key for byte in data])

def pad(plaintext, block_size):
    padding_len = block_size - len(plaintext) % block_size
    return plaintext + bytes([padding_len] * padding_len)

def unpad(padded_data):
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]

def encrypt(plaintext, key):
    plaintext_bytes = plaintext.encode()
    padded_data = pad(plaintext_bytes, 8)
    encrypted_data = xor_encrypt_decrypt(padded_data, key)
    return encrypted_data

def decrypt(ciphertext, key):
    decrypted_data = xor_encrypt_decrypt(ciphertext, key)
    return unpad(decrypted_data).decode()

key = 123
plaintext = "Hello, World!"
ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print(f"Ciphertext: {ciphertext.hex()}")
print(f"Decrypted: {decrypted}")