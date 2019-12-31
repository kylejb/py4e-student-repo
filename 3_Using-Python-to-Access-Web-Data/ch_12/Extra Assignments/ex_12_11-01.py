## Chapter 12, Section 11 | Exercise 01
"""
Change [ex_12_01.py] to prompt the user for the URL so it can read any web page. 
You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. 
Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
"""

import socket


url_User = input("Enter valid URL for basic data extraction: ")
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## Question: did I use try/except correctly here? how can I improve?
try:
    url = url_User.split("/")
    print(url)
    mysock.connect((url[2], 80))
    cmd = (
        f"GET {url_User} HTTP/1.0\r\n\r\n".encode()
    )  # Question: do I need to add f"GET....{url_User}..." to enable url_User to passthrough correctly?
    mysock.send(cmd)
except:
    print(
        f"You entered {url_User}. If url is valid, please make sure you adhere to proper formatting standards."
    )
    quit()  # Question: how can I restart the loop to input? if I use continue or break, I get a syntax error (e.g., "outside the loop")


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()
