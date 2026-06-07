"""
 Challenge: Offline Notes Locker

Create a terminal-based app that allows users to save, view, and search personal notes securely in an encrypted file.

Your program should:
1. Let users add notes with title and content.
2. Automatically encrypt each note using Fernet (AES under the hood).
3. Store all encrypted notes in a single `.vault` file (JSON format).
4. Allow listing of titles and viewing/decrypting selected notes.
5. Support searching by title or keyword.

Bonus:
- Add timestamps to notes.
- Use a master password to unlock vault (optional).
"""
import json
import os
from datetime import datetime
from cryptography.fernet import Fernet

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"


def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        with open(KEY_FILE, "wb") as key_file:
            key = Fernet.generate_key()
            key_file.write(key)
    
    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_notes():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    encrypted_content = fernet.encrypt(content.encode()).decode()
    data = load_vault()
    data.append({"title": title, "content": encrypted_content, "timestamp": timestamp})
    save_vault(data)
    print("Note added successfully!")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes found.")
        return
    for idx, note in enumerate(data, 1):
        print(f"{idx}. {note['title']} (Created: {note['timestamp']})")

def view_notes():
    list_notes()
    try:
        chioce = int(input("Enter note number to view: ").strip()) - 1
        data = load_vault()
        if 0 <= chioce <= len(data):
            note = data[chioce]
            decrypted_content = fernet.decrypt(note["content"].encode()).decode()
            print(f"Title: {note['title']}\nContent: {decrypted_content}\nCreated: {note['timestamp']}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    data = load_vault()
    found = False
    for note in data:
        if keyword in note["title"].lower() or keyword in fernet.decrypt(note["content"].encode()).decode().lower():
            decrypted_content = fernet.decrypt(note["content"].encode()).decode()
            print(f"Title: {note['title']}\nContent: {decrypted_content}\nCreated: {note['timestamp']}\n")
            found = True
    if not found:
        print("No matching notes found.")

def main():
    while True:
        print("\nOffline Notes Locker")
        print("1. Add Note")
        print("2. List Notes")
        print("3. View Notes")
        print("4. Search Notes")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1": add_notes()
            case "2": list_notes()
            case "3": view_notes()
            case "4": search_notes()
            case "5":
                print("Exiting...")
                break
            case _: print("Invalid option. Please try again.")

if __name__ == "__main__":    
    main()