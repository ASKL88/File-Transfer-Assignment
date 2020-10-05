from tkinter import *
import tkinter as tk
from tkinter import messagebox
import shutil_gui
import shutil_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.title("Move Daily Files")
        self.master.minsize(525,175) #(Height, Width)
        self.master.maxsize(525,175)


        shutil_gui.load_gui(self)






if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
