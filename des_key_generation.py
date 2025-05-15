# Write a python program for DES algorithm for decryption
def xor_encrypt_decrypt(data, key):
    return bytes([byte ^ key for byte in data])

if __name__ == "__main__":
    plaintext = "hello world"
    plaintext_bytes = plaintext.encode()
    key = 123
    encrypted = xor_encrypt_decrypt(plaintext_bytes, key)
    print("Encrypted:", encrypted)
    decrypted = xor_encrypt_decrypt(encrypted, key)
    print("Decrypted:", decrypted.decode())