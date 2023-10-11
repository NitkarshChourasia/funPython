from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_12.main")


def close_app():
    global root
    root.destroy()
    root.title("Radiobutton Demo")
    root.geometry("500x500")


def main():
    global root
    root = Tk()
    v = IntVar()
    Radiobutton(
        root, text="One", variable=v, value=1, font=("Helvetica", 20, "bold")
    ).pack(anchor=W),

    Radiobutton(
        root, text="Two", variable=v, value=2, font=("Helvetica", 20, "bold")
    ).pack(anchor=W)

    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()


from tkinter import *


# This increases the size of the radio buttons.
root = Tk()
v = IntVar()
Radiobutton(
    root, text="GfG", variable=v, value=1, indicatoron=0, width=20, height=2
).pack(anchor=W)
Radiobutton(
    root, text="MIT", variable=v, value=2, indicatoron=0, width=20, height=2
).pack(anchor=W)
mainloop()
