import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self):
        car_generator = random.randint(1,6)
        if car_generator == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=2, stretch_len=4)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())
    
    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
