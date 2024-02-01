import os

def get_positive_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def caesar_cipher(text, s, encrypt=True):
    result = ""

    for char in text:
        if char.isalpha():
            shift = s if encrypt else -s

            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

def caesar_cipher_extended(text, s, encrypt=True):
    result = ""

    for char in text:
        if 32 <= ord(char) <= 126:
            shift = s if encrypt else -s
            result += chr((ord(char) + shift - 32) % 95 + 32)
        else:
            result += char

    return result

def encrypt_from_file(input_filename, output_filename, shifts):
    try:
        # Check if input file exists
        with open(input_filename, 'r') as input_file:
            text = input_file.read()

        # Encrypt the text
        encrypted_text = caesar_cipher(text, shifts, encrypt=True)

        # Check if output file exists, create if missing
        try:
            with open(output_filename, 'x') as output_file:
                output_file.write(encrypted_text)
        except FileExistsError:
            # Output file already exists, append to it
            with open(output_filename, 'a') as output_file:
                output_file.write(f"\n{encrypted_text}")

        print(f"Encryption successful. Result written to {output_filename}")
    except FileNotFoundError:
        # Input file not found, create with default text
        with open(input_filename, 'w') as input_file:
            input_file.write("Hello World!")

        # Encrypt the default text
        encrypted_text = caesar_cipher("Hello World!", shifts, encrypt=True)

        # Check if output file exists, create if missing
        try:
            with open(output_filename, 'x') as output_file:
                output_file.write(encrypted_text)
        except FileExistsError:
            # Output file already exists, append to it
            with open(output_filename, 'a') as output_file:
                output_file.write(f"\n{encrypted_text}")

        print(f"Input file '{input_filename}' not found. Created with default text. "
              f"Encryption result written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_from_file(input_filename, output_filename, shifts):
    try:
        # Check if input file exists
        with open(input_filename, 'r') as input_file:
            text = input_file.read()

        # Decrypt the text
        decrypted_text = caesar_cipher(text, shifts, encrypt=False)

        # Check if output file exists, create if missing
        try:
            with open(output_filename, 'x') as output_file:
                output_file.write(decrypted_text)
        except FileExistsError:
            # Output file already exists, append to it
            with open(output_filename, 'a') as output_file:
                output_file.write(f"\n{decrypted_text}")

        print(f"Decryption successful. Result written to {output_filename}")
    except FileNotFoundError:
        # Input file not found, create with default text
        with open(input_filename, 'w') as input_file:
            input_file.write("Khoor Zruog!")

        # Decrypt the default text
        decrypted_text = caesar_cipher("Khoor Zruog!", shifts, encrypt=False)

        # Check if output file exists, create if missing
        try:
            with open(output_filename, 'x') as output_file:
                output_file.write(decrypted_text)
        except FileExistsError:
            # Output file already exists, append to it
            with open(output_filename, 'a') as output_file:
                output_file.write(f"\n{decrypted_text}")

        print(f"Input file '{input_filename}' not found. Created with default text. "
              f"Decryption result written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def encrypt_from_specific_file(output_filename, shifts):
    try:
        file_path = input("Enter the file path to encrypt: ")

        # Validate file path
        while not os.path.isfile(file_path):
            print("Invalid file path. Please enter a valid file path.")
            file_path = input("Enter the file path to encrypt: ")

        with open(file_path, 'r') as input_file:
            text = input_file.read()
            encrypted_text = caesar_cipher(text, shifts, encrypt=True)
            with open(output_filename, 'w') as output_file:
                output_file.write(encrypted_text)
            print(f"Encryption successful. Result written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_from_specific_file(output_filename, shifts):
    try:
        file_path = input("Enter the file path to decrypt: ")

        # Validate file path
        while not os.path.isfile(file_path):
            print("Invalid file path. Please enter a valid file path.")
            file_path = input("Enter the file path to decrypt: ")

        with open(file_path, 'r') as input_file:
            text = input_file.read()
            decrypted_text = caesar_cipher(text, shifts, encrypt=False)
            with open(output_filename, 'w') as output_file:
                output_file.write(decrypted_text)
            print(f"Decryption successful. Result written to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("\nWelcome to CAESAR'S CHIPER!\nMenu:")
    print("1. Encrypt text with Caesar Cipher")
    print("2. Decrypt text with Caesar Cipher")
    print("3. Encrypt with Extended Caesar Cipher")
    print("4. Decrypt with Extended Caesar Cipher")
    print("5. Encrypt from file with Caesar Cipher (default file)")
    print("6. Decrypt from file with Caesar Cipher (default file)")
    print("7. Encrypt from file with Caesar Cipher (specific file)")
    print("8. Decrypt from file with Caesar Cipher (specific file)")
    print("0. Exit")

    choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8 or 0): ")

    if choice == '1':
        text = input("Enter the text to encrypt: ")
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        result_text = caesar_cipher(text, shifts, encrypt=True)
        print("Encrypted Text:", result_text)

    elif choice == '2':
        text = input("Enter the text to decrypt: ")
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        result_text = caesar_cipher(text, shifts, encrypt=False)
        print("Decrypted Text:", result_text)

    elif choice == '3':
        text = input("Enter the text to encrypt with extended cipher: ")
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        result_text = caesar_cipher_extended(text, shifts, encrypt=True)
        print("Encrypted Text (Extended Cipher):", result_text)

    elif choice == '4':
        text = input("Enter the text to decrypt with extended cipher: ")
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        result_text = caesar_cipher_extended(text, shifts, encrypt=False)
        print("Decrypted Text (Extended Cipher):", result_text)

    elif choice == '5':
        encrypt_from_file("in_enc.txt", "out_enc.txt", shifts=3)

    elif choice == '6':
        decrypt_from_file("in_dec.txt", "out_dec.txt", shifts=3)

    elif choice == '7':
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        encrypt_from_specific_file("out_enc_s.txt", shifts)

    elif choice == '8':
        shifts = get_positive_integer_input("Enter the number of shifts: ")
        decrypt_from_specific_file("out_dec_s.txt", shifts)

    elif choice == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, 7, 8 or 0.")
