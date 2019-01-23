#!/bin/python3

from turtle import*
from random import*

screen = Screen()
screen.setup(465,424)
colormode(255)
screen.bgcolor('black')

def randomcolour():
  red = randint(0,255)
  green = randint(0,255)
  blue = randint(0,255)
  color(red,green,blue)
  
def randomplace():
  penup()
  x = randint(-200,200)
  y = randint(-200,200)
  goto(x,y)
  pendown()
  
def randomheading():
  number = randint(1,360)
  setheading(number)

shape("turtle")
speed(0)

for i in range(30):
  randomcolour()
  randomplace()
  randomheading()
  stamp()
  
clear()
setheading(0)


def drawrectangle():
  randomcolour()
  randomplace()
  hideturtle()
  length = randint(10,100)
  height = randint(10,100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  end_fill()

for i in range(20):
  drawrectangle()

clear()
  

def drawcircle():
  randomcolour()
  randomplace()
  size = randint(1,100)
  dot(size)
  
for i in range(20):
  drawcircle()
  
clear()
  
def drawstar(size):
  begin_fill()
  for side in range(5):
    randomcolour()
    left(144)
    forward (size)
  end_fill()

for i in range(20):
  randomplace()
  size = randint(20,200)
  drawstar(size) 
  
clear()  
  
def drawhexagon(size):
  begin_fill()
  for side in range(6):
    randomcolour()
    left(60)
    forward (size)
  end_fill()

for i in range(20):
  randomplace()
  size = randint(20,100)
  drawhexagon(size) 
  
clear()
  
def drawchristmastree(size):
  begin_fill()
  for side in range(6):
    randomcolour()
    right(132)
    forward (size)
  end_fill()

for i in range(20):
  randomplace()
  size = randint(50,300)
  drawchristmastree(size) 