# Exercise 7-2 from Python Crash Course Book
# Completed by Mack Sell

group_size = int(input('How many people are in your dinner group? '))

if group_size > 20:
    print("I'm sorry, we can not accomodate so many guests.")
elif group_size > 8:
    print("I'm sorry, you will have to wait for a table.")
elif group_size > 0: 
    print('Your table is ready!')
