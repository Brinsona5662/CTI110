# CTI-110
# P4LABb
# Alexander Brinson
# 11/15/2022
# This program draws my first and last initials

import turtle

#Code to draw A
turtle.left(110)
turtle.forward(115)
turtle.right(220)
turtle.forward(115)
turtle.left(180)
turtle.forward(50)
turtle.right(70)
turtle.forward(50)

#Code to draw B | MAKE SURE TO CODE IN PEN MOVEMENT
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(115)
turtle.right(90)

for i in range(0, 90):
     turtle.right(2)
     turtle.forward(1)

turtle.right(180)

for i in range(0, 90):
     turtle.right(2)
     turtle.forward(1)

turtle.exitonclick()

