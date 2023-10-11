from tkinter import *
import hupper


def start_reloader():
    return hupper.start_reloader("tkinter_5.main")


def close_app():
    global root
    root.destroy()


def main():
    global root
    root = Tk()
    root.title("Label and Entry Demo")
    root.geometry("300x300")
    lbl_fname = Label(root, text="First Name").grid(row=0)
    lbl_lname = Label(root, text="Last Name").grid(row=1)

    entry_fname = Entry(root)
    entry_fname.grid(row=0, column=1)
    entry_lname = Entry(root)
    entry_lname.grid(row=1, column=1)

    # c = Checkbutton(root, text="Keep me logged in").grid(columnspan=2)

    your_name = f"Hello {entry_fname.get()} {entry_lname.get()}"  # Fix this error of name fname and lname not showing.

    lbl_full_name = Label(root, text=your_name).grid(columnspan=2)

    # root.after(2000, close_app)

    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()
