# class CircularDoublyLinkedList:

class PlayList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # add is going to add a song in the linked list
    def add(self, song):
        # print('[PlayList][add] song:', song)
        if self.head == None:
            self.head = song
            self.tail = song
            self.size += 1
        else:
            self.size += 1
            self.tail = song


"""
songs_play_list = PlayList()
# songs_play_list.head = None
# songs_play_list.tail = None
# songs_play_list.size = 0


print('songs_play_list:', songs_play_list)
print('songs_play_list data: ', vars(songs_play_list))
"""