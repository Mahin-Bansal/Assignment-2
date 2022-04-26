import turtle
import math


a = 150 # ellipse width
b = 20 # ellipse height
for i in range(361):
  t = i * (math.pi / 180)
  x = a * math.sin(t)
  y = b * math.cos(t) - b
  turtle.goto(x,y)


turtle.left(90)
turtle.forward(150)
turtle.right(139)
turtle.forward(226.71)
turtle.backward(226.71)
turtle.left(277)
turtle.forward(226.71)
turtle.done()
