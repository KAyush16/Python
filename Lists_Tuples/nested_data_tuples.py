# Tuples Containg a List of Tuples 

        # 0th indexing
albums = [ 
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    # 1th indexing
    ("Bad Company", "Bad Company", 1974,
     [  
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    # 2nd indexing
    ("Nightflight", "Budgie", 1981,
     [  
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    #3rd indexing 
    ("More Mayhem", "Imelda May", 2011,
     [  # a list of tuples  
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
'''
for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}"
          .format(name, artist, year, songs))

print()

album = albums[2]
print(album)

songs = album[3]
print(songs)

song = songs[1]
print(song)
print(song[1])

'''
