from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Second Demo Program")

# Set geometry (width x height)
root.geometry("500x500")

# adding a label to the root window

lbl = Label(root, text="Hello, World!")
lbl.grid()


root.mainloop()
