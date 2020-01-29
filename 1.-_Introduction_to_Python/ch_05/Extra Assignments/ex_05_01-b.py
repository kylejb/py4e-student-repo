## Chapter 05 | Exercise 01
# Write a program which repeatedly reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using try and except
# and print an error message and skip to the next number.

## Redoing Assignment to incorporate lists from later lecture.
## QUESTION:
#  Is there a way to construction this with a "for...in" loop? What's critical in making the decision between "for...in" and "while"?
#  I suspect "while" is the only way since the list is initially empty

# Kicking things off with a greeting to guide user
print(
    "Enter as many numbers as you wish to calculate their sum and average. When finished, enter 'done' instead of a number."
)

# Creating an empty list to append User_Input values
User_Numbers = list()


while True:
    ## QUESTION: why is the loop breaking if I start with a string value or when initially entering 'done'? This behavior did not occur prior to the introduction of lists.
    User_Input = input("Enter a number: ")
    if User_Input == "done":
        break
    try:
        _Number = float(User_Input)
        # User_Numbers.append(_Number) ## QUESTION: would it be best to nest 'list.append' within try? Pros/Cons? Not seeing difference in output after moving this to line 34.
    except:
        print(
            f"Error: {_Number} is not a valid entry; please enter a numerical value to continue or 'done' to exit."
        )
        continue

    User_Numbers.append(_Number)

Total_List_Value = sum(User_Numbers)
Average_List_Value = Total_List_Value / len(User_Numbers)

print("Total:", Total_List_Value)
print("Count:", len(User_Numbers))
print("Average", Average_List_Value)
