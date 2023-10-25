def encode(password):
	encoded = ""
	for num in password:
		num = int(num)
		encoded += str((num + 3) % 10)
	return encoded


def decode(encoded):
	decoded = ""
	for num in encoded:
		num = int(num)
		if num - 3 < 0:
			num += 10
		decoded += str(num - 3)
	return decoded


def main():
	encoded = None

	while True:
		print("Menu")
		print("-" * 13)
		print("1. Encode")
		print("2. Decode")
		print("3. Quit")
		print()

		menu_selection = int(input("Please enter an option: "))
		if menu_selection == 1:
			password = input("Please enter your password to encode: ")
			encoded = encode(password)

		elif menu_selection == 2:
			decoded = decode(encoded)
			print("The encoded password is " + encoded + " and the original password is " + decoded + ".")

		elif menu_selection == 3:
			break


if __name__ == "__main__":
	main()
