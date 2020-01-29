## Chapter 12 | Exercise 01 (Week 3)
"""
 You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

    http://data.pr4e.org/intro-short.txt

There are three ways that you might retrieve this web page and look at the response headers:

    Preferred: Modify the socket1.py program (https://www.py4e.com/code3/socket1.py) to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
    Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
    Use the telnet program as shown in lecture to retrieve the headers and content.
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
    ## QUESTION: what does "end" do? with it, the output is not bungled up (e.g., "You can write programs for many..." -- without "end" it appears as though there is a weird /n artifact)?
    #  print(data.decode(), end="")
    print(data.decode(), end="")

mysock.close()
