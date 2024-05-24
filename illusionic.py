import turtle

tt = turtle.Turtle()
tt.speed("fastest")
turtle.bgcolor("black")
tt.penup()
tt.goto(200, 0)
tt.pendown()
tt.hideturtle()

def pattern():
    count = 0
    for r in range(200, 0, -10):
        if (count == 0):
            count = 1
            tt.pencolor("black") 
            tt.color("black")
            tt.begin_fill()
            tt.circle(r)
            tt.end_fill()
            
        elif (count == 1):
            count = 0
            tt.pencolor("black") 
            tt.color("white")
            tt.begin_fill()
            tt.circle(r)
            tt.end_fill()

pattern()
for i in range(3):
    tt.right(90)
    pattern()

turtle.done()