# Exercise 8-8 from Python Crash Course Book
# Completed by Mack Sell

def make_albums(artist, album):
    music = {
        'artist': artist,
        'album': album,
        }
    return music

while True:
    
    artist = input('\nWhat artist did you have in mind? ')
    
    if artist == 'quit':
        break
    
    album = input('\nWhich album of theirs did you like? ')
    
    if album == 'quit':
        break
        
    else:
        print(f'\n{make_albums(artist, album)}')

