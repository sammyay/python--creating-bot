import turtle

# create a turtle object
pen = turtle.Turtle()

# draw the face
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.begin_fill()
pen.fillcolor("yellow")
pen.circle(100)
pen.end_fill()

# draw the eyes
pen.penup()
pen.goto(-40, 20)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(20)
pen.end_fill()
pen.penup()
pen.goto(40, 20)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(20)
pen.end_fill()

# draw the mouth
pen.penup()
pen.goto(-60, -40)
pen.pendown()
pen.right(60)
pen.circle(80, 120)

# hide the turtle object
pen.hideturtle()

# keep the window open until closed manually
turtle.done()
