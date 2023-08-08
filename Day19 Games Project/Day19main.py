from turtle import Turtle, Screen
import random
screen = Screen()
# screen.listen()
screen.setup( width = 500 , height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["tim","tam","jim","jam","john","tinky"]
turtle_list = []



def create_turtles(name,color):
    for i in range (0,6):
        names[i] = Turtle(shape = "turtle")
        names[i].color(colors[i])
        turtle_list.append(names[i])



create_turtles(names,colors)

up = -150    
for _ in turtle_list:
    _.penup()
    _.goto(x = -230, y = up)
    up+=50


if user_bet:
    start = True

while start:
    for _ in turtle_list:
        _.forward(random.randint(0,10))
        if _.xcor() > 230:
            start = False
            if user_bet == _.pencolor():
                print(f"Congratulations you {_.pencolor()} wins")
            else:
                print(f"You lost {_.pencolor()} is the winner")

screen.exitonclick()



















# turtle.colormode(255)
# color_list = ((249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153))

# def forwards():
#     tim.forward(50)

# def backwards():
#     tim.backward(100)

# def counter():
#     tim.left(10)

# def clockwise():
#     tim.right(10)

# def clear():
#     tim.setposition(0,0)
#     tim.setheading(0)
#     tim.clear()

# def art():
#     tim.speed("fastest")
#     tim.shape("turtle")
#     tim.pendown()
#     for _ in range (0,180,5):   
#         tim.color(random.choice(color_list))     
#         tim.setheading(_)
#         tim.circle(100)
#     # for _ in range (360,180,-5):   
#     #     tim.color(random.choice(color_list))       
#     #     tim.setheading(_)
#     #     tim.circle(100)
#     # tim.color("white")
#     # tim.left(90)


# screen.onkey(fun = forwards ,key = "w")
# screen.onkey(fun = backwards ,key = "s")
# screen.onkey(fun = counter ,key = "a")
# screen.onkey(fun = clockwise ,key = "d")
# screen.onkey(fun = clear ,key = "c")
# screen.onkey(fun = art ,key = "space")


# screen.exitonclick()
