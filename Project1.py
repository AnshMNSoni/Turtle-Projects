# Chakra:
import turtle

tt = turtle.Turtle()

tt.color("Black")
tt.hideturtle()
tt.speed("fast")

tt.penup()
tt.back(150)
tt.pendown()
tt.forward(300)

tt.begin_fill()
for i in range(23):
    tt.left(165)
    tt.forward(300)
tt.end_fill()

turtle.done()  