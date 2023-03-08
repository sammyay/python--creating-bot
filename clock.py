import turtle

# Create a turtle
t = turtle.Turtle()

# Set the turtle's speed
t.speed(5)
b
# Set the turtle's shape
t.shape("turtle")

# Set the turtle's color
t.color("green")

# Set the turtle's pen size
t.pensize(8)

# Draw a square
for i in range(100):
    t.forward(100)
    t.right(90)
    t.color("red")

# Keep the window open until it is closed
turtle.mainloop(1)
