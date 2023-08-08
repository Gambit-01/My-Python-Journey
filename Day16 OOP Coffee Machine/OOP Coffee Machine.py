from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Items = MenuItem()


# print(Items.name)
# Resilent = Menu()
# print(Resilent.find_drink(Items.name))
# money_machine = MoneyMachine()
# money_machine.report()
# print(Items.ingredients)

Drink = Menu()
print(Drink.get_items())


money_machine = MoneyMachine()
money_machine.make_payment((Drink.find_drink("latte").cost))

Chill = CoffeeMaker()
Chill.report()
print(Chill.is_resource_sufficient(Drink.find_drink("latte")))
Chill.make_coffee((Drink.find_drink("latte")))


# Chill.is_resource_sufficient("")
Chill.report()
money_machine.report()
