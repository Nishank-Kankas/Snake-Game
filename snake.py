import turtle
import random
import time
# from test import screen
MOVE_SPEED = 20
size = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_DISTANCE_BETWEEN_SNAKE = 100


def random_colour():
    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)


# move tail piece to head
def tail_to_head(head, tail):
    tail.goto(head.pos())


# move head
def head_move(head):
    head.forward(MOVE_SPEED)


def create_new_part(body_color=random_colour()):
    body = turtle.Turtle("square")
    body.shapesize(size, size)
    body.speed(0)
    body.penup()
    turtle.colormode(255)
    body.color(body_color)
    return body


class Snake:
    def __init__(self, snake_number=1, starting_len=3):
        self.snake = []
        self.body_colour = random_colour()
        for i in range(0, starting_len):
            body = create_new_part(self.body_colour)
            body.goto(-size * i, STARTING_DISTANCE_BETWEEN_SNAKE*(snake_number-2))
            self.snake.append(body)

        self.snake_head = self.snake[0]
        self.tail_part_no = len(self.snake) - 1
        self.snake_head.color("red")
        self.alive = True

    def move(self):
        tail_to_head(self.snake_head, self.snake[self.tail_part_no])
        self.tail_part_no -= 1
        if self.tail_part_no == 0:
            self.tail_part_no = len(self.snake) - 1
        head_move(self.snake_head)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def grow(self):
        new_part = create_new_part(self.body_colour)
        coordinate_of_tail = self.snake[self.tail_part_no].pos()
        new_part.goto(coordinate_of_tail)
        self.snake.insert(self.tail_part_no, new_part)
        self.tail_part_no += 1

    def die(self):
        self.alive = False




