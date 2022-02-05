import spotipy


# 認証トークン
client_id = '55cd87a12b9e429498917ac04e0412d7'
client_secret = 'fe20d9c071684bc597d10dc2a4f4cc44'

# 認証情報
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# show_artist = spotify.artist("0hCWVMGGQnRVfDgmhwLIxq")
# print((show_artist))

# アーティストIDの取得
def getIdByArtist(artist_name):
    results = spotify.search(q="artist:" + artist_name, type="artist")
    items = results["artists"]["items"]
    artist = items[0]
    artist_id = artist["id"]
    return artist_id


result1 = getIdByArtist("King Gnu")
result2 = getIdByArtist("Vaundy")


def FollowersComparison(result1, result2):
    if result1["followers"]["total"] > result2["followers"]["total"]:
        print(result1["name"])
    else:
        print(result2["name"])

FollowersComparison(result1, result2)
