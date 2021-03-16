from turtle import Turtle, Screen 

screen = Screen()
screen.listen()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up(self):
        self.penup()
        going_up = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), going_up)