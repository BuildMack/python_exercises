# Exercise 6-8 from Python Crash Course Book
# Completed by Mack Sell


person_1 = {
    'first_name': 'Ben',
     'last_name': 'Saadia',
     'age': 23, 
     'city': 'Kingston'
     }


person_2 = {
    'first_name': 'Sarah',
     'last_name': 'Conner',
     'age': 27, 
     'city': 'Toronto'
     }

person_3 = {
    'first_name': 'Bob',
     'last_name': 'Sager',
     'age': 30, 
     'city': 'San Diego'
     }

people =[person_1,person_2,person_3]

for person in people:
    print(f"{person['first_name']} {person['last_name']} lives in {person['city']} and is {person['age']}")