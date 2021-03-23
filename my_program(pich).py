import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange","pink","brown"]

turtle.bgcolor("black")

for i in range(368):
    turtle.speed(99999999999999999999999999999999999999999)
    turtle.pencolor(colors[i % 6])
    turtle.width(i / 180+1)
    turtle.forward(i)
    turtle.left(59)
