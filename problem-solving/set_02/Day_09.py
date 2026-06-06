"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os

VAULT_FILE = 'vault.txt'

def encode_credentials(text):
    return base64.b64encode(text.encode()).decode()

def decode_credentials(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])
    return ['weak', 'medium', 'strong'][min(score, 2)]

def add_credentials(website, username, password):
    strength = password_strength(password)
    line = f"{website}|{username}|{password}"
    encoded_line = encode_credentials(line)

    with open(VAULT_FILE, mode='a', encoding='utf-8') as vault:
        vault.write(encoded_line + '\n')
    print(f"Credentials for {website} added with password strength: {strength}")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("No credentials found.")
        return
    
    with open(VAULT_FILE, mode='r', encoding='utf-8') as vault:
        for line in vault:
            decoded_line = decode_credentials(line.strip())
            website, username, password = decoded_line.split('|')
            masked_password = '*' * len(password)
            print(f"Website: {website}, Username: {username}, Password: {masked_password}")

def main():
    while True:
        print("\nCredential Manager")
        print("1. Add Credentials")
        print("2. View Credentials")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_credentials(website, username, password)
        elif choice == '2':
            view_credentials()
        elif choice == '3':
            print("Exiting Credential Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()