## Chapter 04 | Exercise 07
# Rewrite the grade program from the previous chapter (ex_03_03.py) using a function called
# computegrade that takes a score as its parameter and returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F


def computegrade(score):
    # if score > 1.0:  # preventing output for numerical values outside accepted range
    #    quit()  # QUESTION: Is there a more elegant solution (e.g., restarting)?
    if score >= 0.9:
        ## QUESTION:
        # Do I use print() or return? Why one over the other?
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    # elif score < 0.0:  # preventing output for numerical values outside accepted range
    #    quit()  # QUESTION: Is there a more elegant solution (e.g., restarting)?
    else:
        print("F")


impt = input("Enter your grade for conversion: ")

try:
    impt_score = float(impt)  # converting impt to float; if it fails, program to reset
    print(f"You entered {impt_score}.")
    if impt_score > 1.0 or impt_score < 0.0:
        print("Invalid Input: Please enter a number between 0 and 1")
    else:
        computegrade(impt_score)
except:
    # Prevent tracebacks for string values
    print("Error: Only numerical values between 0.0 and 1.0 are accepted.")
    quit()  # QUESTION: Is there a more elegant solution (e.g., restarting)?

## QUESTION:
# Regarding my interest in replacing quit() with another function such as "break" or "continue"
# 1) Why am I getting SyntaxError when I replace "quit()" on line 43 with break or continue?
# 2) How do I keep the program running until user exits?
