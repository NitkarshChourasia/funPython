from tkinter import *
import hupper


def start_reloader():
    reloader = hupper.start_reloader("tkinter_1.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()
    root.title("Counting Seconds")
    root.geometry("300x50")

    button = Button(
        root,
        text="Stop",
        width=25,
        command=close_app,
        bg="#1FFFFF",
        activebackground="red",
        activeforeground="blue",
    )
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
