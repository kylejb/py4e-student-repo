## Chapter 12, Section 11 | Exercise 05 (Advanced)
"""
Change [ex_12_01.py] so that it only shows data after the headers and a blank line have been received. 
Remember that recv receives characters (newlines and all), not lines.
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    data = data.decode()
    x = data.find("\r\n\r\n")
    # issue: program does not finishing printing "data" from url... stops short, but it does seem to correctly skip headers.
    print(data[x:])
    # print(data.decode(), end="")

mysock.close()
