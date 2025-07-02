class Song:

    def __init__(self, track='NA', artists='', album='', duration=0):
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