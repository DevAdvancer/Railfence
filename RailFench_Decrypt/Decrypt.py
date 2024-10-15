def decrypt(S: str, key: int) -> str:
    rowLengths = [0] * key
    currentRow = 0
    direction = 1

    for _ in S:
        rowLengths[currentRow] += 1
        currentRow += direction
        if currentRow == 0 or currentRow == key - 1:
            direction *= -1

    rows = []
    index = 0
    for length in rowLengths:
        rows.append(S[index:index + length])
        index += length

    plainText = ''
    currentRow = 0
    direction = 1

    while any(rows):
        if rows[currentRow]:
            plainText += rows[currentRow][0]
            rows[currentRow] = rows[currentRow][1:]
        currentRow += direction
        if currentRow == 0 or currentRow == key - 1:
            direction *= -1

    decrypted_text_with_spaces = plainText.replace('', '').strip()
    print(f"The Plain Text is: {decrypted_text_with_spaces}")
    return decrypted_text_with_spaces
