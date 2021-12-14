# Exercise 5-6 from Python Crash Course Book
# Completed by Mack Sell

age = 35

if age < 2:
    group = 'baby'

elif age < 4:
    group = 'toddler'

elif age < 13:
    group = 'kid'

elif age < 20:
    group = 'teenager'

elif age < 65:
    group = 'adult'

elif age >= 65:
    group = 'elder'

print(f"You are a {group}!")
