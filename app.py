import spotipy

client_id = '55cd87a12b9e429498917ac04e0412d7'
client_secret = 'fe20d9c071684bc597d10dc2a4f4cc44'

client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


def getTopSongs(artist_name):
    num = 10
    try:
        search_id = getIdByArtist(artist_name)
        artist_top_tracks = spotify.artist_top_tracks(search_id, country="JP")["tracks"]

        print(artist_name + f" Top{num} Songs")

        for i in range(num):
            print(str(i + 1) + ". " + artist_top_tracks[i]["name"])

    except IndexError:
        print("IndexError has occurred!")
    except AttributeError:
        print("AttributeError has occurred!")


if __name__ == '__main__':
    getTopSongs(input("アーティストの名前を入力してください"))


