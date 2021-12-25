# Exercise 6-6 from Python Crash Course Book
# Completed by Mack Sell

rivers = {
    'nile': 'egypt',
    'mississipi river': 'usa',
    'yangtze river': 'china'
    }

for river in rivers:
    print(f"The {river.title()} is located in {rivers[river].title()}")

print('\nAll the rivers included are:')
for river in rivers:
    print(river.title())

print('\nAll the countries included are:')
for river in rivers:
    print(rivers[river].title())