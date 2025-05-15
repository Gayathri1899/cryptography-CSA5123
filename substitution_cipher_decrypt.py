# Write a C program for the following ciphertext was generated using a simple substitution algorithm
from collections import Counter

# Ciphertext: likely from Poe's "The Gold-Bug"
ciphertext = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83 (88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*---4)8¶8* ;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81 (‡9;48;(88;4(‡?34;48)4‡;161;:188;‡? "

# Step 1: Frequency analysis
frequency = Counter(ciphertext)
common_chars = frequency.most_common()
print("=== Character Frequencies ===")
for char, freq in common_chars:
    print(f"{repr(char)}: {freq}")

# Step 2: Initial substitution map (you can update this as you make better guesses)
substitution_map = {
    '‡': 'e',
    '†': 't',
    '5': 'h',
    '8': 'o',
    '4': 'n',
    '3': 'a',
    '0': 'd',
    '6': 'r',
    ')': ' ',
    '*': 's',
    ';': 'i',
    '.': 'l',
    ':': 'c',
    '(': 'm',
    '9': 'u',
    '1': 'y',
    '?': 'g',
    '2': 'f',
    '¶': 'b',
    '---': 'w',
    ']': 'p'
}

# Step 3: Decrypt message using the substitution map
decrypted_message = ''.join(substitution_map.get(char, char) for char in ciphertext)
print("\n=== Decrypted Output ===")
print(decrypted_message)