# Write a python program for Encrypt and decrypt in cipher block chaining mode using S-DES
def xor(a, b):
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

def p10(key):
    p10_table = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    return ''.join(key[i] for i in p10_table)

def p8(key):
    p8_table = [5, 2, 6, 3, 7, 4, 9, 8]
    return ''.join(key[i] for i in p8_table)

def left_shift(key):
    return key[1:] + key[0]

def generate_keys(key):
    key = p10(key)
    left, right = key[:5], key[5:]
    left, right = left_shift(left), left_shift(right)
    K1 = p8(left + right)
    left, right = left_shift(left), left_shift(right)
    left, right = left_shift(left), left_shift(right)
    K2 = p8(left + right)
    return K1, K2

S0 = [
    ['1', '0', '3', '2'],
    ['3', '2', '1', '0'],
    ['0', '1', '2', '3'],
    ['3', '0', '1', '2']
]

S1 = [
    ['0', '1', '2', '3'],
    ['3', '0', '1', '2'],
    ['3', '2', '1', '0'],
    ['2', '3', '0', '1']
]

def sbox(s, sbox_table):
    row = int(s[0] + s[3], 2)
    col = int(s[1] + s[2], 2)
    return bin(int(sbox_table[row][col], 10))[2:].zfill(2)

def f(block, key):
    left, right = block[:4], block[4:]
    expanded_right = right[1] + right[2] + right[3] + right[0]
    xor_result = xor(expanded_right, key)
    left_s, right_s = xor_result[:4], xor_result[4:]
    left_s = sbox(left_s, S0)
    right_s = sbox(right_s, S1)
    return left_s + right_s

def encrypt(block, key):
    K1, K2 = generate_keys(key)
    block = p10(block)
    left, right = block[:4], block[4:]
    temp = f(left + right, K1)
    left, right = xor(temp[:4], left), xor(temp[4:], right)
    left, right = right, left
    temp = f(left + right, K2)
    left, right = xor(temp[:4], left), xor(temp[4:], right)
    block = p8(left + right)
    return block

def decrypt(block, key):
    K1, K2 = generate_keys(key)
    K1, K2 = K2, K1
    block = p10(block)
    left, right = block[:4], block[4:]
    temp = f(left + right, K1)
    left, right = xor(temp[:4], left), xor(temp[4:], right)
    left, right = right, left
    temp = f(left + right, K2)
    left, right = xor(temp[:4], left), xor(temp[4:], right)
    block = p8(left + right)
    return block

def cbc_encrypt(plaintext, key, iv):
    ciphertext = iv
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        block = xor(block, ciphertext[-8:])
        ciphertext += encrypt(block, key)
    return ciphertext[8:]

def cbc_decrypt(ciphertext, key, iv):
    decrypted = iv
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        decrypted_block = decrypt(block, key)
        decrypted += xor(decrypted_block, ciphertext[i-8:i])
    return decrypted[8:]

iv = '10101010'
key = '01111111101'
plaintext = '0000000100100011'

if len(plaintext) % 8 != 0:
    plaintext = plaintext.ljust(len(plaintext) + (8 - len(plaintext) % 8), '0')

ciphertext = cbc_encrypt(plaintext, key, iv)
decrypted_text = cbc_decrypt(ciphertext, key, iv)

print(f'Ciphertext: {ciphertext}')
print(f'Decrypted: {decrypted_text}')