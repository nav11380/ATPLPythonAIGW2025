from Session11A import Song
from Session11B import PlayList

# main or driver file for the program

song1 = Song(
                track='1. Laal Pari', 
                artists='john, jennie', 
                album='Album1', 
                duration=4.5
            )
# print('[main] song1:', song1)

songs_play_list = PlayList()
songs_play_list.add(song=song1)
