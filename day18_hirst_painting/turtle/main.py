######## Challenge 1 - Draw a Square ############
import random
from turtle import Turtle
import turtle

t = Turtle()

for _ in range(4):
    t.forward(100)
    t.left(90)

t.right(90)
t.penup()
t.forward(100)
t.left(90)

########### Challenge 2 - Draw a Dashed Line ########
for _ in range(15):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    

########### Challenge 3 - Draw Shapes ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",  "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


t.penup()
t.goto(-50,50)
t.pendown()
    
for shape_side_n in range(3, 10):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)
    
    
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
t.pensize(15)
t.speed("fastest")

for _ in range(10):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))
    

# tim = t.Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

t.pensize(5)
draw_spirograph(5)