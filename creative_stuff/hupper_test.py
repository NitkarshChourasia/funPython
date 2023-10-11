import hupper
from tkinter import *


def start_reloader():
    reloader = hupper.start_reloader("hupper_test.main")


def main():
    root = Tk()
    root.title("Hupper Test")
    root.geometry("500x500")

    lbl = Label(root, text="Label, here.")
    lbl.pack()

    button = Button(root, text="This is a button.")
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    start_reloader()
    main()
