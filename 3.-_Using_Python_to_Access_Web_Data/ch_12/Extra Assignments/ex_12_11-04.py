## Chapter 12, Section 11 | Exercise 04
"""
Change the [ex_12_11-03.py] program to extract and count paragraph (p) tags from the retrieved HTML document 
and display the count of the paragraphs as the output of your program. Do not display the paragraph text, only count them. 
Test your program on several small web pages as well as some larger web pages.
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Take user input
url = input("Enter URL: ")
# Creating objects for data manipulation; note to self... better understand what happens to html and soup object (e.g., why is it nec.?)
html = urllib.request.urlopen(url, context=ctx).read()  # what object is this?
soup = BeautifulSoup(html, "html.parser")  # what object is this?

count = 0  # initializing counter variable to track number of <p> tags to be used in the below loop
tags = soup("p")
for tag in tags:
    count += 1
print(f"Number of <p> tags in {url}: {count}")

