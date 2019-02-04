from turtle import *
from random import randint 

speed(10)
penup()
goto(-140,140)




for step in range(15):
  write(step, align ='center')
  right(90)
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)
  penup()
  forward(10)
  pendown()
  forward(10)

  penup()
  backward(140)
  left(90)
  forward(10)
  forward(12)
  
forward(20)


ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,70)
bob.pendown()

em = Turtle()
em.color('yellow')
em.shape('turtle')
em.penup()
em.goto(-160,20)
em.pendown()

gat = Turtle()
gat.color('green')
gat.shape('turtle')
gat.penup()
gat.goto(-160,1)
gat.pendown()

tom = Turtle()
tom.color('purple')
tom.shape('turtle')
tom.penup()
tom.goto(-160,115)
tom.pendown()

for turn in range(113):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  em.forward(randint(1,5))
  gat.forward(randint(1,5))
  tom.forward(randint(1,5))


for turn in range(2):
 bob.right(180)
for turn in range(10):
 ada.right(36)
for turn in range(72):
 em.right(5)
for turn in range(60):
 gat.right(6)
for turn in range(90):
 tom.right(4)