def encrypt(S: str, key: int) -> str:
	S = ''.join(ch for ch in S if ch.isalnum() or ch.isspace())
	S = ' '.join(S.split())

	rows = [''] * key
	currentRow = 0
	direction = 1

	for ch in S:
		rows[currentRow] += ch
		currentRow += direction
		if currentRow == 0 or currentRow == key - 1:
			direction *= -1

	cipherText = ''.join(rows)
	print(f"The Cipher Text is: {cipherText}")
	return cipherText
