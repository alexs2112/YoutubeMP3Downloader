class Album:
    def __init__(self, data):
        self.type = "Album"
        self.title = data['title']
        self.artists = data['artists']
        self.year = data['year']
        self.id = data['audioPlaylistId']
        self.track_count = data['trackCount']
        self.tracks = data['tracks']
        self.single = data['type'] == 'Single'

# {'artists': [{'id': 'UCRXmX2WJFd_VYDk3Iiu_N0w', 'name': 'Hickory Project'}],
#  'audioPlaylistId': 'OLAK5uy_ndztS_V4Gs2ftHafeQ2udqp5xhG17bjoU',
#  'duration': '56 minutes',
#  'duration_seconds': 3390,
#  'thumbnails': [{'height': 60,
#                  'url': 'https://lh3.googleusercontent.com/TB-qFEPtgdOazwIFbffwUBuaMo5gGV29MWTKCukwr9Rd40za4zmu1UMOHVgCKbf29uFhkfTxgDOsf2wy=w60-h60-l90-rj',
#                  'width': 60},
#                 {'height': 120,
#                  'url': 'https://lh3.googleusercontent.com/TB-qFEPtgdOazwIFbffwUBuaMo5gGV29MWTKCukwr9Rd40za4zmu1UMOHVgCKbf29uFhkfTxgDOsf2wy=w120-h120-l90-rj',
#                  'width': 120},
#                 {'height': 226,
#                  'url': 'https://lh3.googleusercontent.com/TB-qFEPtgdOazwIFbffwUBuaMo5gGV29MWTKCukwr9Rd40za4zmu1UMOHVgCKbf29uFhkfTxgDOsf2wy=w226-h226-l90-rj',
#                  'width': 226},
#                 {'height': 544,
#                  'url': 'https://lh3.googleusercontent.com/TB-qFEPtgdOazwIFbffwUBuaMo5gGV29MWTKCukwr9Rd40za4zmu1UMOHVgCKbf29uFhkfTxgDOsf2wy=w544-h544-l90-rj',
#                  'width': 544}],
#  'title': 'Polaris',
#  'trackCount': 18,
#  'tracks': [{'album': 'Polaris',
#              'artists': [{'id': 'UCRXmX2WJFd_VYDk3Iiu_N0w',
#                           'name': 'Hickory Project'}],
#              'duration': '1:56',
#              'duration_seconds': 116,
#              'isAvailable': True,
#              'isExplicit': False,
#              'likeStatus': 'INDIFFERENT',
#              'thumbnails': None,
#              'title': 'Icy Roads',
#              'videoId': '74PsnzzJRBQ',
#              'videoType': 'MUSIC_VIDEO_TYPE_ATV'},
#             ...
#             {'album': 'Polaris',
#              'artists': [{'id': 'UCRXmX2WJFd_VYDk3Iiu_N0w',
#                           'name': 'Hickory Project'}],
#              'duration': '5:35',
#              'duration_seconds': 335,
#              'isAvailable': True,
#              'isExplicit': False,
#              'likeStatus': 'INDIFFERENT',
#              'thumbnails': None,
#              'title': 'Polaris',
#              'videoId': '5cRDynycWdo',
#              'videoType': 'MUSIC_VIDEO_TYPE_ATV'}],
#  'type': 'Album',
#  'year': '2001'}
