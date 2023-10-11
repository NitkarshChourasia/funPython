# Import module
from tkinter import *
import hupper
import re


def close_app():
    """Destroys the root window."""
    global root  # Make root a global variable
    root.destroy()


def start_reloader():
    """When changes are detected, reload the py program."""
    reloader = hupper.start_reloader("p3.main")


def main():
    """Where tkinter is used to create the GUI."""
    global root

    # Create the root window
    root = Tk()
    # root window title and dimension
    root.title("Python GUI 4")
    # Set geometry (widthxheight)
    root.geometry("350x200")

    # Adding a label to the root window
    lbl = Label(root, text="Hello World!")
    lbl.grid()

    # Adding Entry field.
    txt = Entry(root, width=10)
    txt.grid(column=1, row=0)

    # function to display user text when button is clicked.
    def special_character(char):
        pattern = r"[a-zA-Z0-9\s]"
        return re.match(pattern, char) is not None

    def end_special_character(last_char):
        if last_char == ".":
            return ""  # This works well.
        elif not special_character(last_char):  # something is flawed, here.
            # When false, then runs, when true then does not runs.
            return ""
        else:
            full_stop = "."
            return full_stop

    def clicked():
        last_char = txt.get()[-1]
        embed = end_special_character(last_char)
        res = f"You wrote {txt.get()}{embed}"
        # If special characters are used, at the end, then use this.
        lbl.configure(text=res)

    # Button widget with red color text inside.
    btn = Button(root, text="Click Me", fg="red", command=clicked)

    # Set button grid.
    btn.grid(column=2, row=0)

    # Close the tkinter after 2 seconds.
    # root.after(2000, close_app)

    # Execute Tkinter
    root.mainloop()


# Run this functions if this file is run as a script and not imported as a module.
if __name__ == "__main__":
    # start_reloader()
    main()
