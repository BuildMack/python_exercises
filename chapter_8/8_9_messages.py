# Exercise 8-9 from Python Crash Course Book
# Completed by Mack Sell

conversation = [
    'hi', 'hey','how are you?', 'good, hbu?', 
    'great, want to meet at 5?', 'yes, sounds good!'           
    ]

def display_conversation(texts):
    print('This was your conversation:\n')
    for text in texts:
        print(text)

display_conversation(conversation)