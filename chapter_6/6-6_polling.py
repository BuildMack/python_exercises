# Exercise 6-6 from Python Crash Course Book
# Completed by Mack Sell

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'george': 'ruby',
    'phil': 'pyton'
    }

people = ['carl','steve','sarah','jen']

for person in people:
    if person in favorite_languages.keys():
            print(f'\n{person.title()}, thank you for already completing this poll.')
            print(f'Your favourite language is: {favorite_languages[person]}')
    
    else:
        print(f'\n{person.title()}, would you please take this poll?')
        