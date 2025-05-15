def create_matrix(keyword):
    matrix = []
    seen = set()
    for char in keyword.upper().replace("J", "I"):
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    raise ValueError(f"Character {char} not found in matrix")

def encrypt_pair(a, b, matrix):
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]

def playfair_encrypt(plaintext, keyword):
    matrix = create_matrix(keyword)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    
    # Prepare pairs
    i = 0
    pairs = []
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    # Encrypt pairs
    ciphertext = ''.join(encrypt_pair(a, b, matrix) for a, b in pairs)
    return ciphertext

# Example usage
keyword = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, keyword)
print("Ciphertext:", ciphertext)
