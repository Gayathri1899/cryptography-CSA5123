# Write a PYTHON program for PT-109 American patrol boat message in Playfair code
def playfair_decrypt(ciphertext, key):
    def create_matrix(key):
        key = key.upper().replace('J', 'I')
        seen = set()
        result = []
        # Include key letters
        for char in key:
            if char not in seen and char.isalpha():
                seen.add(char)
                result.append(char)
        # Fill in remaining letters of the alphabet
        for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if char not in seen:
                seen.add(char)
                result.append(char)
        # Create 5x5 matrix
        matrix = [result[i:i+5] for i in range(0, 25, 5)]
        return matrix

    def find_position(char, matrix):
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == char:
                    return i, j
        return None

    def decrypt_pair(a, b, matrix):
        pos_a = find_position(a, matrix)
        pos_b = find_position(b, matrix)
        if pos_a is None or pos_b is None:
            return a, b  # fallback, just return as is
        row_a, col_a = pos_a
        row_b, col_b = pos_b
        if row_a == row_b:
            return matrix[row_a][(col_a - 1) % 5], matrix[row_b][(col_b - 1) % 5]
        elif col_a == col_b:
            return matrix[(row_a - 1) % 5][col_a], matrix[(row_b - 1) % 5][col_b]
        else:
            return matrix[row_a][col_b], matrix[row_b][col_a]

    key = key.replace('J', 'I').upper()
    matrix = create_matrix(key)
    ciphertext = ciphertext.replace(' ', '').replace('J', 'I').upper()
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
        pa, pb = decrypt_pair(a, b, matrix)
        plaintext += pa + pb
    return plaintext

# Example usage
ciphertext = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
key = "PT109"
decrypted_message = playfair_decrypt(ciphertext, key)
print("Decrypted Message:\n", decrypted_message)