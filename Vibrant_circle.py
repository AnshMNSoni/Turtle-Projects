# Vibrant Circle:

import turtle 

tt = turtle.Turtle()

turtle.bgcolor("black")
tt.speed("fastest")
tt.pencolor("cyan")
tt.penup()
tt.goto(0, 200)
tt.pendown()

for i in range(1, 210):
    tt.forward(i*3)
    tt.right(i)
    tt.hideturtle()
        
turtle.done()