# Diamond Hernandez
# 03-28-2026
# P4LAB1
# turtle graphics program

import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor("lightpink") 

# Turtle
t = turtle.Turtle()
t.color("#FF1493") 
t.pensize(3)
t.speed(3)

# Draw square 
for _ in range(4):
    t.forward(100)
    t.left(90)

# Draw triangle
t.penup()
t.goto(0, 100)
t.pendown()
t.fillcolor("#FF1493")
t.begin_fill()

count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1
t.end_fill() 

# Hide turtle
t.hideturtle()
screen.mainloop()