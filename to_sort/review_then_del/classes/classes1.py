class Student:
    def __init__(self, f_name, l_name, roll_no):
        self.first = f_name
        self.last = l_name
        self.roll_no = roll_no

    def email(self):
        return f"{self.first}.{self.last}@nitkarsh_chourasia.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Student('{self.first}', '{self.last}', '{self.roll_no}')"

    def __str__(self):
        return f"{self.first} {self.last} - {self.roll_no}"

    def __add__(self, other):
        return self.roll_no + other.roll_no

    def __len__(self):
        return len(self.fullname())

    def __del__(self):
        return "Deleted!"

    def __getitem__(self, item):
        return self.first[item]

    def __setitem__(self, key, value):
        self.first[key] = value

    def __delitem__(self, key):
        del self.first[key]


student1 = Student("Nitkarsh", "Chourasia", 1)
student2 = Student("Anmol", "Chourasia", 2)
student3 = Student("Rohit", "Chourasia", 3)
student4 = Student("Varsha", "Chourasia", 4)
student5 = Student("Santosh", "Chourasia", 5)


# print(student1)
# print(student2)
# print(student3)
# print(student4)
# print(student5)
#
# print(student1 + student2)
#
# print(len(student1))


# Do check out this comments.
# What do they mean.
# Okay?!
# print(student1[0], end="")
# print(student1[1] + student1[2] + student1[3] + student1[4] + student1[5] + student1[6] + student1[7])

print(student1.__dict__)


def add(a, b):
    return a.__add__(b)


print(add(10, 20))


def len(a):
    return a.__len__()  # What are these? Are these functions?


print(len("Nitkarsh"))
print(len("Chourasia"))


def len(string):
    return "Hello, World!"


# So, I have the power to change the function.
# Hmm, interesting, I see.


print(len("Nitkarsh"))

N = "N"

# print(N)
# import builtins
# print(dir(builtins))


class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    # How to format the pay into a currency format?

    def email(self):
        return f"{self.fname}.{self.lname}@nitkarsh_chourasia.com"

    def fullname(self):
        return f"{self.fname} {self.lname}"


emp_1 = Employee("Nitkarsh", "Chourasia", 10_00_00)
emp_2 = Employee("Anmol", "Chourasia", 20_00_00)
emp_3 = Employee("Rohit", "Chourasia", 30_00_00)


print(99_999_999_999)  # This is a valid syntax.

import locale

# Set the locale to the user's default
locale.setlocale(locale.LC_ALL, "")

amount = 12345.67
formatted_amount = locale.currency(amount)
print(
    formatted_amount
)  # Output will be currency symbol based on your locale, e.g., $12,345.67 (for en_US locale)

# How to output comma separated numbers?
# Use the grouping option of locale.format() as follows:
# amount = 12345.67
# formatted_amount = locale.format.string("%d", amount, grouping=True)
# print(formatted_amount)  # Output: 12,345

# How to output comma separated numbers with decimal places?
# Use the grouping option of locale.format() as follows:
# amount = 12345.67
# formatted_amount = locale.format.string("%.2f", amount, grouping=True)
# print(formatted_amount)  # Output: 12,345.67

# Need to learn this, too.
# This are something functional more equipped to real world, I am learning.
# Right?!
# Yes.

import locale
import time

locale.setlocale(locale.LC_ALL, "")


class Employee:
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    def email(self):
        return f"{self.fname}.{self.lname}@nitkarsh_chourasia.com"

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

        # So, multiplicity issue will happen? Nah! Because it is assigned and not return assignment is taken care.

    # So, why is a decorator used, here?!
    # @classmethod
    # def set_raise_amount(cls, amount):
    #     cls.raise_amount = amount


emp_1 = Employee("Nitkarsh", "Chourasia", 10_00_00)
emp_2 = Employee("Anmol", "Chourasia", 20_00_00)

print("\n")
print("Testing my class raises, here.")
print("\n")

print(f"Employee 1 pay before raise: {emp_1.pay}")
print("applying raise ...")
# time.sleep(2)
print("applying raise 10%.")
emp_1.raise_amount = 1.10
emp_1.apply_raise()  # Should have a function to input what value I want to input or else the default one.
print(f"Employee 1 raise %: {emp_1.raise_amount}")
# time.sleep(1)
print("raise applied successfully.")
# time.sleep(1.5)
print(f"Employee 1 pay after raise: {emp_1.pay}")


print("\n")
print(f"Employee 2 pay before raise: {emp_2.pay}")
print(f"Employee 2 raise %: {emp_2.raise_amount}")
emp_2.apply_raise()
print(f"Employee 2 pay after raise: {emp_2.pay}")


# Understand it, refactor it and then commit it.
