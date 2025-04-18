from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) <15:
    scoreboard.refresh()
    snake.extend()
    food.refresh()

  if snake.head.xcor() > 290 or snake.head.xcor()<-290 or snake.head.ycor() > 290 or snake.head.ycor()<-290 :
     game_is_on = False

     scoreboard.game_over()

  for segments in snake.segment:
      if segments==snake.head :
          pass
      elif snake.head.distance(segments)<5:
          game_is_on = False
          scoreboard.game_over()
screen.exitonclick()