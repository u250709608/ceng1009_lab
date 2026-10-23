import turtle
#
#
# --setup--
wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
#
# # --functions --
#
def drawPoly(someturtle,somesides,somesize):
    angle = 360/somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(angle)
#
#         # -- exercises --
#         # Exercises 2
#         tess.pencolor("hotpink")
#         drawPoly(tess,somesides 8,somesize 50):

def drawSpiral(someturtle,angle):
    size = 1
    for i in range(100):
        someturtle.forward(size)
        someturtle.right(angle)
        size = size + 2

# Exercises 3
tess.pencolor('red')
tess.penup()
tess.goto(-150, 0)
tess.pendown()
drawSpiral(tess,90)


 # -- finish --
wn.exitonclick()

def drawStar(someturtle,size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

for i in range(5):
    drawStar(tress,50)
    tress.penup()
    tress.forward(200)
    tress.right(144)
    tress.pendown()


def drawSprite(someturtle,legs,length):
    angle = 360/legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)

drawSprite(tress,15,120)
