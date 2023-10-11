import hupper
from tkinter import *


def close_app():
    global root  # Make root a global variable
    root.destroy()


def start_reloader():
    reloader = hupper.start_reloader("p3.main")


def main():
    global root  # Make root a global variable
    # creates root window
    root = Tk()
    # root window title and dimension
    root.title("Nitkarsh Chourasia")
    # Set geometry (width x height)
    root.geometry("500x500")

    # adding a label to the root window.
    lbl = Label(root, text="Hello, World!")
    lbl.grid()

    # function to display text when button is clicked
    def clicked():
        lbl.configure(text="So, this was clicked.")

    # button widget with red color text inside
    btn = Button(root, text="Don't click me", fg="red", command=clicked)

    # position of button on the root window

    # set Button grid
    btn.grid(column=1, row=0)
    # root.after(1000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
