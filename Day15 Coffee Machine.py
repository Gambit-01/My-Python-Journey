MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 100,
    "milk": 100,
    "coffee": 10,
}



"BEGINNING OF MY CODE"

def coffee_type(type):
    """Returns true or false depending on the availability of resources and enables the program to continue running smoothly"""
    
    water = MENU[type]["ingredients"]["water"]
    coffee = MENU[type]["ingredients"]["coffee"]
    if type != "espresso":
        milk = MENU[type]["ingredients"]["milk"]
    else:
        milk = 0

    Cwater  = resources["water"]
    Cmilk = resources["milk"]
    Ccoffee = resources["coffee"]
   
    availability = True
   
    if Cwater < water:
        print("Sorry there is not enough water")
        availability = False
    if Ccoffee < coffee:
        print("Sorry there is not enough Coffee")
        availability = False
    if Cmilk < milk:
        print("Sorry there is not enough Milk")
        availability = False
    if availability == False:
        print("\n\n")
        return False
    else:
        return True
  

def calc_report(Cmoney):
    """This gives the report of the available resources in the coffee machine. Does not return anything"""
    Cwater  = resources["water"]
    Cmilk = resources["milk"]
    Ccoffee = resources["coffee"]
    print (f"water: {Cwater}\nMilk: {Cmilk}\nCoffee: {Ccoffee}\nMoney: {Cmoney}\n\n")

def transaction_check(total,type):
    """This checks if the money inserted is enough to buy a coffee. If not it prints a message and returns False else it returns True"""
    cost = MENU[type]["cost"]
    if cost > total:
        print("Sorry that's not enough money. Money refunded.\n\n")
        return False
    else:
        return True
    
def art():
    cup = """
     )  (  )
     (   ) )
      ) ( (
   __)_____)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'"""
    print(cup)
    



profit = 0
serve_on = True

while serve_on == True:
    print("\n\n")
    art()
    flavor = input("What would you like to drink? (espresso/latte/cappuccino):\n")

    if flavor == "report":
        calc_report(profit)
        go_on = False
    elif flavor == "off":
        go_on = False
        serve_on = False
    else:
        go_on = coffee_type(flavor)

    if go_on == True:
        coins = print("Please insert your coins")
        quaters = float(input("How many quarters\n"))
        dimes = float(input("How many dimes\n"))
        nickels = float(input("How many nickles\n"))
        pennies = float(input("How many pennies\n"))
        total_money = round((quaters * 0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01),2)
        print(f"total money entered is {total_money}")

        payment = transaction_check(total_money,flavor)
        
        if payment == True:
            profit +=  MENU[flavor]["cost"]
            resources["water"] = (resources["water"]-MENU[flavor]["ingredients"]["water"])
            resources["coffee"] = (resources["coffee"]-MENU[flavor]["ingredients"]["coffee"])
            if flavor != "espresso":
                resources["milk"] = (resources["milk"]-MENU[flavor]["ingredients"]["milk"])
            change = round(total_money - MENU[flavor]["cost"],2)
            if change > 0:
                print(f"Here is your {flavor}. Enjoy! \nHere is ${change} dollars in change.\n\n")
            else:
                print(f"Here is your {flavor}. Enjoy!\n\n")

    input("press enter to continue")




#2nd Version
# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])








