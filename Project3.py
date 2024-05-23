# Shape in shape:
import turtle

tt = turtle.Turtle()
tt.hideturtle()

tt.penup()
tt.back(100)
tt.pendown()
turtle.bgcolor("black")
tt.speed("fastest")

clr = ["pink", "cyan", "blue", "green", "orange", "red", "yellow"]
for sides in range(9, 2, -1):
    tt.color(clr[sides - 3])
    tt.begin_fill()
    for i in range(sides):
        tt.pencolor("black")
        tt.forward(100)
        angle = 360/sides
        tt.left(angle)
    tt.end_fill()

turtle.done()