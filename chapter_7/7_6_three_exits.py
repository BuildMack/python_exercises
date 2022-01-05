# Exercise 7-6 from Python Crash Course Book
# Completed by Mack Sell

#Completing 7_5 in a different way

while True:

    message = "\nWhat is the age of person using the ticket?" \
              "\nEnter 'quit' to leave the program. "

    age = input(message)
    
    if age.lower() == 'quit':
        break
    
    try: 
        age = int(age)
    except ValueError:
        print('\nThis is not a valid entry.')
        break
    if age < 3:
        cost = 'free'
    elif 3 <= age <= 12:
        cost = '$10'
    elif age > 12:
        cost = '$15'

    print(f'\nYour ticket will be {cost}.')
