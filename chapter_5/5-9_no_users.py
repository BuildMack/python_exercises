# Exercise 5-9 from Python Crash Course Book
# Completed by Mack Sell

#Showing that you can use if list_name: to verify that a list has content

usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, glad you logged back in!')
else:
    print('We need to find some users...')