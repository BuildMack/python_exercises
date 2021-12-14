# Exercise 5-10 from Python Crash Course Book
# Completed by Mack Sell


current_users = ['jonsnow', 'JamesBond', 'maTT', 'Bob','brooke']

#Used a list comprehension to change all values in list to lowercase
current_users_lowercase = [ user.lower() for user in current_users]

print(current_users)

new_users = ['BRooke','Leon','Matt']

#This is case insensitive...it does not differnetiate between JOHN and john

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f'Sorry the username {new_user} is taken. Choose another.')
    else:
        print(f'The username {new_user} is available.')
        current_users.append(new_user)
        current_users_lowercase.append(new_user.lower())
