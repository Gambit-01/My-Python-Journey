import random
end_game = False
def compare(answer, guess):
    if guess == answer:
        global end_game
        print(f"Congratulations you win")
        end_game = True
    elif lives == 0:
        print(f"You lose, the number is {answer}")
    elif guess < answer:
        print(f"Number too low, try again, {lives} remaining")
    elif guess > answer:
        print(f"Number too high, try again, {lives} remaining")
    

def decrease_life():
    return (lives - 1)

end_game = False
from art import logo5
print(f"Welcome to the {logo5}")

level = input("Pick a level, easy or hard \n").lower()

if level == "hard":
    lives = 5
elif level == "easy":
    lives = 10
else:
    lives = 3

answer = random.choice(range (1,100))

while lives > 0 and end_game == False:
    guess = int(input("Guess your number"))
    lives = decrease_life()
    compare(answer,guess)
    

