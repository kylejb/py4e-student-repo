# Write a program to prompt the user for hrs and rate per hour using input to compute gross pay
# Pay the hourly rate for the hrs up to 40 and 1.5 times the hourly rate for all hrs worked above 40 hrs
# You should use input to read a string and float() to convert the string to a number. 
# Do not worry about error checking the user input - assume the user types numbers properly. 
# Use 45 hr and a rate of 10.50 per hour to test the program (the pay should be 498.75). 


hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter your Hourly Wage:")
r = float(rate)

if h <= 40:
    paycheck = r * h 
    print(paycheck)
elif h > 40:
    overtime_h = h - 40
    overtime_r = r * 1.5
    overtime_paycheck = overtime_h * overtime_r
    paycheck = (r * 40) + overtime_paycheck
    print(paycheck)
else:
    print("Please try again. If errors persist, contact Human Resources for support.")