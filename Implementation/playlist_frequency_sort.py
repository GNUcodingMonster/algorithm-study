def solution(playlists):
    freq_map={}
    first_apperance={}
    apperance_order = 0

    for i, song in enumerate(playlists):
        songs = playlists.split()

        for song in songs:
            freq_map[song] = freq_map.get(song, 0) + 1
            
            if song not in first_apperance:
                first_apperance[song] = apperance_order
                apperance_order += 1

    unique_songs = list(freq_map.keys())

    unique_songs.sort(key = lambda x:(-freq_map[x],first_apperance[x]))

    return "".join(unique_songs)


