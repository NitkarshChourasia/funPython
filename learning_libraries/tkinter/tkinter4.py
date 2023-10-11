from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_4.main")


def close_app():
    global root
    return root.destroy()


def main():
    global root
    root = Tk()
    root.geometry("300x300")
    root.title("Checkbutton Demo")

    var1 = IntVar()
    Checkbutton(root, text="male", variable=var1).grid(row=0, sticky=W)

    var2 = IntVar()
    Checkbutton(root, text="female", variable=var2).grid(row=1, sticky=W)

    root.after(2000, close_app)

    mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
