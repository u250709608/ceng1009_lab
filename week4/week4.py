for i in range(100):
    print("We like Python's turtles!")



months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
for month in months:
    print("One of the months of the year is", month)



numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for number in numbers:
    print(number, number*number)



import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.penup()
t.goto(-300,0)
t.pendown()

for i in range(3):
    t.forward(80)
    t.left(120)
t.penup()
t.forward(120)
t.pendown()
for i in range(4):
    t.forward(80)
    t.left(90)
t.penup()
t.forward(160)
t.pendown()
for i in range(6):
    t.forward(80)
    t.left(60)
t.penup()
t.forward(210)
t.pendown()
for i in range(8):
    t.forward(80)
    t.left(360/8)


import turtle
t = turtle.Turtle()
screen = turtle.Screen()
angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in range(10):
    t.forward(100)
    t.left(angles[i-2])
t.color("red")
t.shape("arrow")
t.stamp()
screen.exitonclick()
print("pirate final heading", t.heading())



import turtle
for i in range(5):
    t.forward(200)
    t.left(180 + 180/5)



import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.colormode("lightgreen")
t.shape("turtle")
t.color("blue")
t.pensize(3)
t.stamp()
t.penup()
for i in range(12):
    t.forward(125)
    t.pendown()
    t.forward(15)

    t.penup()
    t.forward(25)
    t.stamp()

    t.backward(165)
    t.right(360/12)






