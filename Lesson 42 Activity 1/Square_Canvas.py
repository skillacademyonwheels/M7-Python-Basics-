import turtle

# Create a canvas
canvas = turtle.Screen()
canvas.bgcolor("orange")  # Set the background color
# canvas.title("Square Canvas")
canvas.setup(width=600, height=600)
turtle.title("Square Canvas")

## Turtle object creation
t = turtle.Turtle()
# Set the turtle speed
t.speed(1)
# Set the turtle color
t.color("Blue")

# Draw a square
for _ in range(4):
    t.forward(100)  # Move forward by 100 units
    t.right(90)     # Turn right by 90 degrees