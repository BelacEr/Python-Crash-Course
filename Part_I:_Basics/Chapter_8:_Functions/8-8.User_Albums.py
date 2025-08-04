def make_album(artist: str, album: str, songs: int = None) -> dict:
    """Return a dictionary containing artist and album information."""
    music_album = {'artist': artist, 'album': album}
    if songs is not None:
        music_album['songs'] = songs
    return music_album

def get_album_info(include_songs: bool = False) -> dict:
    """Prompt user for album information and return as dictionary"""
    artist_name = input("Enter the artist name: ")
    album_name = input("Enter the album name: ")
    if include_songs:
        while True:
            try:
                songs_number = int(input("Enter the number of songs: "))
                return make_album(artist_name, album_name, songs_number)
            except ValueError:
                print("Please enter a valid number for songs.")
    return make_album(artist_name, album_name)

def main():
    """Main function to run the album information collection."""
    # First two albums without song count
    for _ in range(2):
        album = get_album_info()
        print(album)
    
    # Third album with song count
    album = get_album_info(include_songs=True)
    print(album)

if __name__ == "__main__":
    main()
