# Exercise 6-8 from Python Crash Course Book
# Completed by Mack Sell


pet_1 = {
    'animal': 'dog',
     'owner': 'steve',
     'age': 5, 
     }


pet_2 = {
    'animal': 'cat',
     'owner': 'bryan',
     'age': 6, 
     }

pet_3 = {
    'animal': 'hamster',
     'owner': 'roger',
     'age': 3, 
     }


pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['animal']} that is {pet['age']} years old.")