# Write a python program for ECB mode and CBC mode error propagation
def xor(block1, block2):
    return bytes([b1 ^ b2 for b1, b2 in zip(block1, block2)])

def decrypt_block(block, key):
    return block[::-1]

def ecb_decrypt(ciphertext, key):
    return [decrypt_block(block, key) for block in ciphertext]

def cbc_decrypt(ciphertext, key, iv):
    plaintext = []
    previous_block = iv
    for block in ciphertext:
        decrypted_block = decrypt_block(block, key)
        plaintext_block = xor(decrypted_block, previous_block)
        plaintext.append(plaintext_block)
        previous_block = block
    return plaintext

def analyze_error_propagation():
    print("In CBC mode, an error in C1 affects P1 and P2, but no blocks beyond P2.")
    print("In CBC mode, a bit error in P1 propagates through C1 and affects only the decryption of P1.")

if __name__ == "__main__":
    ciphertext_ecb = [b'block1', b'block2', b'block3']
    ciphertext_cbc = [b'block1', b'block2', b'block3']
    iv = b'ivblock'
    key = b'secretkey'

    decrypted_ecb = ecb_decrypt(ciphertext_ecb, key)
    print(f"ECB Decrypted: {decrypted_ecb}")

    decrypted_cbc = cbc_decrypt(ciphertext_cbc, key, iv)
    print(f"CBC Decrypted: {decrypted_cbc}")

    analyze_error_propagation()