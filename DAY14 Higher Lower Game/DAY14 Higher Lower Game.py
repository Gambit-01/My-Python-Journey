import random
import game_data 
from game_data import data


score = 0
def compare(followers_A,followers_B,guess):
    answer = ""
    
    if followers_A > followers_B:
        return guess == "a"
    else:
        return guess == "b"

Go_on = True
option_A = random.randint(0,49)
i=1
while Go_on == True:
    print("\n\n\n\n\n\n\n")
    print(game_data.logo6)
    if i > 1:
        score +=1
        print(f"You are right! Current score: {score}")
    print(f"Compare A: {data[option_A]['name']}, a {data[option_A]['description']}, from {data[option_A]['country']}")
    print(game_data.vs)
    option_B = random.randint(0,49)
    print(f"Against B: {data[option_B]['name']}, a {data[option_B]['description']}, from {data[option_B]['country']}")
    choice = input("Who has more followers? 'A' or 'B': ").lower()

        
    #create a function that comapares the followers of the two celebrities
    option_A_followers = data[option_A]['follower_count']
    option_B_followers = data[option_B]['follower_count']
    Go_on = compare(option_A_followers,option_B_followers,choice)
    option_A = option_B
    i+=1
print("\n\n\n\n\n\n\n")
print(game_data.logo6)
print(f"Sorry, that's wrong. Final score: {score}")


###2nd Version###
# from game_data import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()

