from tkinter import *
from tkinter.ttk import *

from time import strftime



root = Tk()
root.title("clock")
root.configure(bg='black')
root.resizable(0, 0)



def time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string )
    label.after(1000, time)

    string2 = strftime("%D")
    label2.config(text = string2)
    label2.after(1000, time)



label2 = Label(font = "ds-digital 40", background = "black", foreground = "white")
label2.pack(side= "bottom", anchor="se")


label = Label(font = "ds-digital 90", background = "black", foreground = "white")
label.pack(side="top")



time()

mainloop()