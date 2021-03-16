
from turtle import Turtle 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10 #Gonna have to work with x coordinate so they move side to side


class CarManager(Turtle):
    def __init__(self):
        super().__init__()            
        self.shape("rectangle")
        self.color(COLORS)
