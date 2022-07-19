import spotipy

# 認証トークン
client_id = '55cd87a12b9e429498917ac04e0412d7'
client_secret = 'fe20d9c071684bc597d10dc2a4f4cc44'

# 認証情報
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# アーティストIDの取得
def get_artist_id(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


# アーティストの総フォロワーを取得
def get_artist_follwers(artist_name):
    artist_id = get_artist_id(artist_name)
    show_artist = spotify.artist(artist_id)["followers"]["total"]
    # return show_artist
    print(show_artist)


# アーティストのalbumsを全て取得
def get_artist_albums(artist_name):
    artist_id = get_artist_id(artist_name)
    album_numbers = spotify.artist_albums(artist_id)["items"]

    print(f"==========={artist_name} Albums===========")

    for i in range(len(album_numbers)):
        albums = spotify.artist_albums(artist_id)["items"][i]["name"]
        print(albums)


# アルバムのtracksを取得
def get_album_tracks(album_name):
    album_id = get_album_id(album_name)
    artist_tracks = spotify.album_tracks(album_id, market="JP")
    return artist_tracks


def get_album_id(album_name):
    album_id = spotify.search(q="album:" + album_name, type="album", market="JP")
    return album_id


if __name__ == "__main__":
   get_artist_follwers("King Gnu")
   get_artist_albums("Ado")

