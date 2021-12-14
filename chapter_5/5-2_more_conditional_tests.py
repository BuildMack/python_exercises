# Exercise 5-2 from Python Crash Course Book
# Completed by Mack Sell

names = ['Tom','Greg','Bob','Tim','Joe','Fred']

active_users = ['Tim','George','Fred']

banned_users = ['Bob','Greg']

#Equal and not equal comparisons

print(names[0] == 'Tom')

print(names[0] == 'tom')

print(names[0] == 'tom'.title())

print(names[0] != names[1])

#In and not in

for name in names:
    if name in active_users:
        print(f'{name}, thanks for using our service!')

    elif name in banned_users:
        print(f'{name}, you are banned... go away!')

    elif name not in banned_users:
        print(f'{name}, please consider joining!')


#And & or

for name in names:
    if (len(name) == 3) and (name[0] == 'T'):
        print(name)
    
for name in names:
    if (len(name) == 3) or (name[0] == 'T'):
        print(name)


