# Write a python program for DES the first 24 bits of each subkey
def generate_subkeys(key):
    key = [int(b) for b in format(key, '028b')]
    subkeys = []
    for i in range(16):
        subkey = key[:24] + key[28:][i % 4 * 6:(i % 4 + 1) * 6]
        subkeys.append(int(''.join(map(str, subkey)), 2))
    return subkeys

initial_key = 0b1010101010101010101010101010  # Example 28-bit key
subkeys = generate_subkeys(initial_key)
print(subkeys)