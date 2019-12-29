## Chapter 11 | Exercise 03
"""
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers. 

Data Format
The file contains much of the text from the introduction of the textbook except that random numbers
are inserted throughout the text. Here is a sample of the output you might see:

Why should you learn to write programs? 7746
12 1929 8827
Writing programs (or programming) is a very creative
7 and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
8837 a difficult data analysis problem to having fun to helping 128
someone else solve a problem.  This book assumes that
everyone needs to know how to program ...

The sum for the sample text above is 27486. The numbers can appear anywhere in the line.
There can be any number of numbers in each line (including none).

Handling The Data
The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
and summing up the integers.
"""

import re

# Using "regex_sum332713.txt" for the graded assignment; I will likely reattempt this assignment using the "regex_sum_42.txt" for additional practice later.
handle = open("regex_sum_332713.txt")

numbers = list()

for line in handle:
    line = line.rstrip()
    # Using regex to extract numerical values from the file line by line
    data = re.findall("[0-9]+", line)

    # Using the len function to exclude empty lines (i.e. lines without numerical values are now empty because of the extraction that took place above)
    if len(data) < 1:
        continue

    ## QUESTION:
    #  How do I convert list to float in order to do various calculations (e.g., sum of all values)?
    #  I attempted float() with various variables, but ran into errors like "TypeError: list indices must be int or slices, not str" and "TypeError: float() arrgument must be a string or a number, not 'list'."
    ## Disclaimer: While searching for an answer, I found and copied the below code from GitHub user kiok46... however, I'm still unsure as to why this is necessary and what it does.
    # Why does the below work? Why do I need range(len())?
    for n in range(len(data)):
        numfloat = float(data[n])
        numbers.append(numfloat)

print(sum(numbers))
