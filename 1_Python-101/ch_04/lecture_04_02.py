## Chapter 04 | Coursera Lecture
#  Copied code from lecture to mess around with a few lines
## QUESTION
#  What is the difference between "print()" and "return"? (p.51)


def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        print("Bonjour")
    else:
        return "Hello"


print(greet("es"), "Glenn")
print(str(greet("fr")) + "Glenn")
