from tkinter import *
import hupper


def start_reloarder():
    reloader = hupper.start_reloader("tkinter11.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()
    root.title("Message Demo")
    root.geometry("300x70")

    our_message = "This is our Message."
    message_var = Message(root, text=our_message)
    message_var.config(bg="lightgreen")
    message_var.pack()

    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloarder()
    main()
