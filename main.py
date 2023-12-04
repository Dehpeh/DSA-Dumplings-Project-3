from heap_sort import heap_sort
from merge_sort import merge_sort
from timeit import default_timer as timer
import csv
import os
import glob
import subprocess


# function uses the spotdl library to download an mp3 file given a track's spotify url
def download_mp3_with_spotdl(song_url):
    try:
        # use subprocess to run spotdl CLI to download the mp3 file
        subprocess.run(["spotdl", song_url])
        return True
    except subprocess.CalledProcessError:  # download error
        return False


# main function called by app.py to parse the CSV file, compare sorts, and select 10 songs for the quiz
def main(region, sort_metric):
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

    # read first 100,000 entries in the CSV file
    count = 0
    songs = []  # stores the CSV file entries
    # open the CSV file
    with open('charts.csv', newline='') as song_list:
        song_reader = csv.reader(song_list, delimiter=',')
        for row in song_reader:
            if count > 0 and row[param_dict["region"]] == region:  # ignore the row with attribute titles
                songs.append(row)
            count += 1
            if count > 100000:  # stop reading after 100,000 entries
                break

    # time heap sort
    start_heap = timer()
    ten_songs = heap_sort(songs, sort_metric)
    end_heap = timer()
    heap_time = (end_heap - start_heap)

    # time merge sort
    start_merge = timer()
    merge_sort(songs, sort_metric)
    end_merge = timer()
    merge_time = (end_merge - start_merge)

    ten_files = []
    # heap and merge sort should return same results, use heap sort result to download mp3 files
    for entry in ten_songs:
        download_mp3_with_spotdl(entry[1])  # download mp3 using spotify url
        # change file names and move to static/mp3 directory
        list_of_files = glob.glob("/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/*")
        latest_file = max(list_of_files, key=os.path.getctime)
        splice_index = latest_file.find("-3/") + 3
        file_name = latest_file[splice_index:]
        os.rename(f"/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/{file_name}",
                  f"/Users/rachelyoung/PycharmProjects/COP3530Project3/DSA-Dumplings-Project-3/static/mp3/{file_name}")
        ten_files.append((entry[0], file_name))

    # add merge and heap sort run times to the list to be returned
    ten_files.append((f'Merge Sort Run-time: {merge_time} s', f'Heap Sort Run-time: {heap_time} s'))
    for file in ten_files:
        print(' || '.join(file))

    return ten_files


if __name__ == "__main__":
    main("Mexico", "title")
