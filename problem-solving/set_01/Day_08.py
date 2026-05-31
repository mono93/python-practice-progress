"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import string
import random
from getpass import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        issues.append("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        issues.append("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        issues.append("Password must contain at least one digit.")
    if not any(char in string.punctuation for char in password):
        issues.append("Password must contain at least one special character.")
    return issues

def suggest_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password = getpass("Enter your password: ")
issues = check_password_strength(password)

if not issues:
    print("Your password is strong!")
else:    
    print("Your password is weak for the following reasons:")
    for issue in issues:
        print(f"- {issue}")
    print("\nHere's a strong password suggestion for you:")
    print(suggest_strong_password())