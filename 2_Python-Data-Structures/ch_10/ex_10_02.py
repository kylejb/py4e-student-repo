## ASSIGNMENT: Ch 10, Q# 02

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for lines in handle:
    # Without adding too many variables, how should I go about adding .strip()?
    # Is this practice to eliminate white space for consistent parsing?
    lines = lines.strip()
    if lines.startswith("From "):
        lines = lines.split()
        time = lines[5].split(":")
        hour = time[0]
        ## Note
        # Feel a little shaky on this conceptually; review
        counts[hour] = counts.get(hour, 0) + 1

## Is there a better way for this as well?
# Output correctly displays target solution, so I passed; feels sloppy and would appreciate guidance
lst = sorted([(keys, values) for keys, values in counts.items()])
for k, v in lst:
    print(k, v)

## Appendix illustrating various attempts at ending the program

## Assignment
# This gets the order right, but it's sorted within dic()... we need it printed as key, value pairing
# print("Print1", sorted(counts.items()))

# Attemping to create a loop within a print statement, so I can have it iterate print statements within a single line
# print("Print2", sorted([(keys, values) for keys, values in counts.items()]))

# for keys, values in counts.items():
#    print(sorted(counts.items()))

#
# Built the below off memory from lecture
# Struggling with passing arguments into methods
# e.g. counts.items(reversed=False) didn't work
# googling for solutions
# print(sorted((keys, values) for (values, keys) in counts.items(), reversed=True))
# SyntaxError: "Generator expression must be parenthesized"
# Solution = "[ ]"
#
## QUESTION/ISSUE
#  Bonus Challenge
# print(sorted( [ (keys, values) for values, keys in counts.items(), reverse=True ] ) )
# SyntaxError: invalid syntax pointing to the comma before "reverse/reversed=True"
# Print function works without "reverse/reversed=True"
# Attempting to practice sorting by reversed count rather than hours for fun
# print(sorted([(keys, values) for values, keys in counts.items()]))
#
#
# Used the following manual methods to determine index in order to automate the python script
## QUESTION
# What's the programmatic (i.e. efficient) way to improve this process into my code? At the moment, I cannot grasp how to parse the information into a flow.
# testString = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
# tsFind = testString.find(":")
# print(tsFind)
# tsSplit = testString.split()
# x = tsSplit[5].split(":")
# print(tsSplit)
# print(x)
#
##BONUS
# Rewrite this code to minimize lines

# Do I need to end like this
# file.close()
