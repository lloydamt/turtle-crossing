from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-260, 270)
        self.display_level()

    def display_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)