## Chapter 04 | Exercise 06

# Write a program to prompt the user for hours and rate per
# hour using input to compute gross pay. Pay should be
# the normal rate for hours up to 40 and time-and-a-half for
# the hourly rate for all hours worked above 40 hours. Put
# the logic to do the computation of pay in a function
# called computepay() and use the function to do
# the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test. Pay should be 498.75.
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.


def computepay(hrs, rate):
    if hrs <= 40:
        basepay = hrs * rate
        return basepay
    if hrs > 40:
        basepay = 40 * rate
        overtime_hrs = hrs - 40
        overtime_rate = rate * 1.5
        # basepay plus overtime pay
        total_pay = (overtime_hrs * overtime_rate) + basepay
        return total_pay


h = input("Enter Hours:")
r = input("Enter Hourly Rate:")

hrs = float(h)
rate = float(r)

p = computepay(hrs, rate)
print(p)