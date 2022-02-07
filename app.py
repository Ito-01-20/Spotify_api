import spotipy

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


# アーティストの総フォロワーを取得
def get_artist_follwers(artist_name):
    artist_id = getIdByArtist(artist_name)
    show_artist = spotify.artist(artist_id)["followers"]["total"]
    return show_artist


# アーティストalbum_id取得
def get_artist_album_id(album_name):
    album_id = spotify.albums(album_name)["id"]
    return album_id


if __name__ == "__main__":
    artist_id = getIdByArtist("King Gnu")
    results = spotify.artist_albums(artist_id, album_type='single', country='JP', limit=20)
    print(results["items"])