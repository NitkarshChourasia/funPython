from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_10.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()
    root.title("Menu Demo")
    root.geometry("300x100")

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open...")
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)  # command = close app
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About")

    # root.after(2000, close_app)
    mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
