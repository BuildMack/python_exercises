# Exercise 6-2 from Python Crash Course Book
# Completed by Mack Sell

favourite_numbers = {
    'Sharon': 16,
    'Dan': 2,
    'Curtis': 31, 
    'Mitchell': 24
    }

for favourite_number in favourite_numbers:
    print(f"{favourite_number}'s favourite number", 
    f"is: {favourite_numbers[favourite_number]}")