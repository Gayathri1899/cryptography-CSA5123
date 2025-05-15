# Write a python program that can perform a letter frequency attack on an additive cipher
from collections import Counter
import string

def frequency_analysis(ciphertext, top_n=10):
    freq = Counter(ciphertext)
    most_common = freq.most_common()
    return most_common

def decrypt(ciphertext, shift):
    decrypted = ''.join(
        chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else
        chr((ord(char) - shift - 97) % 26 + 97) if char.islower() else char
        for char in ciphertext
    )
    return decrypted

def letter_frequency_attack(ciphertext, top_n=10):
    possible_plaintexts = []
    for shift in range(26):
        possible_plaintexts.append(decrypt(ciphertext, shift))
    return sorted(possible_plaintexts, key=lambda x: frequency_analysis(x), reverse=True)[:top_n]

ciphertext = "Wklv lv d whvw phvvdjh"
top_plaintexts = letter_frequency_attack(ciphertext, 10)
print(top_plaintexts)