import tkinter, pprint
from ytmusicapi import YTMusic
from system.result import Result
from system.album import Album
from system.song import Song
from system.config import *

class Search:
    def __init__(self):
        self.top = None
        self.albums = []
        self.songs = []
        self.results = []

        self.yt = YTMusic()
    
    def pack(self, frame):
        search_frame = tkinter.Frame(master=frame, bg=COLOUR_BACKGROUND)
        search_frame.pack()
        self.results_frame = tkinter.Frame(master=frame, bg=COLOUR_BACKGROUND)
        self.results_frame.pack()

        self.search = tkinter.Entry(master=search_frame, width=30, bg=COLOUR_FOREGROUND)
        self.search.focus()
        self.search.bind("<Return>", self.perform_search)
        self.search.pack(side=tkinter.LEFT)

        button = tkinter.Button(master=search_frame, text="Search", padx=10, pady=2)
        button.bind("<Button-1>", self.perform_search)
        button.pack(side=tkinter.RIGHT)
    
    def pack_results(self):
        if self.top != None:
            self.results.append(Result(self.top))
        for a in self.albums:
            self.results.append(Result(a))
        for s in self.songs:
            self.results.append(Result(s))

        for r in self.results:
            r.pack(self.results_frame)

    def perform_search(self, _):
        s = self.search.get().strip()
        if s == "": return

        self.clear_results()
        data = self.yt.search(s)

        albums = 0
        songs = 0
        for j in data:
            r = self.data_to_result(j)
            if r == None:
                continue

            if self.top == None:
                self.top = r
            elif r.type == "Album" and albums < MAX_ALBUMS:
                self.albums.append(r)
                albums += 1
            elif r.type == "Song" and songs < MAX_SONGS:
                self.songs.append(r)
                songs += 1
            
            if albums == MAX_ALBUMS and songs == MAX_SONGS:
                break

        self.pack_results()
    
    def data_to_result(self, entry):
        if 'resultType' not in entry: return None
        if entry['category'] == "Top result": return None

        try:
            if entry['resultType'] == "album":
                album = self.yt.get_album(entry['browseId'])
                return Album(album)
            elif entry['resultType'] == "song":
                return Song(entry)
            else:
                return None
        except:
            pprint.pprint(entry)

    def clear_results(self):
        for r in self.results:
            r.destroy()
        self.top = None
        self.albums = []
        self.songs = []
        self.results = []
    
    def get_youtube_links(self):
        out = []
        for r in self.results:
            if not r.selected: continue
            data = r.result
            if data.type == "Song":
                out.append(f"https://music.youtube.com/watch?v={data.id}")
            elif data.type == "Album":
                for s in data.tracks:
                    out.append(f"https://music.youtube.com/watch?v={s['videoId']}")
        return out
