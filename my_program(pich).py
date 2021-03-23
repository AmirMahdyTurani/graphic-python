#بسم الله الرحمن الرحیم
#in the name of god
#import "turtle"
import turtle

# Create a list include color of program
colors = ["red", "purple", "blue", "green", "yellow", "orange","pink","brown"]

#set background color
turtle.bgcolor("black")

#create main loop
for i in range(368):
    #speed of cursor
    turtle.speed(99999999999999999999999999999999999999999)
    # use list colors
    turtle.pencolor(colors[i % 6])
    turtle.width(i / 180+1)
    turtle.forward(i)
    turtle.left(59)
