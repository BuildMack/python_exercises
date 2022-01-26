conversation = [
    'hi', 'hey','how are you?', 'good, hbu?', 
    'great, want to meet at 5?', 'yes, sounds good!'           
    ]

def send_messages(texts):
    print('This is your conversation:')
    sent_texts=[]
    while texts:
        text = texts.pop(0)
        print(text)
        sent_texts.append(text)
    return sent_texts

# Uses the [:] splice to pass a copy of the original list in order to preserve it
print(send_messages(conversation[:]))

print('\nAs you can see the original list is still preserved:')
print(conversation)