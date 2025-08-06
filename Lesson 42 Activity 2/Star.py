import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")
canvas.title("Star Pattern")
canvas.setup(width=600, height=600)

t = turtle.Turtle()
t.color("yellow")
t.speed(1)

t.goto(-100, 0)  # Move to starting position
t.forward(100)  # Draw the first line of the star
# First triangle for the star
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.right(150)
t.forward(50)

# Second triangle for the star
t.pendown()
t.right(90)
t.forward(100)
t.right(120)
t.forward(100)
t.right(120)
t.forward(100)

# import turtle library    
# for i in range(50):
#    t.forward(150)           
#    t.right(144)               
# turtle.done()


turtle.done()  # ✅ Correct way to finish turtle graphics
