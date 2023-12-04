from heap_sort import heap_sort
from merge_sort import merge_sort
import subprocess


def download_mp3_with_spotdl(song_url):
    """
    Downloads an MP3 file from Spotify using spotdl.

    Parameters:
    - song_url: str
        The URL of the Spotify song to be downloaded.

    Returns:
    - bool:
        True if the download was successful, False otherwise.
    """

    try:
        # Using subprocess to run the spotdl command to download the song
        # subprocess.run(["spotdl", "download", song_url, "mp3"], check=True)
        subprocess.run(["spotdl", song_url])
        return True
    except subprocess.CalledProcessError:
        # If an error occurs during the download, return False
        return False


def main():
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
    download_mp3_with_spotdl(songs[0][2])
    for entry in songs:
        for attribute in entry:
            print(attribute, end=", ")
        print()


if __name__ == "__main__":
    main()
