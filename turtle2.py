import turtle
import turtle
wn =turtle.Screen()
elan= turtle.Turtle()
distance =50
angle=90
for i in range(20):
    elan.right(45)
    elan.forward(distance)
    elan.right(angle)
    distance=distance+5
    angle =angle-3
turtle.exitonclick()