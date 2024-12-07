import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen1 = turtle.Turtle()

pen.shape("turtle")
pen1.shape("turtle")

pen.color("red")
pen1.color("black")

pen.penup()
pen.goto(0,200)
pen.down()

pen.write("Welcome to turtlerace")

pen.hideturtle()

steps = int(input("How many steps?"))

def go_forward():
    pen1.forward(steps)

def go_up():
    pen1.setheading(90)

def go_down():
    pen1.setheading(270)

def go_left():
    pen1.setheading(180)

def go_right():
    pen1.setheading(0)

def click(x,y):
    #tracing
    screen.tracer(0)
    pen1.setheading(pen1.towards(x,y))
    pen1.goto(x,y)
    screen.tracer(1)   

def drag(x,y):
    screen.tracer(1)
    screen.goto(x,y)

screen.listen()
screen.onkey(go_forward, "space")
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_right, "d")
screen.onkey(go_left, "a")

screen.onclick(click)
pen1.ondrag(drag)



turtle.done()

