from RailFench_Decrypt import decrypt
from RailFench_Encrypt import encrypt


def main():
	process = input("Would you like to encrypt or decrypt: ").lower()
	key = int(input("Enter the key: "))

	operations = {
		"encrypt": lambda: encrypt(input("Enter your Plain Text Message: ").lower(), key),
		"decrypt": lambda: decrypt(input("Enter your Cipher Text Message: ").lower(), key)
	}

	operation = operations.get(process)

	if operation:
		operation()
	else:
		print("Invalid option! Please choose either 'encrypt' or 'decrypt'.")


if __name__ == '__main__':
	main()
