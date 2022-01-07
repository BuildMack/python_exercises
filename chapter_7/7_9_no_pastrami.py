# Exercise 7-9 from Python Crash Course Book
# Completed by Mack Sell

sandwich_orders = [
    'pastrami', 'ruben','pastrami',
    'tomato', 'pastrami', 'turkey',
    'cucumber']

sandwich_finished = []

while sandwich_orders != []:

    if sandwich_orders[0].lower() == 'pastrami':
        print("\nI'm sorry, we are out of pastrami.")
        new_order = input('What would you like instead? ')
        sandwich_orders.append(new_order)

    else:
        print(f'\nYour {sandwich_orders[0]} sandwich has been completed.')
        sandwich_finished.append(sandwich_orders[0])
    
    sandwich_orders.remove(sandwich_orders[0])

print(f'\nCurrent orders: {sandwich_orders}')

print(f'\nCompleted sandwich: {sandwich_finished}')