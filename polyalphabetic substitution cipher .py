def polyalphabetic_cipher(plaintext, key):
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    return ''.join(chr((ord(p) - 65 + ord(k) - 65) % 26 + 65) for p, k in zip(plaintext.upper(), key.upper()))

# Example usage
plaintext = "HELLO"
key = "KEY"
ciphertext = polyalphabetic_cipher(plaintext, key)
print(ciphertext)

