from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_8.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()

    list_box = Listbox(root)
    list_box.insert(1, "Python")
    list_box.insert(2, "Java")
    list_box.insert(3, "C++")
    list_box.insert(4, "Any other")
    list_box.pack()

    # list_box.after(2000, close_app)
    list_box.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
