from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.rand = None
        self.shape("circle")
        self.penup()
        self.shapesize(1, 1)
        self.color("red")
        self.direction = []
        self.current_direction = self.heading()
        self.for_reverse_y = 10
        self.for_reverse_x = 10
        self.speed = 0.06

    def ball_direction(self):
        new_x = self.xcor() + self.for_reverse_x
        new_y = self.ycor() + self.for_reverse_y
        self.goto(new_x, new_y)

    def collision_to_wall(self):
        self.for_reverse_y *= -1

    def collision_to_paddle(self):
        self.for_reverse_x *= -1
        self.speed *= 0.9

    def go_to_origin(self):
        self.home()
        self.speed = 0.06


