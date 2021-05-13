from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game 2.0")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280:
        snake.head.goto(-280, snake.head.ycor())
    elif snake.head.xcor() < -280:
        snake.head.goto(280, snake.head.ycor())
    elif snake.head.ycor() > 280:
        snake.head.goto(snake.head.xcor(), -280)
    elif snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), 280)

    #Collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()