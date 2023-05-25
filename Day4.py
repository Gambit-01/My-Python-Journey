import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Choose = input("Choose one option \n 1: rock \n 2: paper \n 3: scissors  ")
Choice = int(Choose)
Computer = random.randint(1,3)
tool = [rock, paper, scissors]

if Choice == Computer:
    print(f"{tool[Choice-1]} \n {tool[Choice-1]} \n It's a draw♻️")
elif Choice == 1 and Computer ==3:
    print(f"{tool[Choice-1]} \n {tool[Computer-1]} \n You win🤗")
elif Choice == 2 and Computer == 1:
    print(f"{tool[Choice-1]} \n {tool[Computer-1]} \n You win🤗")
elif Choice == 3 and Computer == 2:
    print(f"{tool[Choice-1]} \n {tool[Computer-1]} \n You win🤗")
else:
    print(f"{tool[Choice-1]} \n {tool[Computer-1]} \n You lose😔")
