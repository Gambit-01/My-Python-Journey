# import colorgram
# colors = colorgram.extract("image1.jpg",30)

# list = []
# for color in colors:
#     r, g, b= color.rgb
#     list.append((r,g,b))

# print(list)

import random
import turtle as t
t.colormode(255)
color_list = ((249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153))

screen = t.Screen()
tim = t.Turtle()

tim.speed(0)
tim.shape("turtle")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(255)
tim.setheading(0)

for i in range (10):

    for i in range (10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

tim.left(90)
tim.backward(50)
tim.right(90)
tim.setheading(225)
tim.forward(636.39)
tim.setheading(0)
tim.backward(50)

for i in range (10):

    for i in range (10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

tim.left(90)
tim.backward(500)
tim.right(90)
tim.forward(1000)

for i in range (10):

    for i in range (10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
tim.color("white")
screen = screen.exitonclick()







#Original trial code, it worked :)
# import random
# import turtle as t
# t.colormode(255)

# color_list = ((249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153))
# tim = t.Turtle()

# # tim.speed(0)
# tim.penup()
# tim.width(30)
# tim.backward(300)
# tim.right(90)
# tim.forward(200)
# tim.left(90)

# for i in range (10):
#     for i in range (10):
#         tim.color(random.choice(color_list))
#         tim.pendown()
#         tim.forward(1)
#         tim.penup()
#         tim.forward(50)
#         tim.pendown()
#     tim.penup()
#     tim.backward(510)
#     tim.left(90)
#     tim.forward(50)
#     tim.right(90)
# tim.color("white")

# screen = t.Screen()
# screen = screen.exitonclick()
