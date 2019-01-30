#!/bin/python3

import json
import urllib.request
import turtle
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']
print(people)

#craft = result['craft']
#print(craft)


for p in people:
  print(p['name'])
  print('in ' + p['craft'])

 
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')

screen.register_shape('iss2.png')
iss = turtle.Turtle()
iss.shape('iss2.png')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)

#Space Center, Houston
lat = 29.5502
lon = -95.097

location = turtle.Turtle()
location.penup()
location.color('red')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
#print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)
location.goto(0,0)


#Great Neck,
lat2 = 36.8982
lon2 = -76.0558

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon2,lat2)
location.dot(5)
location.hideturtle()



url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat2) + '&lon=' + str(lon2)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

#Hanoi,Vietnam
lat2 = 21.028280
lon2 = 105.853882

location = turtle.Turtle()
location.penup()
location.color('blue')
location.goto(lon2,lat2)
location.dot(5)
location.hideturtle()



url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat2) + '&lon=' + str(lon2)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)

#London,England

lat2 = 51.507351
lon2 = -0.127758

location = turtle.Turtle()
location.penup()
location.color('green')
location.goto(lon2,lat2)
location.dot(5)
location.hideturtle()



url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat2) + '&lon=' + str(lon2)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']
print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)
