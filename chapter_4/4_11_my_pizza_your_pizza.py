# Exercise 4-11 from Python Crash Course Book
# Completed by Mack Sell

#THE [:] IS VERY IMPORTANT IN MAKING A SEPERATE COPY OF A LIST
#IF YOU DON'T THE TWO VARIABLES WILL BE POINTING TOWARDS THE SAME PLACE!!!

my_favorites = ['peperoni','margarita','cheese']

my_friends_favorites = my_favorites[:]

my_favorites.append('mozarella')

my_friends_favorites.append('pineapple')

print("My favourite pizzas are:")
for pizza in my_favorites:
    print(pizza)

print("\nMy friend's favourite pizzas are:")
for pizza in my_friends_favorites:
    print(pizza)    
