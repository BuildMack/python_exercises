# Exercise 6-11 from Python Crash Course Book
# Completed by Mack Sell

#Dictionaries nested in dictionaries

cities = {
    'toronto': {
        'population': 2_900_000,
        'country': 'Canada',
        'tallest building': 'CN Tower' 
        },
    'paris': {
        'population': 2_100_000 ,
        'country': 'France',
        'tallest building': 'Eiffel Tower' 
        },
    'new york': {
        'population': 8_400_000,
        'country': 'United States',
        'tallest building': 'One World Trade Centre'
        }
    }

for city, facts in cities.items():
    print(f'Did you know that {city.title()}...')
    print(f"\t-Has a population of {facts['population']} people")
    print(f"\t-Is located in {facts['country']}")
    print(f"\t-The largest building is {facts['tallest building']}\n")
