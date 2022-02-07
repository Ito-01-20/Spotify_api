import spotipy
import json

# 認証トークン
client_id = '55cd87a12b9e429498917ac04e0412d7'
client_secret = 'fe20d9c071684bc597d10dc2a4f4cc44'

# 認証情報
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# アーティストIDの取得
def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


# アーティストのalbumsを取得
def get_artist_albums(artist_name):
    artist_id = getIdByArtist(artist_name)
    album_numbers = spotify.artist_albums(artist_id)["items"]

    print(f"==========={artist_name} Albums===========")

    for i in range(len(album_numbers)):
        albums = spotify.artist_albums(artist_id)["items"][i]["name"]
        print(albums)



# アーティストの総フォロワーを取得
def get_artist_follwers(artist_name):
    artist_id = getIdByArtist(artist_name)
    show_artist = spotify.artist(artist_id)["followers"]["total"]
    return show_artist


if __name__ == "__main__":
    artist_albums = get_artist_albums("Vaundy")

