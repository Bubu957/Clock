from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, time)

label = Label(font = "ds-digital 100", background = "black", foreground = "green")
label.pack(anchor="center")

time()

mainloop()