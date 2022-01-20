# Exercise 8-6 from Python Crash Course Book
# Completed by Mack Sell

def describe_cities(city, country = 'united states of america'):
    #place = city + ', ' + country.title()
    return city + ', ' + country.title()

print(describe_cities('Oklahoma'))

print(describe_cities('New York'))

print(describe_cities('Toronto', 'Canada'))
