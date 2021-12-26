# Exercise 6-6 from Python Crash Course Book
# Completed by Mack Sell

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'george': 'ruby',
    'phil': 'pyton'
    }

people = ['carl','steve','sarah','jen']

for person in people:
    for pollTaker in favorite_languages:
        if person == pollTaker:
            print('Thank you for already completing this poll.')
            print(f'Your favourite language is: {favorite_languages[person]}')
        
        break
    
    print(f'{person}, would you please take this poll?')
        