# Exercise 5-4 from Python Crash Course Book
# Completed by Mack Sell

alien_colors = ['yellow','green','red']

for alien_color in alien_colors:
    if alien_color.lower() == 'green':
        print('Green alien, you get 5 points!')
        
    else:
        print(f'{alien_color.title()} alien, you get 10 points')
