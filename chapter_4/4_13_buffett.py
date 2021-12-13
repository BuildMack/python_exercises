# Exercise 4-13 from Python Crash Course Book
# Completed by Mack Sell

#Practice using tuples

buffet_foods = ('pizza','fries','wings','meatballs','salad\n')

for food in buffet_foods:
    print(food)

#If you want to alter a tuple you have to reassign a new one to the variable:

buffet_foods = ('pizza','hashbrowns','wings','meatballs','salad\n')

for food in buffet_foods:
    print(food)

    
#Intentionally creating error to demonstrate that tuples are immutable lists

buffet_foods[0] = 'hotdog'