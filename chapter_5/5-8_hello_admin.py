# Exercise 5-8 from Python Crash Course Book
# Completed by Mack Sell

usernames = ['jonsnow', 'jamesbond24', 'admin', 'bob']

for user in usernames:
    if user == 'admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, glad you logged back in!')