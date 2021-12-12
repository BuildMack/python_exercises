# Exercise 3-8 from Python Crash Course Book
# Completed by Mack Sell

places = ['Paris','Interlaken','Lake Como','Budapest','South Korea','Japan']

print('\nUsing sorted() function is not permanent:\n')

print(places)

print(sorted(places))

print(places)

print(sorted(places, reverse = True))

print(places)

print('\nReverse original then reverse back:\n')

places.reverse()

print(places)

places.reverse()

print(places)

print('\nUsing sort() method is permanent():\n')

places.sort()

print(places, end = '\n\n')

places.sort(reverse = True)

print(places)