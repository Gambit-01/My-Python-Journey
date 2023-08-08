from turtle import Turtle, Screen
import random 
import turtle
turtle.colormode(255)




def random_color():
    y = random.randint(0,255)
    b = random.randint(0,255)
    r = random.randint(0,255)
    return (r,y,b)


tim = Turtle()    
tim.shape("turtle")
tim.color("gold")
tim.width(1)
tim.speed(0)


# # for i in range (0,4):
# #     tim.forward(200)
# #     tim.left(90)
# # tim.left(45)
# # tim.forward(282.84271)
# # tim.left(135)
# # tim.forward(200)
# # tim.left(135)
# # tim.forward(282.84271)
# # tim.right(180)
# # tim.forward(282.84271/2)
# # tim.right(45)
# # tim.color("red")


# # tim.color("white")
# # tim.backward(300)

# # tim.color("blue")

# # for i in range (50):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# tim.left(90)
# tim.penup()
# tim.backward(350)
# tim.right(90)
# tim.pendown()


# shape = 3
# angle = 120
# cycle = 0

# while cycle < 35:
#     tim.color(random.choice(color_list))
#     for _ in range (shape):
#         tim.forward(100)
#         tim.left(angle)

#     shape+=1
#     angle = (180-(180*(shape-2)/shape))
#     cycle += 1
for _ in range (0,180,5):   
    tim.color(random_color())       
    tim.setheading(_)
    tim.circle(100)
for _ in range (360,180,-5):   
    tim.color(random_color())       
    tim.setheading(_)
    tim.circle(100)
tim.color("white")
tim.left(90)

    

for _ in range (0,500): 
    tim.penup()  
    way = [90,180,270,360]        
    tim.setheading(random.choice(way))
    tim.forward(5)





screen = Screen()
screen.exitonclick()


# for _ in range (0,500):   
#     tim.color(random_color())
#     way = [90,180,270,360]        
#     tim.setheading(random.choice(way))
#     tim.forward(35)