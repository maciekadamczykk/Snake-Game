#Import turtle class and screen 
from turtle import Turtle, Screen
#Create a screen
screen = Screen()
screen.bgcolor("black")
screen.title("Snake")
screen.screensize(600,600)

#Create an object which will be the square on the screen
starting_points = [(0,0), (-20,0), (-40, 0)]

parts = []

for part in starting_points:
    new_part = Turtle()
    new_part.shape("square")
    new_part.color("#2CFF05")
    new_part.goto(part)
    parts.append(new_part)



screen.mainloop()