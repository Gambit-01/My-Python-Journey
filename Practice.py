# dictionary = {
#     "key":"what you use to open the door",
#     "messenger": "what you use to chat with your friends"
# }

# print(dictionary["key"])

# dictionary["handle"]= {"what you give your friends so that they can follow you on IG"}

# print(dictionary)

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     i = student_scores[student]
#     if i > 90 and i < 101:
#         grade = "Outstanding"
#     elif i > 80 and i < 91:
#         grade = "Exceeds Expctations"    
#     elif i > 70 and i < 81:
#         grade = "Acceptable"
#     elif i > 0 and i < 71:
#         grade = "Fail"
#     student_grades[student]=grade

# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visits,cities):
    
#     travel_log[3]={country}




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# from replit import clear
# #HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)
# import subprocess

# def clear_screen():
#     subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)



# from art import logo2
# print (logo2)

# More = "yes"
# Bidders = {}
# while More == "yes":

    
#     name = input ("what is your name\n")
#     price = int(input("What is you bid price\n"))
#     Bidders[name] = price
#     More = input("Are there any other users who want to bid\n").lower()
# comparitor = 0
# for person in Bidders:
#     if Bidders[person] > comparitor:
#         comparitor = Bidders[person]
#         winner = person
# print(f"The highest bidder is {winner} with a bid of {comparitor}")
# print (Bidders)

# import turtle
# import random

# color_list = [
#     "red", "orange", "yellow", "green", "blue",
#     "purple", "pink", "brown", "black",
#     "gray", "cyan", "magenta", "lightblue", "lightgreen",
#     "gold", "salmon", "lime", "aqua", "turquoise"
# ]

# # Function to create a turtle with given properties
# def create_turtle(color, shape, width, speed):
#     t = turtle.Turtle()
#     t.shape(shape)
#     t.color(color)
#     t.width(width)
#     t.speed(speed)
#     return t

# # Create the turtles
# tim = create_turtle("gold", "turtle", 10, 10)
# tom = create_turtle("blue", "turtle", 10, 10)
# tam = create_turtle("red", "turtle", 10, 10)

# tim.forward(1050)
# tam.backward(1050)
# tom.left(90)
# tom.backward(50)


# turtles = [tim, tom, tam]

# move = 1
# while move < 500:
#     for turtle in turtles:
#         turtle.color(random.choice(color_list))
#         way = [90, 180, 270, 360]
#         turtle.setheading(random.choice(way))
#         turtle.forward(35)
#     move += 1

# turtle.done()
# screen = turtle.Screen()
# screen.exitonclick()


from turtle import Screen, Turtle
screen = Screen()
import random
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("My snake Game")
import time


screen.tracer(0)
segment_list = []
turtle_position = [(0,0),(-20,0),(-40,0)]
x,y = -40,0
for i in range (70):
    yoo = (x,y)
    turtle_position.append(yoo)
    x-=20

for position in turtle_position:
    segment = Turtle(shape = "square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segment_list.append(segment)
# screen.update()
direction = [90,270,-90,-270]
game_is_on = True
i = 0
tre = len(segment_list)
while game_is_on:
    time.sleep(0.2)
    screen.update()
    for segment in range(len(segment_list)-1, 0, -1):
        r = segment_list[segment-1].xcor()
        t = segment_list[segment-1].ycor()
        segment_list[segment].goto(r,t)
    segment_list[0].forward(10)
    if i % 9 == 0:
        segment_list[0].right(random.choice(direction))
    segment_list[0].forward(0.5)
    i+=1


screen.exitonclick()