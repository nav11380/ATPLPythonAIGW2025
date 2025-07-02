# class CircularDoublyLinkedList:

class PlayList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a song in the linked list
    def add(self, song):
        self.size += 1
        # print('[PlayList][add] song:', song)
        if self.head == None:
            self.head = song
            self.tail = song
        else:
            self.tail.next = song
            song.previous = self.tail
            song.next = self.head
            self.head.previous = song
            self.tail = song

    """
    def iterate_forward(self):
        song = self.head
        song.show()
        while song.next != self.head:
            song = song.next
            song.show()

    def iterate_backward(self):
        song = self.tail
        song.show()
        while song.previous != self.tail:
            song = song.previous
            song.show()
    """

    def iterate(self, direction=0):

        if direction == 0:
            song = self.head
            song.show()
            while song.next != self.head:
                song = song.next
                song.show()
        else:
            song = self.tail
            song.show()
            while song.previous != self.tail:
                song = song.previous
                song.show()


"""
songs_play_list = PlayList()
# songs_play_list.head = None
# songs_play_list.tail = None
# songs_play_list.size = 0


print('songs_play_list:', songs_play_list)
print('songs_play_list data: ', vars(songs_play_list))
"""