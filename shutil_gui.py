from tkinter import *
import tkinter as tk
import shutil_main
import shutil_func

def load_gui(self):
    
    self.btn_one = tk.Button(self.master,width=25,height=1,text='Folder with files', command=lambda:shutil_func.checkdaily(self))
    self.btn_one.grid(row=1,column=0,padx=(15,0),pady=(35,10),sticky=W)
    
    self.btn_two = tk.Button(self.master,width=25,height=1,text='Folder that will receive files', command=lambda:shutil_func.receivedaily(self))
    self.btn_two.grid(row=2,column=0,padx=(15,0),pady=(5,10),sticky=W)

    self.btn_three = tk.Button(self.master,width=25, height=2,text='Press to File Check', command=lambda:shutil_func.last_mod_time)
    self.btn_three.grid(row=3,column=0,padx=(15,0),pady=(5,10),sticky=W)




    self.txt_one = tk.Entry(self.master, width=50, text='')
    self.txt_one.grid(row=1,column=5,rowspan=1,columnspan=6,padx=(15,0),pady=(30,10),sticky=E)
    self.txt_two = tk.Entry(self.master, width=50, text='')
    self.txt_two.grid(row=2,column=5,rowspan=1,columnspan=6,padx=(15,0),pady=(0,10),sticky=E)
  


if __name__ == "__main__":
    pass
