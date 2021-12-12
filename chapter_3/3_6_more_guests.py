# Exercise 3-6 from Python Crash Course Book
# Completed by Mack Sell

import importlib

previousExercise = importlib.import_module("3_5_changing_guest_list")

guests = previousExercise.guests

guests.insert(0,'George Clooney')

guests.append('George Carlin')

#guests.insert(-1, 'George Carlin')

guests.insert((len(guests)//2), 'Bob')

print('The guests list is:')
for guest in guests:
    print(guest)


