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
    


#SECOND CODE
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()

