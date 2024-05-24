# Square Pattern:

import turtle

tt = turtle.Turtle()

tt.speed("fastest")
turtle.bgcolor("black")
tt.hideturtle()

def square(cnt):
    add = 420
    count = cnt
    for i in range(5):
        if count == 0:
            count = 1
            add -= 60
            tt.begin_fill()
            tt.color("white")
            for side in range(4):
                tt.pencolor('black')
                tt.forward(add)
                tt.right(90)      
            tt.end_fill()
        else:
            count = 0
            add -= 60
            tt.color("black")
            tt.begin_fill()
            for side in range(4):
                tt.pencolor('black')
                tt.forward(add)
                tt.right(90)      
            tt.end_fill()


count = 0
for i in range(4):
    if (count == 0):
        count = 1
        tt.left(90)
        square(0)
    else:
        count = 0
        tt.left(90)
        square(1)
    
turtle.done()