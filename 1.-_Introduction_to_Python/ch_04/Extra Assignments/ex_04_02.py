## Chapter 04 | Exercise 02
## Section 4.7: Definition and Uses
# Move the last line of this program to the top, so the function call appears before the definitions.
# Run the program and see what error message you get.

## Copied from page 48
# def print_lyrics():
#    print("I'm a lumberjack, and I'm okay.")
#    print("I sleep all night and I work all day.")


# def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

# repeat_lyrics()

## Producing an error message, as per assignment instructions, by calling the function "repeat_lyrics" prior to defining it.
repeat_lyrics()


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


## RESULT:
# Traceback error... 'repeat_lyrics' is not defined.

