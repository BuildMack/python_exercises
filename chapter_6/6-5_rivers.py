# Exercise 6-5 from Python Crash Course Book
# Completed by Mack Sell

rivers = {
    'nile': 'egypt',
    'mississipi river': 'usa',
    'yangtze river': 'china'
    }

for river, location in rivers.items():
    print(f"The {river.title()} is located in {location.title()}!")
    
print('\nAll the rivers included are:')
for river in rivers:
    print(f'\t{river.title()}')

print('\nAll the countries included are:')
for location in rivers.values():
    print(f'\t{location.title()}')