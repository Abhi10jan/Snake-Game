from turtle import Turtle
ALLIGNMENT = 'center'
FONT = ('Times New Roman', 15, 'italic')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align=ALLIGNMENT, font=FONT)


    def game_over(self):
        self.clear()
        self.color('green')
        self.goto(0, 0)
        self.write(f"Game Over!", align=ALLIGNMENT, font=('Times New Roman', 20, 'bold'))
        self.goto(0, -30)
        self.write(f"Score = {self.score}", align=ALLIGNMENT, font=('Times New Roman', 20, 'bold'))