"""
 Challenge: Auto File Organizer with Watchdog

Goal:
- Monitor a folder (e.g., Downloads/Desktop)
- When a new file is added:
    - Move PDFs to /PDFs
    - Move Images to /Images
    - Move ZIP files to /Archives
    - Everything else goes to /Others

Teaches: Folder monitoring, real-time automation, event-driven design
Tools: watchdog, shutil, os
"""
import os
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Desktop")

file_to_folder_mapper = {
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.txt': 'TextFiles'
}

class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        
        if event.is_directory:
            return
        
        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        target_folder = file_to_folder_mapper.get(ext, 'Others')
        full_path = os.path.join(WATCH_FOLDER, target_folder)

        os.makedirs(full_path, exist_ok=True)
        move_to = os.path.join(full_path, os.path.basename(filepath))

        try:
            shutil.move(filepath, move_to)
            print("✅ Operation successful")
        except OSError as e:
            print(f"❌ Operation failed: {e}")


if __name__ == "__main__":
    print(f"👀 watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()