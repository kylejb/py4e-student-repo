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

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

emailList = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words[1])
    count += 1


print("There were", count, "lines in the file with From as the first word")

# py4e autograder tool did not accept the below input
# print(f"There were {count} lines in the file with From as the first word")
