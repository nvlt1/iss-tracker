import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

# retrieve the name of all astronaut on iss
# url of api of current astronaut
url = "http://api.open-notify.org/astros.json"

# use this url object to open the api
response = urllib.request.urlopen(url)

#reads the response brought from the api
result = json.loads(response.read())

file = open("iss.txt", "w")
# str() wrap so we can concatanate the number into the string
file.write("There are currently" +
            str(result["number"]) + " astronauts on the ISS: \n\n")

# get the name of the astronauts
people = result["people"]
for p in people:
    file.write(p["name"] + " - on board" + "\n")


# print our current longitude and langitude in txt file
g = geocoder.ip("me")
file.write("\n Your current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")