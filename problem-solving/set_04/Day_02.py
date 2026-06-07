"""
Challenge: Batch Rename Files in a Folder

Goal:
- Scan all files in a selected folder
- Rename them with a consistent pattern:
    e.g., "image_1.jpg", "image_2.jpg", ...
- Ask the user for:
    - A base name (e.g., "image")
    - A file extension to filter (e.g., ".jpg")
- Preview before renaming
- Optional: allow undo (save original names in a file)

Teaches: File iteration, string formatting, renaming, user input
"""

import os

def batch_rename(folder_path, base_name, extension):
    files_to_rename = [f for f in os.listdir(folder_path) if f.lower().endswith(extension.lower()) and os.path.isfile(os.path.join(folder_path, f))]

    if not files_to_rename:
        print(f"No files with extension '{extension}' found in the folder.")
        return

    print("Files to be renamed:")
    for idx, file in enumerate(files_to_rename, start=1):
        print(f"{idx}. {file}")

    confirm = input("Do you want to proceed with renaming? (yes/no): ").strip().lower()
    print(f"User confirmation: {confirm}")
    if confirm != 'yes' and confirm != 'y':
        print("Renaming cancelled.")
        return

    for idx, file in enumerate(files_to_rename, start=1):
        new_name = f"{base_name}_{idx}{extension}"
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        print(f"Renamed: {file} → {new_name}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to rename files: ").strip() or os.getcwd()

    if not os.path.isdir(folder_path):
        print("Invalid folder path. Please try again.")
    else:
        base_name = input("Enter base name for files: ").strip()
        extension = input("Enter extension name for files: ").strip()

        batch_rename(folder_path, base_name, extension)