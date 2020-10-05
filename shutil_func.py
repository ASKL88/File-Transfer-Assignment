import shutil
import os
import datetime
import time
import shutil_gui
import shutil_main
from tkinter import filedialog


#set where the source of the files are
source = '/Users/AL/Desktop/FolderA/'

#set the destination path to folderB
dest = '/Users/AL/Desktop/FolderB/'
#files = os.listdir(source)

SECONDS_IN_DAY = 24 * 60 * 60

now = time.time()
before = now - SECONDS_IN_DAY

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(source):
    source_fname = os.path.join(source, fname)
    if last_mod_time(source_fname) > before:
        dest_fname = os.path.join(dest, fname)
        shutil.move(source_fname, dest_fname)

def checkdaily(self):
  folder = filedialog.askdirectory()
  #self.txt_one.delete(0, END)
  self.txt_one.insert(0,folder)

def receivedaily(self):
  folder = filedialog.askdirectory()
  #self.txt_two.delete(0, END)
  self.txt_two.insert(0,folder)
