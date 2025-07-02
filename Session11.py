from Session11A import Song
from Session11B import PlayList

"""
    # FOR INTERVIEW PREP OF TIER1 COMPANIES
    1. DESIGN PATTERNS
    https://refactoring.guru/design-patterns
    
    2. SOLID PRINCIPLES
    https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design
"""

# main or driver file for the program

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

song4 = Song(
                track='4. Hi Hello', 
                artists='george, ben', 
                album='Album2', 
                duration=6.2
            )

song5 = Song(
                track='5. Thank You', 
                artists='george, ben', 
                album='Album3', 
                duration=6.2
            )

# print('[main] song1:', song1)

songs_play_list = PlayList()

songs_play_list.add(song=song1)
songs_play_list.add(song=song2)
songs_play_list.add(song=song3)
songs_play_list.add(song=song4)
songs_play_list.add(song=song5)


# songs_play_list.iterate_forward()
# songs_play_list.iterate_backward()
# songs_play_list.iterate()
songs_play_list.iterate(direction=1)


"""

    HW: (Mandatory)
    Class1: WhatsAppMessage: text, sender, receiver, status
    Class2: WhatsAppMessageList: head, tail, size (Doubly LinkedList)
            here, follow the same session11, 11A, 11B
            only head and tail will not refer to each other


"""