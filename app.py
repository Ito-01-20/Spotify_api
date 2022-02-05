import spotipy
import pprint

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


def getTopSongs(artist_name):
    num = 10  # 調べたい楽曲数(最大10)
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




# アーティストの楽曲一覧を取得する
# results = spotify.artist_albums(artist_id, album_type='single', country='JP', limit=20)


# artist_songs = []
# for song in results['items'][:len(results)]:
#     data = [
#         '曲名：' + song['name'],
#         '発売日：' + song['release_date'],
#         'id：' + song['id']]
#     artist_songs.append(data)
# pprint.pprint(artist_songs)



if __name__ == "__main__":
    getTopSongs("King Gnu")