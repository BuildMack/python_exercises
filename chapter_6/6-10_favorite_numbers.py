# Exercise 6-10 from Python Crash Course Book
# Completed by Mack Sell

favourite_numbers = {
    'Sharon': [16, 3],
    'Dan': [2, 6, 30],
    'Curtis': [31, 2, 5], 
    'Mitchell': [24,4]
    }



for favourite_number in favourite_numbers:
    print(f"\n{favourite_number}'s favourite numbers are:") 
    numbers = ''
    
    for number in favourite_numbers[favourite_number]:
        numbers += str(number) + " and "
    
    print(numbers[:-5])
    