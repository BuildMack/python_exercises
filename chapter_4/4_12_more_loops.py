# Exercise 4-12 from Python Crash Course Book
# Completed by Mack Sell

my_favorite_foods = ['pizza','cheesecake','burgers']

my_friends_favorite_foods = my_favorite_foods[:]

my_favorite_foods.append('potatoes')

my_friends_favorite_foods.append('pasta')

print("My favourite foods are:")
for food in my_favorite_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in my_friends_favorite_foods:
    print(food)    
