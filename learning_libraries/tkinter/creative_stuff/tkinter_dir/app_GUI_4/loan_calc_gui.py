# Importing the necessary modules.
from tkinter import *
import hupper


# Adding a live server for tkinter test GUI.
def start_reloader():
    reloader = hupper.start_reloader("loan_calc_gui.main")


# A func to close the GUI window.
# def close_app():
#     global root
#     return root.destroy()


class LoanCalculator:
    def __init__(self):
        # Declaring root for the close_app() to work.
        # global root

        # Create a window
        window = Tk()
        # root = window #? Will it work?

        # Create a title for the window.
        window.title("Loan Calculator")

        # Create the input boxes.

        Label(window, text="Annual Interest Rate").grid(row=1, column=1, sticky=W)
        Label(window, text="Number of Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, text="Monthly Payment").grid(row=4, column=1, sticky=W)
        Label(window, text="Total Payment").grid(row=5, column=1, sticky=W)

        # For taking inputs.

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(
            row=1, column=2
        )

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable=self.numberOfYearsVar, justify=RIGHT).grid(
            row=2, column=2
        )

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(
            row=3, column=2
        )

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(
            row=4, column=2, sticky=E
        )

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(
            row=5, column=2, sticky=E
        )

        # Create the button.
        btComputePayment = Button(
            window, text="Computer Payment", command=self.computePayment
        ).grid(row=6, column=2, sticky=E)

        # Create an event loop.
        window.mainloop()

        def computePayment(self):
            monthlyPayment = self.getMonthlyPayment(
                float(self.loanAmountVar.get()),
                float(self.annualInterestRateVar.get()) / 1200,
                int(self.numberOfYearsVar.get()),
            )

            self.monthPaymentVar.set(format(monthlyPayment, "10.2f"))
            totalPayment = (
                float(self.monthlyPaymentVar.get())
                * 12
                * int(self.numberOfYearsVar.get())
            )

            self.totalPaymentVar.set(format(totalPayment, "10.2f"))

        def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
            monthlyPayment = (
                loanAmount
                * monthlyInterestRate
                / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
            )
            return monthlyPayment

        root = Tk()  # Create the widget

    # call the class to run the program.


LoanCalculator()  # Create GUI
