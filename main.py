# ------- IMPORTS -------
from display import Display
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


# ------- INSTANCES -------
snake = Snake()
display = Display()
food = Food()
scoreboard = Scoreboard()


# ------- GLOBAL VARIABLES -------
game_is_on = True


# ------- MAIN LOOP -------
while game_is_on:
    # Sets up the game
    display.update_screen()
    time.sleep(.1)
    snake.movement_behaviour()
    display.on_key_pressed(snake)

    # Collisions with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_scoreboard()
        snake.add_segment()

    # Collision with walls
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
            or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        display.game_over()
        game_is_on = False

    # Collisions with tail
    # Ignores the distance check of the head with itself
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            display.game_over()
            game_is_on = False

display.exit_on_click()
