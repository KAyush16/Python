from nested_data_tuples import albums  
while( True ):
    print("Plead choose your album (invalid choice exists):")
    # for index,(title,artist,year,songs) in enumerate(albums):
    #     print("{}: {}, {}, {}, {}"
    #             .format(index+1,title, artist,year,songs))
    # break    

    for index,(title,artist,year,songs) in enumerate(albums): # iterate within the albums list 
        print("{}: {}".format(index+1, title))# printing albums list 
        
    choice=int(input())# input of the choice 
    if 1<=choice<=len(albums):
        songs_list=albums[choice-1][3] # assigning songs_list to the albums songs 
    else:
        break
    
    print("Please choose the Songs from the Album: ")
    for index, (track_number,song) in enumerate(songs_list): # printing songs name 
        print("{}: {}".format(index+1,song)) # printing songs list
        
    song_choice=int(input()) # entering the songs list we want 
    if 1<=song_choice<=len(songs_list):
        title=songs_list[song_choice-1][1]
    else:
        break
    
    print("Playing {}".format(title))
    print("="*40)
    break

