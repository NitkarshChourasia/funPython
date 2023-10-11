from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_6.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()

    frame = Frame(root)
    frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM)

    red_button = Button(frame, text="Red", fg="red")
    red_button.pack(side=LEFT)

    green_button = Button(frame, text="Green", fg="green")
    green_button.pack(side=LEFT)

    blue_button = Button(frame, text="Blue", fg="blue")
    blue_button.pack(side=LEFT)

    black_button = Button(bottom_frame, text="Black", fg="black")
    black_button.pack(side=BOTTOM)

    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
