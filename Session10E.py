"""
    1. Song: track, artists, album, duration
"""

class Song:

    def __init__(self, track, artists, album, duration):
        self.track = track
        self.artists = artists
        self.album = album
        self.duration = duration
        self.next = None
        self.previous = None

    def show(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('Track:', self.track)
        print('Artists:', self.artists)
        print('Album:', self.album)
        print('Duration:', self.duration)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



song1 = Song(
                track='1. Laal Pari', 
                artists='john, jennie', 
                album='Album1', 
                duration=4.5
            )

song2 = Song(
                track='2. Zamaana Lage', 
                artists='harry, jennie', 
                album='Album1', 
                duration=3.5
            )

song3 = Song(
                track='3. Chor Bazaari', 
                artists='george, ben', 
                album='Album2', 
                duration=6.2
            )


# Linking of Objects with Each Other in next and previous form
# Hard Code
song1.next = song2
song2.next = song3
song3.next = song1

song1.previous = song3
song2.previous = song1
song3.previous = song2
