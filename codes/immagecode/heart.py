import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle()

def curve():
for i in range(200):
turtle.right(1)
turtle.forward(1)

def heart():
turtle.fillcolor(‘red’)
red.begin_fill()
red.left(140)
red.forward(113)
curve()
red.left(120)
curve()
red.forward(112)
red.end_fill()

heart()
red.ht()
turtle.done()