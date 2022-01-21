# Exercise 8-6 from Python Crash Course Book
# Completed by Mack Sell

def make_albums(artist, album, songs = None, year = None):
    music = {
        'artist': artist,
        'album': album,
        'number of songs': songs,
        'year': year
        }
    return music

print(make_albums('Prince','Purple Rain', 8))

print(make_albums('ACDC','Back in Black'))

print(make_albums('Led Zepplin','Mothership', year=1966))