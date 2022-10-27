import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.sr_path} has been created!")

     def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.sr_path}!")

     def on_modified(self,event):
        print(f"Hey there!, {event.sr_path} has been modiied")

     def on_moved(self,event):
        print(f"Someone moved, {event.sr_path} to {event.dest_path}") 

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()






