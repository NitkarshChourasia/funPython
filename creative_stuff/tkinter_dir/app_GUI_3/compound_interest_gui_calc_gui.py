# Importing the necessary libraries
from tkinter import *
import hupper


def start_reloader():
    reloader = hupper.start_reloader("compound_interest_gui_calc_gui.main")


def close_app():
    global root
    return root.destroy()
    #! Find out what parameter input does it takes?!


# function for clearing the contents of all the entry boxes.
def clear_all(principal_field, rate_field, time_field, compound_field):
    # Whole content of entry boxes is deleted.

    principal_field.delete(0, END)
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)

    # set focus on the principal_field entry box
    principal_field.focus_set()


# Function to find compound interest.
def calculate_ci(principal_field, rate_field, time_field, compound_field):
    # get a content from entry box.

    principal = int(principal_field.get())

    rate = float(rate_field.get())

    time = float(time_field.get())

    # Calculates compound interest.

    CI = principal * (pow((1 + rate / 100), time))

    # insert method inserting the value in the text entry box.

    compound_field.insert(10, CI)


# Driver code.


def main():
    # Create a GUI window.
    root = Tk()

    # Set the backgroud color of GUI window.
    root.configure(background="#4C4E52")

    # Set the configuration of GUI window (WidthxHeight).
    root.geometry("400x250")

    # set the name of tkinter GUI window.
    root.title("Compound Interest Calculator")

    # Create a Principal Amount : label
    lbl1 = Label(root, text="Principal Amount(Rs) : ", fg="#FFFFFF", bg="#000000")

    # Create a Rate : label
    lbl2 = Label(root, text="Rate(%) : ", fg="#FFFFFF", bg="#000000")

    # Create a Time : label
    lbl3 = Label(root, text="Time(years) : ", fg="#FFFFFF", bg="#000000")

    lbl4 = Label(root, text="Compound Interest : ", fg="#FFFFFF", bg="#000000")

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .

    lbl1.grid(row=1, column=0, padx=10, pady=10)
    lbl2.grid(row=2, column=0, padx=10, pady=10)
    lbl3.grid(row=3, column=0, padx=10, pady=10)
    lbl4.grid(row=5, column=0, padx=10, pady=10)

    # Create a entry box
    # for filling or typing the information.

    principal_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .

    principal_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    # Create a submit button and attached to calculate_ci function.

    button1 = Button(
        root,
        text="Submit",
        bg="#000000",
        fg="#FFFFFF",
        command=lambda: calculate_ci(
            principal_field, rate_field, time_field, compound_field
        ),
    )

    # Create a clear button and attached to clear_all function.

    button2 = Button(
        root,
        text="Clear",
        bg="#000000",
        fg="#FFFFFF",
        command=lambda: clear_all(
            principal_field, rate_field, time_field, compound_field
        ),
    )

    button1.grid(row=4, column=1, pady=10)
    button2.grid(row=6, column=1, pady=10)

    # Start the GUI
    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()


# Should also add a rounding feature.
