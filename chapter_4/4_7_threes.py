# Exercise 4-7 from Python Crash Course Book
# Completed by Mack Sell

#List Comprehension Way:
multiples_of_three = [3*value for value in range(3,30)]

#Longer Way:

multiples_of_three_V2 = []

for value in range(3,30):
    multiples_of_three_V2.append(value*3)

for value in multiples_of_three:
    print(value)


