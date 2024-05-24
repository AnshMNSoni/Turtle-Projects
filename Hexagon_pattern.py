# Hexagon Pattern:

import turtle

tt = turtle.Turtle()

turtle.bgcolor("black")
tt.speed("fastest")
tt.penup()
tt.goto(0, 200)
tt.back(100)
tt.pendown()
tt.hideturtle()

clr = ["blue", "pink", "red", "yellow", "orange", "green"]

side = 6
for i in range(6, 250, 6):
    for j in range(6):
        tt.right(1)
        tt.pencolor(clr[j])
        tt.forward(i)
        tt.right(60)
    
    # Move the pen to another position
    tt.penup()
    tt.left(120)
    tt.forward(5)
    tt.right(120)
    tt.pendown()

turtle.done()