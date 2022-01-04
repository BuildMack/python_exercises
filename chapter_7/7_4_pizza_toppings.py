# Exercise 7-4 from Python Crash Course Book
# Completed by Mack Sell

#Initialize variables
active = True
toppings = []

#When 'quit' is entered flag is changed to false and the program exits
while active:
    topping_input = input("""\nEnter the toppings that you want one at a time.
When you are done enter 'quit'.
What topping would you like? """)

    if topping_input.lower() == 'quit':
        print("\nThe toppings you've selected for your pizza are:")

        for topping in toppings:
            print(f'\t-{topping}')

        active = False
    else:
        toppings.append(topping_input.title())
        print(f"\nYou've successfully added {topping_input.lower()}",
        "to your pizza!\n")