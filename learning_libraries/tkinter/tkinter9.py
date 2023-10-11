from tkinter import *


def start_reloader():
    return hupper.start_reloader("tkinter_9.main")


def close_app():
    global root
    root.destroy()


def main():
    root = Tk()
    root.title("Menubutton Demo")
    root.geometry("200x200")
    menu_button = Menubutton(root, text="Menu")
    menu_button

    menu_button.menu = Menu(menu_button, tearoff=0)
    menu_button["menu"] = menu_button.menu
    cVar = IntVar()
    aVar = IntVar()

    menu_button.menu.add_checkbutton(label="Contact", variable=cVar)
    menu_button.menu.add_checkbutton(label="About", variable=aVar)
    menu_button.pack()
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()


# It is just an introduction.
# Understand it more better, next time.
