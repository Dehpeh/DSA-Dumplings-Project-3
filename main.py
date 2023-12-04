from heap_sort import heap_sort
from merge_sort import merge_sort
import csv
import subprocess

'''
function to download mp3 files from spotify url,
inspired by: https://codepal.ai/code-generator/query/qojNFO2Y/python-spotify-download-mp3-spotdl
'''
def download_mp3_with_spotdl(song_url):
    try:
        # using subprocess to run the spotdl command to download the song
        subprocess.run(["spotdl", song_url])
        return True
    except subprocess.CalledProcessError:  # download error
        return False


def main():
    count = 0
    songs = []
    with open('charts.csv', newline='') as song_list:
        song_reader = csv.reader(song_list, delimiter=',')
        for row in song_reader:
            if count > 0:  # ignore the row with attribute titles
                songs.append(row)
            # print(' || '.join(row))
            count += 1
            if count > 101734:  # arbitrary stopping point in dataset traversal, >100,000 datapoints
                break

    print(len(songs))
    print(print(' || '.join(songs[101733])))


    '''
    # sample data for testing
    heap = [
        ["Chantaje", 1, "2017-01-01", "Shakira", "https://open.spotify.com/track/6mICuAdrwEjh6Y6lroV2Kg",
         "Argentina", "top200", "SAME_POSITION", 253019],
        ["Vente Pa' Ca", 2, "2017-01-01", "Ricky Martin", "https://open.spotify.com/track/7DM4BPaS7uofFul3ywMe46",
         "Argentina", "top200", "MOVE_UP", 223988],
        ["Reggaetón Lento (Bailemos)", 3, "2017-01-01", "CNCO", "https://open.spotify.com/track/3AEZUABDXNtecAOSC1qTfo",
         "Argentina", "top200", "MOVE_DOWN", 210943],
        ["Safari", 4, "2017-01-01", "J Balvin, Pharrell Williams, BIA, Sky", "https://open.spotify.com/track/6rQSrBHf7HlZjtcMZ4S4bO",
         "Argentina", "top200", "SAME_POSITION", 173865],
        ["Shaky Shaky", 5, "2017-01-01", "Daddy Yankee", "https://open.spotify.com/track/58IL315gMSTD37DOZPJ2hf",
         "Argentina", "top200", "MOVE_UP", 153956],
        ["Traicionera", 6, "2017-01-01", "Sebastian Yatra", "https://open.spotify.com/track/5J1c3M4EldCfNxXwrwt8mT",
         "Argentina", "top200", "MOVE_DOWN", 151140],
        ["Cuando Se Pone a Bailar", 7, "2017-01-01", "Rombai", "https://open.spotify.com/track/1MpKZi1zTXpERKwxmOu1PH",
         "Argentina", "top200", "MOVE_DOWN", 148369],
        ["Otra vez (feat. J Balvin", 8, "2017-01-01", "Zion & Lennox", "https://open.spotify.com/track/3QwBODjSEzelZyVjxPOHdq",
         "Argentina", "top200", "MOVE_DOWN", 143004]
           ]

    songs = heap_sort(heap, "artist")
    # download_mp3_with_spotdl(songs[0][2])
    for entry in songs:
        download_mp3_with_spotdl(entry[2])
        # for attribute in entry:
        #     print(attribute, end=", ")
        # print()
    '''


if __name__ == "__main__":
    main()
