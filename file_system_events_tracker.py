import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/seanl/Downloads"
to_dir = "C:/Users/seanl/OneDrive/Desktop/Coding/Sean Code/PRO/Projects 102+/Project-103Watch_Dog"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hi, {event.src_path} has been created!")
    
    def on_deleted(self, event):
        print(f"Heyy! Someone deleted {event.src_path}")

    def on_modified(self, event):
        print(f"Hey, someone modified {event.src_path}")
    
    def on_moved(self, event):
        print(f"Heads up! someone moved {event.src_path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()