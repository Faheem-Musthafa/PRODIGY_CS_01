def encrypt(text, shift):
    """Encrypt the given text using Caesar Cipher with specified shift."""
    result = ""
    for char in text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - ascii_base + shift) % 26
            result += chr(shifted + ascii_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    """Decrypt the given text using Caesar Cipher with specified shift."""
    return encrypt(text, -shift)

def crack(text):
    """Show all possible shifts of the text."""
    possibilities = []
    for shift in range(26):
        decrypted = decrypt(text, shift)
        possibilities.append((shift, decrypted))
    return possibilities

def main():
    while True:
        print("\n=== Caesar Cipher Program ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Crack an encrypted message")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("Thank you for using Caesar Cipher. Goodbye!")
            break
            
        elif choice in ['1', '2']:
            message = input("Enter your message: ").strip()
            
            while True:
                try:
                    shift = int(input("Enter the shift value (1-25): "))
                    if 1 <= shift <= 25:
                        break
                    else:
                        print("Shift must be between 1 and 25.")
                except ValueError:
                    print("Please enter a valid number.")
            
            if choice == '1':
                result = encrypt(message, shift)
                print("\nEncrypted message:", result)
            else:
                result = decrypt(message, shift)
                print("\nDecrypted message:", result)
                
        elif choice == '3':
            message = input("Enter the encrypted message: ").strip()
            print("\nAll possible decryptions:")
            print("-" * 40)
            
            possibilities = crack(message)
            for shift, text in possibilities:
                print(f"Shift {shift:2d}: {text}")
            print("-" * 40)
            
        else:
            print("Invalid choice. Please choose 1-4.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")