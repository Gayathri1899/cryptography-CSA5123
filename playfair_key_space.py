# Write a python program for possible keys does the Playfair cipher have?
import math

def total_playfair_keys():
    letters = 25
    total_keys = math.factorial(letters) // (math.factorial(5) ** 5)
    return total_keys

def unique_playfair_keys():
    unique_keys = total_playfair_keys() // 2  # Simplified assumption
    return unique_keys

total_keys = total_playfair_keys()
unique_keys = unique_playfair_keys()

print(f"Total possible keys (approx. power of 2): {math.log2(total_keys):.2f}")
print(f"Effectively unique keys (approx. power of 2): {math.log2(unique_keys):.2f}")