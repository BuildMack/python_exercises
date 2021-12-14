# Exercise 5-5 from Python Crash Course Book
# Completed by Mack Sell

alien_colors = ['yellow','green','red']

for alien_color in alien_colors:
    if alien_color.lower() == 'green':
        points = 5
    
    elif alien_color.lower() == 'yellow':
        points = 10

    elif alien_color.lower() == 'red':
        points = 15

    print(f'{alien_color.title()} alien, you get {points} points!')
