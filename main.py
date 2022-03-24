import time
import turtle

from food import Food
from scorebord import ScoreBoard
from snake import Snake

REFRESH_RATE = 0.1


def snake_hit_wall(snake):
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        return True


def snake_hit_snake(snake_who_hit, snake_who_got_hit):
    for body_part in snake_who_got_hit.snake:
        if snake_who_hit.snake_head.distance(body_part) < 10 and body_part != snake_who_hit.snake_head:
            return True


screen = turtle.Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
no_of_player = int(screen.textinput("Snake Game", "no of player"))

if no_of_player == 1:
    snake = Snake()
    food = Food()
    score_board = ScoreBoard()

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(REFRESH_RATE)

        snake.move()
        if snake_hit_wall(snake):
            game_is_on = False
            score_board.game_over()

        if snake.snake_head.distance(food) < 15:
            food.refresh()
            score_board.increase_score()
            snake.grow()

        if snake_hit_snake(snake, snake):
            game_is_on = False
            score_board.game_over()


elif no_of_player == 2:
    snake1 = Snake(1)
    snake2 = Snake(2)
    food = Food()
    score_board1 = ScoreBoard(1)
    score_board2 = ScoreBoard(2)


    screen.listen()
    screen.onkey(snake1.up, "w")
    screen.onkey(snake1.right, "d")
    screen.onkey(snake1.left, "a")
    screen.onkey(snake1.down, "s")

    screen.onkey(snake2.up, "Up")
    screen.onkey(snake2.right, "Right")
    screen.onkey(snake2.left, "Left")
    screen.onkey(snake2.down, "Down")


    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(REFRESH_RATE)

        snake1.move()
        snake2.move()
        if snake_hit_wall(snake1) or snake_hit_wall(snake2):
            game_is_on = False
            score_board1.game_over()


        if snake1.snake_head.distance(food) < 15:
            food.refresh()
            score_board1.increase_score()
            snake1.grow()

        if snake2.snake_head.distance(food) < 15:
            food.refresh()
            score_board2.increase_score()
            snake2.grow()

        if snake_hit_snake(snake1, snake1) or snake_hit_snake(snake2, snake2):
            game_is_on = False
            score_board1.game_over()

        if snake_hit_snake(snake1, snake2) or snake_hit_snake(snake2, snake1):
            game_is_on = False
            score_board1.game_over()

elif no_of_player == 3:
    snake1 = Snake(1)
    snake2 = Snake(2)
    snake3 = Snake(3)
    food = Food()
    score_board1 = ScoreBoard(1)
    score_board2 = ScoreBoard(2)
    score_board3 = ScoreBoard(3)


    screen.listen()
    screen.onkey(snake1.up, "w")
    screen.onkey(snake1.right, "d")
    screen.onkey(snake1.left, "a")
    screen.onkey(snake1.down, "k_array")

    screen.onkey(snake2.up, "Up")
    screen.onkey(snake2.right, "Right")
    screen.onkey(snake2.left, "Left")
    screen.onkey(snake2.down, "Down")

    screen.onkey(snake3.up, "u")
    screen.onkey(snake3.right, "k")
    screen.onkey(snake3.left, "h")
    screen.onkey(snake3.down, "end_matrix")

    position = 3
    while snake1.alive or snake2.alive or snake3.alive:
        screen.update()
        time.sleep(REFRESH_RATE)

        if snake1.alive:
            snake1.move()
        if snake2.alive:
            snake2.move()
        if snake3.alive:
            snake3.move()

        if snake1.alive and snake1.snake_head.distance(food) < 15:
            food.refresh()
            score_board1.increase_score()
            snake1.grow()

        if snake2.alive and snake2.snake_head.distance(food) < 15:
            food.refresh()
            score_board2.increase_score()
            snake2.grow()

        if snake3.alive and snake3.snake_head.distance(food) < 15:
            food.refresh()
            score_board3.increase_score()
            snake3.grow()

        if snake1.alive and (
                snake_hit_snake(snake1, snake1) or snake_hit_snake(snake1, snake2) or snake_hit_snake(snake1,
                                                                                                      snake3) or snake_hit_wall(
                snake1)):
            snake1.die()
            score_board1.game_over(position)
            position -= 1

        if snake2.alive and (
                snake_hit_snake(snake2, snake1) or snake_hit_snake(snake2, snake2) or snake_hit_snake(snake2,
                                                                                                      snake3) or snake_hit_wall(
                snake2)):
            snake2.die()
            score_board2.game_over(position)
            position -= 1

        if snake3.alive and (
                snake_hit_snake(snake3, snake1) or snake_hit_snake(snake3, snake2) or snake_hit_snake(snake3,
                                                                                                      snake3) or snake_hit_wall(
                snake3)):
            snake3.die()
            score_board3.game_over(position)
            position -= 1


screen.exitonclick()
