def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalnum(): # Check if the character is alphanumeric
            if char.isalpha(): # Check if the character is alphabetic
                base = ord('a') if char.islower() else ord('A') # Determine the base for lowercase or uppercase letters
                result += chr((ord(char) - base + shift) % 26 + base)  # Shift character within the alphabet, wrapping around if necessary
            else: # Handle numeric characters
                base = ord('0') # Base for digits
                result += chr((ord(char) - base + shift) % 10 + base) # Shift character within the digits, wrapping around if necessary
        else:
            result += char # Non-alphanumeric characters remain unchanged
    return result

def caesar_cipher_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalnum(): # Check if the character is alphanumeric
            if char.isalpha(): # Check if the character is alphabetic
                base = ord('a') if char.islower() else ord('A')
                result += chr((ord(char) - base - shift) % 26 + base)  # Reverse shift character within the alphabet, wrapping around if necessary
            else:
                base = ord('0')
                result += chr((ord(char) - base - shift) % 10 + base)  # Reverse shift character within the digits, wrapping around if necessary
        else:
            result += char  # Non-alphanumeric characters remain unchanged
    return result

while True:
    action = input("Would you like to encrypt or decrypt a message? (encrypt/decrypt): ").strip().lower()
    if action not in ['encrypt', 'decrypt']:
        print("Please enter 'encrypt' or 'decrypt'.")
        continue
        
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    if action == 'encrypt':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    else:
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    
    # Ask if user wants to perform another operation    
    repeat = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    if repeat != 'yes':
        break
