from art import logo2
print (logo2)

More = "yes"
Bidders = {}
while More == "yes":

    
    name = input ("what is your name\n")
    price = int(input("What is you bid price\n"))
    Bidders[name] = price
    More = input("Are there any other users who want to bid\n").lower()
comparitor = 0
for person in Bidders:
    if Bidders[person] > comparitor:
        comparitor = Bidders[person]
        winner = person
print(f"The highest bidder is {winner} with a bid of {comparitor}")
print (Bidders)