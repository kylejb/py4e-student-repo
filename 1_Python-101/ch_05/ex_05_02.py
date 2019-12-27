## Chapter 05 | Exercise 02
""" Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number 
catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below."""

## FYI - Assignment's Sample Code
"""// Starting Sample Code for Assignment below:

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    print(num)

print("Maximum", largest)"""

# QUESTION: How do i store values through iterative loop?
# QUESTION: How do i accept fractional input?

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid Entry: Enter numerical value.")
        continue
    print(fnum)
    if largest is None and smallest is None:
        largest = fnum
        smallest = fnum
    elif fnum > largest:
        largest = fnum
    elif fnum < smallest:
        smallest = fnum

if largest == None and smallest == None:
    print("You have exited the program without entering any numerical values.")
else:
    print("Maximum is", int(largest))
    print("Minimum is", int(smallest))
