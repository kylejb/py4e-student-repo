## Chapter 03 | Exercise 03
# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit.

score = input("Enter Score: ")

try:
    iscore = float(score)
    print(f"You entered {iscore}.")
    if iscore > 1.0:
        print(
            "Error - grading scale: Values cannot exceed 1.0. Please resubmit your request."
        )
    elif iscore < 0.0:
        print(
            "Error - grading scale: Values cannot be lower than 0.0. Please resubmit your request."
        )
except:
    print(
        "Error - unrecognized input: Only numerical values between 0.0 and 1.0 are accepted."
    )
    ## QUESTION
    # is it possible to restart or loop back to top instead of quitting?
    quit()

if iscore > 1.0:
    ## QUESTION
    # Does "quit()" differ from break and/or continue?
    quit()
if iscore >= 0.9:
    print("A")
elif iscore >= 0.8:
    print("B")
elif iscore >= 0.7:
    print("C")
elif iscore >= 0.6:
    print("D")
elif iscore < 0.0:
    quit()
else:
    print("F")
