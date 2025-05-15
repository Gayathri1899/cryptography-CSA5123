# Write a python program for monoalphabetic cipher is that both sender and receiver must commit the permuted cipher sequence to memory
def monoalphabetic_cipher(keyword):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keyword_unique = ''.join(sorted(set(keyword), key=keyword.index))
    cipher = keyword_unique + ''.join(c for c in alphabet if c not in keyword_unique)
    return dict(zip(alphabet, cipher))

cipher_mapping = monoalphabetic_cipher("CIPHER")
print(cipher_mapping)