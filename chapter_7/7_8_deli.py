# Exercise 7-8 from Python Crash Course Book
# Completed by Mack Sell

sandwich_orders = ['ruben', 'tomato', 'ham', 'turkey', 'cucumber']

sandwich_finished = []

while sandwich_orders != []:
    print(f'\nYour {sandwich_orders[0]} sandwich has been completed.')
    sandwich_finished.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])

print(f'\nCurrent orders: {sandwich_orders}')

print(f'\nCompleted sandwich: {sandwich_finished}')