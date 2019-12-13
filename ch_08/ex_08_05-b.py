## ASSIGNMENT INSTRUCTIONS | Ch 08, Problem 05
#
# Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
#
## INITIAL SAMPLE CODE
#
# fname = input("Enter file name: ")
# if len(fname) < 1 : fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# print("There were", count, "lines in the file with From as the first word")
#
#
#
## ALTERNATIVE ATTEMPT TO PRACTICE ITERATIVE LOOPS

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
# is there a more elegant way to keep counter?
# e.g. incorporate a list within the loop to track printed line count
# and then pass that to the print statement outside of the loop
# the list can retain the number of values stored.
# range() can replicate a counter in this case?
# OR len()
# count = 0

emailList = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    emailList.append(words[1])

# Is there a way to replicate the output format from ex_08_05
# Outside of the given requirements for the assignment, is it ever necessary to do so? What's an example use case?
print(emailList[0 : len(emailList)])

print(f"There were {len(emailList)} lines in the file with From as the first word")
