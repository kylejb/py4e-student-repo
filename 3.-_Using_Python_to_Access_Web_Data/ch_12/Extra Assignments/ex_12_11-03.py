## Chapter 12, Section 11 | Exercise 03
"""
Use urllib to replicate the previous exercise of:

(1) retrieving the document from a URL, 
(2) displaying up to 3000 characters, and 
(3) counting the overall number of characters in the document. 

Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
"""

import urllib.request, urllib.parse, urllib.error

url = input("Enter URL: ")
fhand = urllib.request.urlopen(url)


character_count = 0
document = list()

for line in fhand:
    if len(line) < 1:
        break
    # print(line.decode().strip())
    line = line.decode().strip()
    words = line.split()
    for word in words:
        character_count += len(line)
        document.append(word)

#  Print the first 3,000 characters from retrived document over HTTP
## QUESTION: How do I print characters rather than words? As written, I think the way to approach this is to convert the list into string. Is there a better way?
print("Total number of characters:", character_count)
