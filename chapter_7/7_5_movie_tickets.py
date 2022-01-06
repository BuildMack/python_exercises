# Exercise 7-5 from Python Crash Course Book
# Completed by Mack Sell


age = int(input('\nWhat is your age? '))

if age < 3:
    cost = 'free'
elif 3 <= age <= 12:
    cost = '$10'
elif age > 12:
    cost = '$15'

print(f'\nYour ticket will be {cost}.')

