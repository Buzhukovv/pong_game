from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from score_board import Score

screen = Screen()
screen.title("Pong game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
screen.listen()
score = Score()

screen.onkey(paddle.move_right, 'm')
screen.onkey(paddle.move_left, 'z')

while True:
    time.sleep(ball.speed)
    screen.update()
    paddle.movement()
    ball.ball_direction()

    # paddle movement
    if paddle.left_paddle.ycor() > 240:
        paddle.left_paddle.setheading(270)
    elif paddle.left_paddle.ycor() < -240:
        paddle.left_paddle.setheading(90)

    if paddle.right_paddle.ycor() > 240:
        paddle.right_paddle.setheading(270)

    elif paddle.right_paddle.ycor() < -240:
        paddle.right_paddle.setheading(90)

    # collision of ball to wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.collision_to_wall()

    # collision to paddle
    if ball.distance(paddle.right_paddle) < 35 or ball.distance(paddle.left_paddle) < 35:
        ball.collision_to_paddle()

    if ball.xcor() > 450:
        score.change_the_score_of_left()
        ball.go_to_origin()

    if ball.xcor() < -450:
        score.change_the_score_of_right()
        ball.go_to_origin()


screen.exitonclick()
