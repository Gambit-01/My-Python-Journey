#Greeting and Welcoming User to Calcuculator
print ("Welcome to the tip calculator")
#Request for Total Bill amount
Bill = float(input("What was the total bill? $"))
#Request for the tip percentage they want to give
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Request for number of people that dined
Number_Of_People = float(input("How many people to split the bill?"))
#Calculation of tip
extra = float(Bill*(percentage/100))
#Calculation of final total with tip included
Final_Total = float(extra+Bill)
#The amount of money each person is to pay
Bill_per_person = round(Final_Total/Number_Of_People,2)
Bill_per_person = "{:.2f}".format(Bill_per_person)
print(f"Each person should pay:${Bill_per_person}")