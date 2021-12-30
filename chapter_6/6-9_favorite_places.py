# Exercise 6-9 from Python Crash Course Book
# Completed by Mack Sell

favorite_places = {
    'john': ['Toronto', 'Detroit', 'Collingwood'],
    'iyana': ['Hawaii', 'Paris', 'New York'],
    'ryan': ['Kingston', 'Berlin', 'Geneva']
    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favourite places are:")
    for place in places:
        print(f'\t{place}')