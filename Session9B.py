"""
    1. Think of an Object
    Song: name, artists, album, duration

    Song is an Object
    name, artists, album, duration are attributes or data or variable inside the object

"""

# 2. Create its class
class Song:
    
    def __init__(self):
        print('constructor executed')
        print('self:', self, type(self), id(self))


# 3. Create Object from Class Definition
# johns_song: is not object. It is a REFERENCE VARIABLE (Stack Area)
# It will hold hashcode of the object in memory
# Song(): creating an object in RAM (Heap Area)
johns_song = Song()
print('johns_song:', johns_song, type(johns_song), id(johns_song))

print('Data in Object Referred by johns_song')
print(vars(johns_song))

# Write Data in Object
# name, artists, album, duration
johns_song.name = 'Laal Pari'
johns_song.artists = 'Yo Yo Honey Singh, Simar Kaur, Alfaaz'
johns_song.album = 'Housefull 5'
johns_song.duration = 4.16

print('Data in Object now:')
print(vars(johns_song))


