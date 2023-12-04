from heap_sort import heap_sort
from merge_sort import merge_sort
from timeit import default_timer as timer
import csv
import os
import glob
import subprocess


def download_mp3_with_spotdl(song_url):
    try:
        # using subprocess to run the spotdl command to download the song
        subprocess.run(["spotdl", song_url])
        return True
    except subprocess.CalledProcessError:  # download error
        return False


def main(region, sort_metric):
    param_dict = {"title": 0,
                  "rank": 1,
                  "date": 2,
                  "artist": 3,
                  "url": 4,
                  "region": 5,
                  "chart": 6,
                  "trend": 7,
                  "stream": 8}

    count = 0
    songs = []
    with open('charts.csv', newline='') as song_list:
        song_reader = csv.reader(song_list, delimiter=',')
        for row in song_reader:
            if count > 0 and row[param_dict["region"]] == region:  # ignore the row with attribute titles
                songs.append(row)
            count += 1
            if count > 100000:  # arbitrary stopping point in dataset traversal, >100,000 datapoints
                break

    start_heap = timer()
    ten_songs = heap_sort(songs, sort_metric)
    end_heap = timer()
    heap_time = (end_heap - start_heap)

    start_merge = timer()
    merge_sort(songs, sort_metric)
    end_merge = timer()
    merge_time = (end_merge - start_merge)

    ten_files = []
    print(len(ten_songs))
    for entry in ten_songs:
        download_mp3_with_spotdl(entry[1])
        print(entry[1])
        list_of_files = glob.glob("/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/*")
        latest_file = max(list_of_files, key=os.path.getctime)
        splice_index = latest_file.find("-3/") + 3
        file_name = latest_file[splice_index:]
        os.rename(f"/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/{file_name}",
                  f"/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/static/mp3/{file_name}")
        ten_files.append((entry[0], file_name))

    ten_files.append((f'Merge Sort Run-time: {merge_time} s', f'Heap Sort Run-time: {heap_time} s'))
    for file in ten_files:
        print(' || '.join(file))
    return ten_files


if __name__ == "__main__":
    main("Mexico", "title")
