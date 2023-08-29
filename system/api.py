from ytmusicapi import YTMusic
import pprint

yt = YTMusic()

bid = None
search = yt.search(f"Silent Planet When the End Began")
pprint.pprint(search)


song = None
album = None
for res in search:
    if song == None and res['resultType'] == "song":
        song = res
    elif album == None and res['resultType'] == "album" and "browseId" in res:
        album = yt.get_album(res['browseId'])

# pprint.pprint(song)
# print('\n\n\n')
# pprint.pprint(album)

# album = yt.get_album(bid)
# print(f"{album['title']} - {album['year']}")
# if ('description' in album): print(album['description'])
# print(f"https://music.youtube.com/playlist?list={album['audioPlaylistId']}")

# i = 1
# for track in album['tracks']:
#     print(f"    {i}: {track['title']} - {track['duration']}")
#     print(f"         https://music.youtube.com/watch?v={track['videoId']}")
#     i += 1
