# Exercise 7-10 from Python Crash Course Book
# Completed by Mack Sell

dream_vacations = []

active = True

while active:

    dream_vacation = input('What is your dream vacation destination? ')

    if dream_vacation.lower() == 'quit':
        active = False
    else:
        dream_vacations.append(dream_vacation)

print(f'The vacations identified are: {dream_vacations}')

unique_vacations = []

for vacation in dream_vacations:
    if vacation not in unique_vacations:
        unique_vacations.append(vacation)

print(f'The unique vacations identified are: {unique_vacations}')