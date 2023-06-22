class Song:
    def __init__(self, data, track_num=None):
        self.type = "Song"
        self.title = data['title']
        self.artists = data['artists']
        self.album = data['album']
        self.id = data['videoId']
        self.duration = data['duration']
        self.track_num = track_num

# {'album': {'id': 'MPREb_qRk7I2P59dT', 'name': 'The Guilt & The Grief'},
#  'artists': [{'id': 'UCZx7OhOHYWiNBdBbCLBfxvg', 'name': 'Polaris'}],
#  'category': 'Songs',
#  'duration': '3:54',
#  'duration_seconds': 234,
#  'feedbackTokens': {'add': None, 'remove': None},
#  'isExplicit': True,
#  'resultType': 'song',
#  'thumbnails': [{'height': 60,
#                  'url': 'https://lh3.googleusercontent.com/2Kn9Owg3W4G3-BlBoXC2Jq6bgnjWdxJ6WCAPvr3RJwUlAuJnWuplDWKmrDEOe_VxERaWjW0MibA01wpn=w60-h60-l90-rj',
#                  'width': 60},
#                 {'height': 120,
#                  'url': 'https://lh3.googleusercontent.com/2Kn9Owg3W4G3-BlBoXC2Jq6bgnjWdxJ6WCAPvr3RJwUlAuJnWuplDWKmrDEOe_VxERaWjW0MibA01wpn=w120-h120-l90-rj',
#                  'width': 120}],
#  'title': 'Voiceless',
#  'videoId': 'tX-0VIaicGI',
#  'videoType': 'MUSIC_VIDEO_TYPE_ATV',
#  'year': None}
