from turtle import Turtle

FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 1
        self.board = Turtle()
        self.board.hideturtle()
        self.hideturtle()
        self.board.penup()
        self.place_score()

    def place_score(self):
        self.board.clear()
        self.board.goto(-280, 260)
        self.board.write(f"Level: {self.level}, Score: {self.score}", align="left", font=FONT)
    
    def update_score(self):
        self.score += 5
        self.level += 1
        self.place_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAMEOVER", move=False, align=ALIGNMENT, font=FONT)
        
