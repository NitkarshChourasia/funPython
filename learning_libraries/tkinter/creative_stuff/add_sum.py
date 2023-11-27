from tkinter import *
from tkinter.ttk import *


def add_sum(num1, num2):
    """A program to add two numbers."""
    return num1 + num2


root = Tk()


root.title("First paragraph")
root.geometry("400x400")


# button = Button(frame, text="QUIT", command=quit).pack()

lbl = Label(root, text="Hello, World!")
lbl.grid()


def clicked():
    # So, I can multiple functions, good.
    lbl.configure(text="Button was clicked !!")


btn = Button(root, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

root.mainloop()
