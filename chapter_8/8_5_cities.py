# Exercise 8-5 from Python Crash Course Book
# Completed by Mack Sell

def describe_cities(city, country = 'united states of america'):
    print(f"{city.title()} is in {country.title()}!")

describe_cities('Oklahoma')

describe_cities('New York')

describe_cities('Toronto', 'Canada')
