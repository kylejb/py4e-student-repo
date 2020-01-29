## Chapter 13 | Exercise 03:  Using the GeoJSON API
"""
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program 
will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve 
the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.

API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get "No address..." response.

To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that 
is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and 
json endpoints so make sure you are using the same end point as this autograder is using.

Sample Execution

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2412 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8

Test Data 

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of 
"ChIJNeHD4p-540AR2Q0_ZjwmKJ8".
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

#  Hard coding url for assignment; this url has no API rate limits for students
serviceURL = "http://py4e-data.dr-chuck.net/json?"
## QUESTION: Why does this key of "42" resolve ouput issue?
apiKey = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Prompt user for a location
    location = input("Enter location: ")
    if len(location) < 1:
        break
    parameters = dict()
    parameters["address"] = location
    parameters["key"] = apiKey
    url = serviceURL + urllib.parse.urlencode(parameters)
    # Contact a web service and retrieve JSON for the web service and parse that data
    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print(f"Retrieved {len(data)} characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    # String to delineate output on terminal clearly for debugging
    print("======================")
    # Printing json output in terminal to assist with parsing the requested data for hw assignment
    print(json.dumps(js, indent=4))

    # Retrieve place_id from the JSON
    pl_id = js["results"][0]["place_id"]
    print(f"Google Map's 'place_id' for {location} is {pl_id}")
