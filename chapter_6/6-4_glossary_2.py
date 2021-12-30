# Exercise 6-4 from Python Crash Course Book
# Completed by Mack Sell

glossary = {
    'tuple': 'An immutable list.',
    'conditional expression': 'An expression that evaluates to True or False.',
    'immutable': 'Unable to be altered.',
    'PEP8': 'Python Enhancement Proposal 8'
    }

for word, definition in glossary.items():
    print(f'{word.title()}:\n{definition}\n')

glossary['set'] = 'A mutable, unordered class (uses curly brackets).'

for word, definition in glossary.items():
    print(f'{word.title()}:\n{definition}\n')

