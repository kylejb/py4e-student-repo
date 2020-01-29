# ASSIGNMENT INSTRUCTIONS | Ch 08, Problem 04
#
# Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should
# build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    # QUESTION
    # The below lines (14, 15)... is there a way to combine them?
    # Or is the below best practice in python?
    line = line.rstrip()
    words = line.split()
    # QUESTION
    # Is there another way to do this?
    # Is it best to track duplicates with another list/set?
    for word in words:
        if word not in lst:
            lst.append(word)
print(sorted(lst))

# Successfully completed this assignment
# 12/12/2019
