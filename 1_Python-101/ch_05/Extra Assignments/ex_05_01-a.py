## Chapter 05 | Exercise 01
# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

Running_Total = None
Running_Count = None
print(
    "Enter as many numbers as you wish to calculate their sum and average. When finished, enter 'done' instead of a number."
)

while True:
    User_Input = input("Enter a number: ")
    if User_Input == "done":
        break
    try:
        number = float(User_Input)
    except:
        print(
            "Error: Invalid entry; please enter a numerical value to continue or 'done' to run calculations and exit."
        )
        continue

    if Running_Total == None and Running_Count == None:
        Running_Total = number
        Running_Count = 1
    else:
        Running_Total += number
        Running_Count += 1

if Running_Total == None or Running_Count == None:
    print("You have exited the program without entering any numerical values.")
else:
    print("Total:", Running_Total)
    print("Count:", Running_Count)
    print("Average:", Running_Total / Running_Count)
