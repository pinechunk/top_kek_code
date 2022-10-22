# need to install watchdog plugin
# looking for pdf, txt, jpg and html files on desktop and sorting them
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_track):
            extension = filename.split('.')
            if len(extension) > 1 and (extension[1].lower() == 'pdf' or extension[1].lower() == 'txt' or extension[1].lower() == 'jpg'):
                file = folder_track + '/' + filename
                new_path = folder_dest + '/' + filename
                os.rename(file, new_path)
            elif len(extension) > 1 and extension[1].lower() == 'html':
                file = folder_track + '/' + filename
                new_path = folder_dest2 + '/' + filename
                os.rename(file, new_path)

folder_track = "\\Users\\LEGION\\Desktop"
folder_dest = "\\Users\\LEGION\\Desktop\Docs"
folder_dest2 = "\\Users\\LEGION\\Desktop\HTML"

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()

try:
    while(True):
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()