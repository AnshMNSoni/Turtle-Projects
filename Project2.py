# Circles on Circle Drawing:
import turtle
from math import *

tt = turtle.Turtle()
tt.hideturtle()
tt.speed("fastest")
turtle.bgcolor("black")

for x in range(1, 270):
    
    if (x %2 == 0):
        tt.pencolor("yellow")
    else:
        tt.pencolor("red")
        
    tt.penup()
    tt.goto(70*cos(x), 70*sin(x))
    tt.pendown()
    tt.circle(70)

turtle.done()