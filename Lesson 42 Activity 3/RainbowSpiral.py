import turtle
canvas = turtle.Screen()
canvas.bgcolor("black")
canvas.title("Rainbow Spiral")
canvas.setup(width=800, height=600)
t = turtle.Turtle()
t.speed(1)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
t.hideturtle()

while True:
    for i in range(200):
        t.pencolor(colors[i % len(colors)])
        t.width(i / 10 + 1)
        t.forward(i)
        t.left(59)
        # print(i)
    t.right(239)
    for i in range(200,0, -1):
        t.pencolor(colors[i % len(colors)])
        t.width(i / 10 + 1)
        t.forward(i)
        t.right(59)
        # print(i)
    


