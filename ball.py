from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("ball")
        self.color('white')

    def move(self):
        pass
