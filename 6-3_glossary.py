# Exercise 6-3 from Python Crash Course Book
# Completed by Mack Sell

glossary = {
    'tuple': 'An immutable list.',
    'conditional expression': 'An expression that evaluates to True or False.',
    'immutable': 'Unable to be altered.',
    'PEP8': 'Python Enhancement Proposal 8'
    }

for word in glossary:
    print(f'{word.title()}:\n{glossary[word]}\n')
