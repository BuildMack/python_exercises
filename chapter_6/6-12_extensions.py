# Exercise 6-12 from Python Crash Course Book
# Completed by Mack Sell

order_1 = {
    'crust': 'thin',
    'toppings': ['pinapple', 'pepperoni', 'sausage']
    }

order_2 = {
    'crust': 'thin',
    'toppings': ['pinapple', 'onions']
    }

order_3 = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'peppers']
    }

orders = [order_1, order_2, order_3]

for order in orders:
    print(f"\nYour pizza is number {orders.index(order)+1} in line!")
    print(f"You have ordered a {order['crust']} crust pizza with:")
    for topping in order['toppings']:
        
        print(f'\t{topping}')
