# Exercise 2-7 from Python Crash Course Book
# By Mack Sell

# Displays how the different strip methods deal with white spaces on the ends of strings

name = "\nKarl\t"
print(f".{name}.")
print(f".{name.lstrip()}.")
print(f".{name.rstrip()}.")
print(f".{name.strip()}.")
