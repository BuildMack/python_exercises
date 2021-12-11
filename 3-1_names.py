# Exercise 3-1 from Python Crash Course Book
# Completed by Mack Sell

# Lesson learned here: names.pop() modifies the saved list whereas the .strip() method does not alter a saved string

names = ["Jon", "Mel", "Conor"]

jon = names[0]

del names[0]

conor = names.pop()

print(jon)
print(conor)
print(names)

test = ".\tBob's your uncle\t."
print(test)

test.strip()
print(test)
