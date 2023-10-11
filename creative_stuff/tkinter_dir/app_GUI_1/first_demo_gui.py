# Importing the necessary required modules.
from tkinter import *
import re
import hupper


def close_app():
    """Destroys the root window."""
    global root  # Make root a global variable
    return root.destroy()


def start_reloader():
    """When changes are detected, reload the py program."""
    reloader = hupper.start_reloader("p5.main")


def main():
    """Where tkinter is used to create the GUI."""

    # Create the root window.
    root = Tk()

    # root window title and dimension.
    root.title = "Python GUI 5"

    # Set geometry (width x height)
    root.geometry("350x200")

    # Adding menu bar in root window.
    # new item in menu bar labelled as "New".
    # Adding more items in the menu bar.

    menu = Menu(root)
    item = Menu(menu)
    item.add_command(label="New")
    menu.add_cascade(label="File", menu=item)
    root.config(menu=menu)

    # Adding a label to the root window.
    lbl = Label(root, text="Hello World!")
    lbl.grid()

    # Adding entry field.
    txt = Entry(root, width=10)
    txt.grid(column=1, row=0)

    # function to display user text when button is clicked.

    def clicked():
        res = "You wrote" + txt.get()
        lbl.configure(text=res)

    # button widget with red color text inside.
    btn = Button(root, text="Click Me", fg="red", command=clicked)

    # Set button grid.
    btn.grid(column=2, row=0)

    # Execute Tkinter.
    root.mainloop()


if __name__ == "__main__":
    main()
