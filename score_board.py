from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("red")
        self.penup()
        self.hideturtle()
        top_height = 220
        self.goto(0, top_height)
        self.score_change()

    def change_the_score_of_left(self):
        self.score_left += 1
        self.clear()
        self.score_change()

    def change_the_score_of_right(self):
        self.score_right += 1
        self.clear()
        self.score_change()

    def score_change(self):
        self.write(f"{self.score_left}      {self.score_right}", move=False, align='center', font=("arial", 60, "normal"))

