from turtle import Turtle

MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.refresh()
        self.setheading(90)

    def move_up(self):
        xcor = self.xcor()
        ycor = self.ycor() + MOVE_DISTANCE
        self.goto(xcor, ycor)

    def refresh(self):
        self.goto(0, -280)