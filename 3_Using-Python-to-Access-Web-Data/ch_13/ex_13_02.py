## Chapter 13 | Exercise 02:  Extracting Data from JSON
"""
In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program 
will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from 
the JSON data, compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other 
is the actual data you need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each 
student will have a distinct data url for the assignment - so only use your own data url for analysis.

Data Format

The data consists of a number of names and comment counts in JSON as follows:

{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}

The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at 
geoxml.py to see how to prompt for a URL and retrieve data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...
"""
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Hard coding URL for debugging
# Still getting "failure to retrieve output" (i.e. js = None)
# // resolved by removing try, except and using len() for iterative loop
# url = "http://py4e-data.dr-chuck.net/comments_42.json"

# Take user input of host/domain url for json parsing
url = input("Please enter URL: ")
# Checks whether url ends with '.json'; if not, concatenates to url string before python gets to work
if not url.endswith(".json"):
    jsonURL = url + ".json"
else:
    jsonURL = url

## Question: what is 'addinfourl'? it seems to be the type(uh)?
#  Creating python object from json data from opening url to storing data.json()
uh = urllib.request.urlopen(jsonURL, context=ctx)
data = uh.read().decode()
print(f"Retrieved {len(data)} characters")

## Question: What's breaking within this block of code below?
# try:
#    js = json.loads(data)
#    print("yay")
# except:
#    print("DANGERRRR")
#    js = None

js = json.loads(data)

#  Flag in event js is None
## Question: Why does this occur? How do I troubleshoot this issue?
if not js or "status" not in js or js["status"] != "OK":
    print("==== Failure To Retrieve ====")
    print(data)


# Printing json output in terminal to assist with parsing the requested data for hw assignment
print(json.dumps(js, indent=4))

# Is the following also groundwork for a viable solution --> foo = js.get("dic-key-here")?
countList = list()
for cnt in range(len(js["comments"])):
    commentCountText = js["comments"][cnt]["count"]
    countList.append(commentCountText)

print("Total comment counts:", sum(countList))
