from turtle import Turtle, Screen
from snake import Snake
import time

# Screen Set-Up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake Set-Up
starting_positions = [(0,0), (-20,0), (-40,0)]

snake = Snake()

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()



screen.exitonclick()