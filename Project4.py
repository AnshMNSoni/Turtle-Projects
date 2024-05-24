# Polygon:

import turtle

tt = turtle.Turtle()
turtle.bgcolor("black")
tt.speed("fastest")
tt.hideturtle()
clr = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(300):
    tt.pensize(i/100 + 1)
    tt.pencolor(clr[i%6])
    tt.forward(i)
    tt.right(30)
    
turtle.done()