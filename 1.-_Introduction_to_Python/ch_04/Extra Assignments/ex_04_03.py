## Chapter 04 | Exercise 03
## Section 4.7: Definition and Uses
# Move the function call back to the bottom and move the definition of print_lyrics after the definition
# of repeat_lyrics. What happens when you run this program?

## Copied from page 48
# def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print("I sleep all night and I work all day.")


# def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

# repeat_lyrics()

## As per assignment instructions, I am defining "repeat_lyrics" with "print_lyrics()" before it is defined.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


repeat_lyrics()

## RESULT: No Error; output is correct
#  It appears ordering is not importnat when defining functions, as long as the functions are not called
## QUESTION:
# Why is there no traceback error though? What's the "flow of execution" in the program?
# Doesn't python read from top to bottom? And, since it does, why doesn't a conflict occur because of the first
# function's call to an undefined function?
