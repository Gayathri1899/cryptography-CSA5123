# Write a PYTHON program for Playfair matrix encryption
def playfair_encrypt(message, matrix):
    def format_message(msg):
        msg = ''.join(filter(str.isalpha, msg)).upper().replace("J", "I")
        formatted = []
        i = 0
        while i < len(msg):
            a = msg[i]
            if i + 1 < len(msg):
                b = msg[i + 1]
                if a == b:
                    formatted.append(a + 'X')
                    i += 1
                else:
                    formatted.append(a + b)
                    i += 2
            else:
                formatted.append(a + 'X')
                i += 1
        return formatted

    def find_position(char):
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == char:
                    return r, c
        return None  # If not found (shouldn't happen with proper input)

    pairs = format_message(message)
    encrypted = []
    for pair in pairs:
        pos1 = find_position(pair[0])
        pos2 = find_position(pair[1])
        if pos1 is None or pos2 is None:
            raise ValueError(f"Character {pair[0]} or {pair[1]} not found in matrix.")
        r1, c1 = pos1
        r2, c2 = pos2
        if r1 == r2:
            encrypted.append(matrix[r1][(c1 + 1) % 5])
            encrypted.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            encrypted.append(matrix[(r1 + 1) % 5][c1])
            encrypted.append(matrix[(r2 + 1) % 5][c2])
        else:
            encrypted.append(matrix[r1][c2])
            encrypted.append(matrix[r2][c1])
    return ''.join(encrypted)

# 5x5 Playfair cipher matrix (excluding 'J')
matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

message = "Must see you over Cadogan West. Coming at once."
encrypted_message = playfair_encrypt(message, matrix)
print("Encrypted Message:", encrypted_message)