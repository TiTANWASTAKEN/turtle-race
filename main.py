from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinate = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for custom_turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[custom_turtle])
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate[custom_turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner_list = []
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner_list.append(turtle)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

max_dist_covered = 0
winning_color = ""
for winner_turtle in winner_list:
    if max_dist_covered < winner_turtle.xcor():
        max_dist_covered = winner_turtle.xcor()
        winning_color = winner_turtle.pencolor()

if winning_color == user_bet:
    print(f"You've won! The {winning_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()
