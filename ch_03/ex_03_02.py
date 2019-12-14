# Improving ex_03_01.py with Try & Except in anticipation of user input error. Prevent crashing.

hrs = input("Enter Hours:")
rate = input("Enter your Hourly Wage:")
try:
    h = float(hrs)
except:
    h = -1
try:
    r = float(rate)
except:
    r = -1
    # alternatively, I could nest my "if h/r < 0 stuff within and even add "quit()" parameter to force it out

if h < 0:
    print("Please try again and input numerical value for hour.")
elif r < 0:
    print("Please try again and input numerical value for hour.")
elif h <= 40:
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