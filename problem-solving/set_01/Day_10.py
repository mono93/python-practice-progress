"""
Building a Caesar Cipher

Challenge: Secret Message Encryptor & Decryptor

Create a Python script that helps you send secret messages to your friend using simple encryption.

Your program should:
1. Ask the user if they want to (E)ncrypt or (D)ecrypt a message.
2. If encrypting:
   - Ask for a message and a numeric secret key.
   - Use a Caesar Cipher (shift letters by the key value).
   - Output the encrypted message.
3. If decrypting:
   - Ask for the encrypted message and key.
   - Reverse the encryption to get the original message.

Rules:
- Only encrypt letters; leave spaces and punctuation as-is.
- Make sure the letters wrap around (e.g., 'z' + 1 → 'a').

Bonus:
- Allow uppercase and lowercase letter handling
- Show a clean interface
"""

def encrypt_message(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
if choice == 'E':
    message = input("Enter the message to encrypt: ")
    key = int(input("Enter the numeric secret key: "))
    encrypted = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted}")
elif choice == 'D':
    encrypted_message = input("Enter the message to decrypt: ")
    key = int(input("Enter the numeric secret key: "))
    decrypted = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted}")
else:
    print("Invalid choice. Please select 'E' for encrypt or 'D' for decrypt.")