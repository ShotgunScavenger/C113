import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/pangp/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f'Hey, {event.src_path} has been created!')

    def on_deleted(self, event):
        print(f'Oops! Someone deleted {event.src_path}')

    def on_modified(self, event):
        print(f'Hey there, {event.src_path} has been modified!')

    def on_moved(self, event):
        print(f'Hello, someone moved {event.src_path} to {event.dest_path}!')

eventHandler = FileEventHandler()
observer = Observer()
observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()

try:
    while True:
        print('running...')
        time.sleep(2)
except KeyboardInterrupt:
    print('program shutdown...')
    observer.stop()

