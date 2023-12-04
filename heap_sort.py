import heapq  # module performs min heap operations on a list


def heap_sort(data, sort_parameter) -> set:
    # dictionary to pair attribute names with their indices in a song entry
    param_dict = {"title":  0,
                  "rank":   1,
                  "date":   2,
                  "artist": 3,
                  "url":    4,
                  "region": 5,
                  "chart":  6,
                  "trend":  7,
                  "stream": 8}

    # swap sort_parameter with index 0 for heap building purposes
    for entry in data:
        entry[param_dict[sort_parameter]], entry[0] = entry[0], entry[param_dict[sort_parameter]]
    # update dictionary to reflect swap
    param_dict[sort_parameter], param_dict["title"] = param_dict["title"], param_dict[sort_parameter]

    # build min heap
    heapq.heapify(data)
    sorted_songs = []  # stores the sorted songs as they're extracted from the heap
    # load songs into sorted_songs list
    while True:
        try:
            song_entry = heapq.heappop(data)  # extract_min() from min heap
            # add song title and spotify url into sorted_songs
            sorted_songs.append((song_entry[param_dict["title"]],
                                 song_entry[param_dict["url"]]))
        except IndexError:  # reached end of the data
            break

    ten_songs = set()  # stores the 10 songs selected from sorted_songs for the quiz (no duplicates)
    i = 0
    while len(ten_songs) < 10:  # keep adding songs until the set contains 10 songs
        ten_songs.add(sorted_songs[i])
        i += 1

    return ten_songs
