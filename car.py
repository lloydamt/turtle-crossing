from turtle import Turtle
import random

COLOURS = ['red', 'blue', 'green', 'orange', 'yellow']

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLOURS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        xcor = random.randint(-300, 300)
        ycor = random.randint(-250, 250)
        self.goto(xcor, ycor)
        self.setheading(180)

    def reappear(self):
        y_position = self.ycor()
        self.goto(300, y_position)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def create_car(self):
        self.penup()
        self.color(random.choice(COLOURS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        ycor = random.randint(-250, 250)
        self.goto(280, ycor)
        self.setheading(180)