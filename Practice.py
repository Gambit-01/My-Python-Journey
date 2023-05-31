# dictionary = {
#     "key":"what you use to open the door",
#     "messenger": "what you use to chat with your friends"
# }

# print(dictionary["key"])

# dictionary["handle"]= {"what you give your friends so that they can follow you on IG"}

# print(dictionary)

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores:
#     i = student_scores[student]
#     if i > 90 and i < 101:
#         grade = "Outstanding"
#     elif i > 80 and i < 91:
#         grade = "Exceeds Expctations"    
#     elif i > 70 and i < 81:
#         grade = "Acceptable"
#     elif i > 0 and i < 71:
#         grade = "Fail"
#     student_grades[student]=grade

# # 🚨 Don't change the code below 👇
# print(student_grades)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,visits,cities):
    
#     travel_log[3]={country}




# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# from replit import clear
# #HINT: You can call clear() to clear the output in the console.

# from art import logo
# print(logo)
# import subprocess

# def clear_screen():
#     subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)



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