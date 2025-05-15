# Write a python program that can perform a letter frequency attack on any monoalphabetic substitution cipher
import string
from collections import Counter

def frequency_analysis(ciphertext):
    freq_order = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
    letter_count = Counter(filter(str.isalpha, ciphertext.upper()))
    total_letters = sum(letter_count.values())
    freq = {char: count / total_letters for char, count in letter_count.items()}
    return sorted(freq, key=lambda x: freq_order.index(x) if x in freq_order else len(freq_order))

def substitute(ciphertext, key):
    return ''.join(key.get(c, c) for c in ciphertext)

def letter_frequency_attack(ciphertext, top_n=10):
    freq_order = frequency_analysis(ciphertext)
    possible_plaintexts = []
    for i in range(len(freq_order)):
        key = {freq_order[j]: string.ascii_uppercase[j] for j in range(len(freq_order))}
        possible_plaintexts.append(substitute(ciphertext, key))
    return possible_plaintexts[:top_n]

ciphertext = "GSRH RH Z HVXIVG"
top_plaintexts = letter_frequency_attack(ciphertext, 10)
for i, text in enumerate(top_plaintexts, 1):
    print(f"{i}: {text}")