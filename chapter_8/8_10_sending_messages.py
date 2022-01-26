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

print(send_messages(conversation))

print(conversation)