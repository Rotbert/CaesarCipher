# Caesar Cipher Program

## Overview

This Python program implements the Caesar Cipher technique for encrypting and decrypting text. It provides a menu-driven command-line interface with various options, including encryption, decryption, and file operations.

## Features

- **Text Encryption and Decryption:** Encrypt or decrypt text using the Caesar Cipher technique.
- **Extended Cipher:** Additional options to handle numbers and symbols.
- **File Operations:** Encrypt and decrypt text from files, both default and specific.
- **User Input Validation:** Ensures valid input for text, shifts, and file paths.

## How to Use

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/caesar-cipher.git
    cd caesar-cipher
    ```

2. Run the program:

    ```bash
    python caesar_cipher.py
    ```

3. Follow the on-screen menu to choose options for encryption, decryption, file operations, and more.

## Menu Options

- **Encrypt (Option 1):** Encrypt a user-provided text with a specified number of shifts.
- **Decrypt (Option 2):** Decrypt a user-provided text with a specified number of shifts.
- **Encrypt with Extended Cipher (Option 3):** Encrypt text with additional support for numbers and symbols.
- **Decrypt with Extended Cipher (Option 4):** Decrypt text with additional support for numbers and symbols.
- **Encrypt from file (Default) (Option 5):** Encrypt text from a default input file (`in_enc.txt`) and write the result to a default output file (`out_enc.txt`).
- **Decrypt from file (Default) (Option 6):** Decrypt text from a default input file (`in_dec.txt`) and write the result to a default output file (`out_dec.txt`).
- **Encrypt from file (Specific) (Option 7):** Encrypt text from a user-provided input file and write the result to a default output file (`out_enc_s.txt`).
- **Decrypt from file (Specific) (Option 8):** Decrypt text from a user-provided input file and write the result to a default output file (`out_dec_s.txt`).
- **Exit (Option 0):** Exit the program.

## Requirements

- Python 3.x

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt) - see the [LICENSE](LICENSE.txt) file for details.
