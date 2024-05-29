# Triangle in Triangle 

import turtle

tt = turtle.Turtle()
tt.speed("fastest")
turtle.bgcolor("black")
tt.pencolor('white')
tt.goto(-125, 0)

def Triangle(length, clr):
    tt.color(clr)
    tt.begin_fill()
    for side in range(3):
        tt.forward(length)
        tt.left(120)
    tt.end_fill()

def change():
    tt.penup()
    tt.left(30)
    tt.forward(45)
    tt.right(30)
    tt.pendown()
    
side = 400      
for count in range(5):
    if (count%2 == 0):
        Triangle(side, "white")
        change()
    elif (count%2 != 0):
        Triangle(side, "black")
        change()
        
    side -= 80
    
    
    
turtle.done()