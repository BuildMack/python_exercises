# Exercise 3-7 from Python Crash Course Book
# Completed by Mack Sell

import importlib

previousExercise = importlib.import_module("3_6_more_guests")

guests = previousExercise.guests

print('My apologies, there are only two seats available!')

for i in range(len(guests)-2):
    uninvited = guests.pop()
    print(f'I am sorry {uninvited} but we do not have space for you at the table.')

for guest in guests:
    print(f'{guest}, you are still invited!')

print(guests)

del guests[1]

del guests[0]

print(guests)