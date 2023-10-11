# Import the required libraries
from tkinter import *
import hupper


def start_reloader():
    reloader = hupper.start_reloader("rank_based_Percentile_GUI.main")


def close_app():
    global root
    return root.destroy()


# Function to calculate percentile
def getPercentile():
    # Take a value from the respective entry boxes
    # get method returns current text as string

    students = int(total_participantField.get())

    rank = int(rankField.get())

    # Variable to store the result upto 3 decimal points.
    result = round((students - rank) / students * 100, 3)

    percentileFiled.insert(10, str(result) + "%")


# Function to clearing the contents of all text entry boxes.
def Clear():
    # deleting the content from the entry box
    rankField.delete(0, END)

    total_participantField.delete(0, END)

    percentileField.delete(0, END)


# Driver code
def main():
    # Create a GUI window.
    root = Tk()

    # Set the background colour of GUI window.
    root.configure(background="#4C4E52")

    # set the name of tkinter GUI window.
    root.title("Rank Based - Percentile Calculator")

    # Set the configuration of GUI window (WidthxHeight)
    gui.geometry("400x250")

    # Create a Rank: Label.
    rank = Label(root, text="Rank:", bg="#4C4E52", fg="white")

    # Create a And: Label
    and1 = Label(root, text="And", bg="#4C4E52", fg="white")

    # Create a totoal_participant: Label

    total_participant = Label(
        root, text="Total Participants:", bg="#4C4E52", fg="white"
    )

    # Create a Find Percentile Button and attached to getPercentile function.

    find = Button(
        root, text="Find Percentile", fg="Black", bg="#FFFFFF", command=getPercentile
    )

    percentile = Label(root, text="Percentile:", bg="#4C4E52", fg="white")

    clear = Button(root, text="Clear", fg="Black", bg="#FFFFFF", command=Clear)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.

    # padx attributed provide x-axis margin
    # from the root window to the widget.

    rank.grid(row=1, column=1, padx=10)
    and1.grid(row=1, column=4)

    total_participant.grid(row=1, column=6, padx=10)

    # pady attributed provide y-axis.
    # margin from the widget.

    find.grid(row=3, column=4, pady=10)

    percentile.grid(row=4, column=3, padx=10)

    clear.grid(row=5, column=4, pady=10)

    # Create a text entry box for filling
    # typing the information.

    rankField = Entry(root)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like strucutres.

    rankField.grid(row=1, column=3, padx=10)

    # root.after(2000, close_app)
    root.mainloop()


if __name__ == "__main__":
    # start_reloader()
    main()


# Not complete.
