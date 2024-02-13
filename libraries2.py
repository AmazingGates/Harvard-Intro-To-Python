# "APIs" or (Application Program Interface) are third party services that us programmers can write code to talk to.
# Here we will be learning about a "requests". The "requests" library allows us to make internet / web request
#using python code.
# In the example below, we will be using a "request" to pull information from the web.
# In the example below we were able to "requests" information for itunes using the link in the dode below.
# We wrote the code to ask for the artist you want information on. You can type the artists name in after 
#the .py when running the code.
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

x = response.json()
for result in x["results"]:
    print(result["trackName"])