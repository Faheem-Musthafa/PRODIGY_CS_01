

---

# Caesar Cipher Program

This is a simple command-line application for encrypting, decrypting, and cracking messages using the Caesar Cipher technique. The Caesar Cipher is one of the oldest and simplest encryption techniques, where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encrypt a message**: Input a message and a shift value to receive the encrypted message.
- **Decrypt a message**: Input an encrypted message and a shift value to retrieve the original message.
- **Crack an encrypted message**: Automatically attempt all possible shifts to reveal the original message.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/caesar-cipher.git](https://github.com/Faheem-Musthafa/PRODIGY_CS_01.git
   cd caesar-cipher
   ```

2. Run the program:

   ```bash
   python caesar_cipher.py
   ```

3. Follow the on-screen prompts to choose between encryption, decryption, cracking, or exiting the program.

## Usage Example

```
=== Caesar Cipher Program ===
1. Encrypt a message
2. Decrypt a message
3. Crack an encrypted message
4. Exit

Enter your choice (1-4): 1
Enter your message: Hello, World!
Enter the shift value (1-25): 3

Encrypted message: Khoor, Zruog!
```

## Functions

- `encrypt(text, shift)`: Encrypts the given text using the Caesar Cipher with a specified shift.
- `decrypt(text, shift)`: Decrypts the given text using the Caesar Cipher with a specified shift.
- `crack(text)`: Displays all possible shifts for the encrypted text.
- `main()`: The main function that runs the command-line interface for user interaction.

## Requirements

- Python 3.1
---
