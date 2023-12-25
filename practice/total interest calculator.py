print("Interest Calculator:")
amount= float(input("Principle amount ?"))
roi = float(input("Rate of Interest ?"))
Years = int(input("Duration (no. of years) ?"))
total = (amount * pow(1 + (roi/100), Years))
interest = total - amount
print("\nInterest = %0.2f" %interest)

"""A = P(1 + r/n)^nt
where P = principal amount (initial investment)
r = annual nominal interest rete (as a decimal)
n = number ot times the interest is compounded per year
t = number of years """
