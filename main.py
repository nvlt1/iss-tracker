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

# setyp the world map in turtle module
screen = turtle.Screen()
#1280 = width, 720 = height
screen.setup(1280, 720)

# create the x, y coords of the 4 corners of the canvas so iss can freely
# traverse the map and come back around to the other side
screen.setworldcoordinates(-180, -90, 180, 90)

# load the world map image

screen.bgpic("map.gif")
screen.register_shape("iss.gif")
# Turtle() is the main class
iss = turtle.Turtle()
iss.shape("iss.gif")
# give the pan shap an angle of 45 degrees when moving
iss.setheading(45)
iss.penup() # for no more drawing

# input('stop')

while True:
    #load the current status of the ISS in real-time
    # 2nd api
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    #extract the ISS location
    location = result["iss_position"]
    lat = location["latitude"]
    lon = location["longitude"]