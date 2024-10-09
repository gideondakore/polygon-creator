from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")
tim.color("PaleGreen4")

# POLYGONS

def polygon(p_angle):
    tim.forward(100)
    tim.right(p_angle)


turt_colors = ["AliceBlue", "aquamarine4", "DarkViolet", "gold1", "khaki", "indianRed", "lavender", "firebrick",
"turquoise4"]
size = 3
angle = 360

while size <= 10:
    for _ in range(size):
        polygon(angle/size)

    size += 1
    tim.color(random.choice(turt_colors))

