from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self, score_board_number=1):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.color("white")
        if score_board_number == 1:
            self.scoreboard_pos = 0, 250
        if score_board_number == 2:
            self.scoreboard_pos = 0, -250
        if score_board_number == 3:
            self.scoreboard_pos = 0, -280
        self.goto(self.scoreboard_pos)
        self.score = 0
        self.show_score()


    def increase_score(self):
        self.score += 1
        self.show_score()


    def show_score(self):
        self.clear()
        self.write(arg=f"score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self, position=None):
        if position == 1:
            self.goto(0, 0)
            self.write(arg=f"WINNER", align=ALIGN, font=FONT)
        elif position:
            self.clear()
            self.write(arg=f":-x score: {self.score}", align=ALIGN, font=FONT)
        else:
            self.goto(0, 0)
            self.write(arg=f"Game Over", align=ALIGN, font=FONT)
