from turtle import Turtle


class Paddle:
    def __init__(self):
        self.right_paddle = None
        self.left_paddle = None
        self.position_for_y_line = 250
        self.line_segments = None
        self.paddle_segments = None
        self.paddle_speed = 10
        self.position_for_x_left = -350
        self.position_for_y_left = 0
        self.position_for_x_right = 350
        self.position_for_y_right = 0
        self.create_paddle_left()
        self.create_paddle_right()
        self.create_line()

    def one_segment_creater(self):
        self.paddle_segments = Turtle()
        self.paddle_segments.penup()
        self.paddle_segments.shape("square")
        self.paddle_segments.color("white")
        self.paddle_segments.shapesize(stretch_wid=1, stretch_len=4, outline=None)
        self.paddle_segments.left(90)
        return self.paddle_segments

    def create_paddle_left(self):
        self.left_paddle = self.one_segment_creater()
        self.left_paddle.goto(self.position_for_x_left, self.position_for_y_left)

    def create_paddle_right(self):
        self.right_paddle = self.one_segment_creater()
        self.right_paddle.goto(self.position_for_x_right, self.position_for_y_right)

    def create_line(self):
        for i in range(18):
            self.create_sections_of_line()
            self.line_segments.goto(0, self.position_for_y_line)
            self.position_for_y_line -= 30

    def create_sections_of_line(self):
        self.line_segments = Turtle()
        self.line_segments.shapesize(stretch_wid=0.7, stretch_len=0.2, outline=None)
        self.line_segments.penup()
        self.line_segments.shape("square")
        self.line_segments.color("white")


    def move_right(self):
        self.right_paddle.right(180)

    def move_left(self):
        self.left_paddle.right(180)

    def movement(self):
        self.left_paddle.forward(self.paddle_speed)
        self.right_paddle.forward(self.paddle_speed)
