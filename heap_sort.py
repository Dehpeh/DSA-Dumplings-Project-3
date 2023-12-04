import heapq


def heap_sort(data, sort_parameter) -> set:
    param_dict = {"title":  0,
                  "rank":   1,
                  "date":   2,
                  "artist": 3,
                  "url":    4,
                  "region": 5,
                  "chart":  6,
                  "trend":  7,
                  "stream": 8}

    # move sort_parameter to index 0 for heap building purposes
    for entry in data:
        entry[param_dict[sort_parameter]], entry[0] = entry[0], entry[param_dict[sort_parameter]]
    # update dictionary to reflect swap
    param_dict[sort_parameter], param_dict["title"] = param_dict["title"], param_dict[sort_parameter]

    heapq.heapify(data)  # build min heap
    sorted_songs = []  # stores the sorted songs as they're extracted from the heap
    while True:
        try:
            song_entry = heapq.heappop(data)
            sorted_songs.append((song_entry[param_dict["title"]],
                                 song_entry[param_dict["url"]]))
        except IndexError:
            break

    ten_songs = set()

    i = 0
    while len(ten_songs) < 10:
        ten_songs.add(sorted_songs[i])
        i += 1

    return ten_songs
