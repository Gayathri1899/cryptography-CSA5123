def caesar_cipher(text, k):
    return ''.join(chr((ord(c) - 65 + k) % 26 + 65) if c.isupper() else 
                   chr((ord(c) - 97 + k) % 26 + 97) if c.islower() else c for c in text)

# Example usage
print(caesar_cipher("Hello, World!", 3))