# Write a python program for ECB, CBC, and CFB modes padding
def simple_aes_encrypt_block(block, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(block)])

def encrypt_ecb(plaintext, key):
    block_size = 16
    plaintext = plaintext + b'\x00' * (block_size - len(plaintext) % block_size)
    ciphertext = []
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        encrypted_block = simple_aes_encrypt_block(block, key)
        ciphertext.append(encrypted_block)
    return b''.join(ciphertext)

def encrypt_cbc(plaintext, key):
    block_size = 16
    iv = b'\x00' * block_size
    plaintext = plaintext + b'\x00' * (block_size - len(plaintext) % block_size)
    ciphertext = []
    previous_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        block = bytes([b ^ previous_block[i] for i, b in enumerate(block)])
        encrypted_block = simple_aes_encrypt_block(block, key)
        ciphertext.append(encrypted_block)
        previous_block = encrypted_block
    return iv + b''.join(ciphertext)

def encrypt_cfb(plaintext, key):
    block_size = 16
    iv = b'\x00' * block_size
    plaintext = plaintext + b'\x00' * (block_size - len(plaintext) % block_size)
    ciphertext = []
    previous_block = iv
    for i in range(0, len(plaintext), block_size):
        block = plaintext[i:i + block_size]
        encrypted_block = simple_aes_encrypt_block(previous_block, key)
        ciphertext_block = bytes([b ^ encrypted_block[i] for i, b in enumerate(block)])
        ciphertext.append(ciphertext_block)
        previous_block = ciphertext_block
    return iv + b''.join(ciphertext)

key = b'1234567890abcdef'
plaintext = b'This is a test message.'

print("ECB Encrypted:", encrypt_ecb(plaintext, key))
print("CBC Encrypted:", encrypt_cbc(plaintext, key))
print("CFB Encrypted:", encrypt_cfb(plaintext, key))