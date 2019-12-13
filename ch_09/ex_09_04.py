# See ex-instructions_09_04 for assignment instructions

# Question:
# How would I instruction Python script to read files in other locations?
# Python script does not require to be installed in same folder/path, right?

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

max_Count = None
max_Word = None
## QUESTION
# Line 23: why counts.items() instead of just counts?
# general: I don't fully understand how this block works. how is max_Word tracked appropriately?
for word, count in counts.items():
    if max_Count is None or count > max_Count:
        max_Count = count
        max_Word = word

print(max_Word, max_Count)
print(counts.items())

## QUESTION
# Why does the following block of code produce significantly more values?
# I don't understand why the placement of line.split() affects the program logic in this way.

# words = line.split()
# for word in words:
# Parameter to focus only on lines starting with "From "
#    if line.startswith("From "):
#        email = words[1]
#        print(email)
# counts[email] = counts.get(email, 0) + 1
