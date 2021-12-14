# Exercise 5-7 from Python Crash Course Book
# Completed by Mack Sell

fruits_in_stock = [
    "apple", "pineapple", "cherry",
    "strawberry", "blueberry", "watermelon",
    'coconut','lemon','kiwi'
    ]

if fruits_in_stock:    #Returns true as long as the lis is not empty
    for fruit_in_stock in fruits_in_stock:
        if 'pineapple' == fruit_in_stock.lower():
            print('Get a pineapple!')
        if 'apple' == fruit_in_stock.lower():
            print('Get an apple!')
        if 'cherry' == fruit_in_stock.lower():
            print('Get a cherry!')
        if 'kiwi' == fruit_in_stock.lower():
            print('Get a kiwi!')

#Alternatively, if we don't care about ensuring all values in the list are 
#lowercase and don't care about first verifying that the list is not empty:

if 'pineapple' in fruits_in_stock:
    print('Get a pineapple!')
if 'apple' in fruits_in_stock:
    print('Get an apple!')

#etc...