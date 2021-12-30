# Exercise 6-10 from Python Crash Course Book
# Completed by Mack Sell

favourite_numbers = {
    'Sharon': [16, 3],
    'Dan': [2, 6, 30],
    'Curtis': [31, 2, 5], 
    'Mitchell': [24]
    }



for person, numbers in favourite_numbers.items():
    print(f"\n{person}'s favourite number", end = '') 
    fav_numbers = 's are '
    for number in numbers:
        #For the last number of multiple:
        if number == numbers[-1] and len(numbers) > 2:
            fav_numbers = fav_numbers + 'and ' + str(number) +'.'
        
        #For the last number when there are two:
        elif number == numbers[-1] and len(numbers) == 2:
            fav_numbers = fav_numbers[:-2] + ' and ' + str(number) +'.'
        
        #For when there is only one favourite number:
        elif len(numbers) == 1:
            fav_numbers =' is ' + str(number) + '.'

        #For multiple numbers aside from the last one:
        else:
            fav_numbers = fav_numbers + str(number) + ', '

    print(fav_numbers)
