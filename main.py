import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")

game_is_on = True
num = 0

while game_is_on:
    car_manager.create_car()
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    for car in car_manager.cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

    if player.ycor() > 300:
         player.player_reset()
         scoreboard.update_score()
         

screen.exitonclick() 

    
