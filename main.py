from heap_sort import heap_sort
from merge_sort import merge_sort
import csv
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

    ten_songs = heap_sort(songs, sort_metric)
    print(len(ten_songs))
    for entry in ten_songs:
        download_mp3_with_spotdl(entry[2])
        print(' || '.join(entry))


if __name__ == "__main__":
    main("Argentina", "artist")
