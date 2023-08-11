import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/caleb/watchDogFile"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Created: {event.src_path}")
    
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")
    
    def on_moved(self, event):
        print(f"Moved: {event.src_path} to {event.dest_path}")
    
    def on_deleted(self, event):
        print(f"Deleted: {event.src_path}")

observer = Observer()
event_handler = FileEventHandler()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
