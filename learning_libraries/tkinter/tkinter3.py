from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_3.main")


def close_app():
    global root
    root.destroy()


def main():
    root = Tk()
    root.geometry("300x300")
    root.title("Canvas Demo")

    canvas = Canvas(root, width=600, height=400, bg="#476042")

    canvas.pack(anchor=CENTER, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
