# Exercise 8-12 from Python Crash Course Book
# Completed by Mack Sell

def make_sandwich(*ingredients):
    print('\nYou chose the following ingredients:')
    for ingredient in ingredients:
        print(f'-{ingredient}')

make_sandwich('salami')
make_sandwich('lettuce','ham','meatball')