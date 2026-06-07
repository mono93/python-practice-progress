"""
 Challenge: File Sorter by Type

Goal:
- Scan the current folder (or a user-provided folder)
- Move files into subfolders based on their type:
    - .pdf → PDFs/
    - .jpg, .jpeg, .png → Images/
    - .txt → TextFiles/
    - Others → Others/
- Create folders if they don't exist
- Ignore folders during the move

Teaches: File system operations, automation, file handling with `os` and `shutil`
"""

import os
import shutil

file_to_folder_mapper = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.txt': 'TextFiles'
}

def get_target_folder(file_name):
    extension = os.path.splitext(file_name)[1].lower()
    return file_to_folder_mapper.get(extension, 'Others')


def sort_files_in_folder(folder_path):
    for file in os.listdir(folder_path):
        print(f"Processing: {file}")
        full_path = os.path.join(folder_path, file)

        extension = os.path.splitext(file)[1].lower()

        if os.path.isfile(full_path) and extension != '.py':
            target_folder = get_target_folder(file)
            target_path = os.path.join(folder_path, target_folder)

            os.makedirs(target_path, exist_ok=True)
            shutil.move(full_path, os.path.join(target_path, file))
            print(f"Moved: {file} → {target_folder}/")


if __name__ == "__main__":
    folder = os.getcwd()  # You can change this to a user-provided folder if needed
    sort_files_in_folder(folder)
    print("✅ Files have been sorted into their respective folders.")
