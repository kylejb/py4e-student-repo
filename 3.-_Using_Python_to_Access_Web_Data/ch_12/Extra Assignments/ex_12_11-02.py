## Chapter 12, Section 11 | Exercise 02
"""
Change [ex_12_01.py] so that it counts the number of characters it has received and stops displaying any text after 
it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters 
and display the count of the number of characters at the end of the document.
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

character_count = 0
# document = []
document = b""

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    character_count += len(data.decode())
    document += data
    # document.append(x)

# Print the first 3,000 characters from retrived document over HTTP
## QUESTION: How can I improve upon the below? Should this be nested within "for...in" loop?
x = document.decode()
y = x.rstrip()
print(y[0:3000])
print("Total number of characters:", character_count)

mysock.close()
