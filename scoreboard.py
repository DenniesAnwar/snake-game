from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        if self.score < self.high_score:
            self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
    #     self.goto(0,-25)
    #     self.write(f"Your High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


