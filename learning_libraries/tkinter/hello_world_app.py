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
    root.geometry("500x250")
    root.title("Label Demo")

    lbl_1 = Label(root, text="Hello World", font=("Arial Bold", 50))

    # Put the lbl1 in the center of the screen with a responsive width

    lbl_1.pack(anchor=CENTER, expand=True)
    # The expand thing is good.

    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()


# The best, program as per my liking, as what I wanted it to be.

# So, this is how to make installables.
