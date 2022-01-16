# Exercise 8-3 from Python Crash Course Book
# Completed by Mack Sell

#Remember default arguments cannot come before non-default argumeny

def tshirt_order(tshirt_text, size = 'medium'):
    print(f'You ordered a {size.lower()} T-shirt that reads {tshirt_text}')

tshirt_order('Hello world!','large')

tshirt_order('BOOM!')

tshirt_order(size = 'S', tshirt_text='OPPOSITE!')

#Remember you cannot enter a positional argument after a keyword argument

#tshirt_order(size = 'S', 'OPPOSITE!') 