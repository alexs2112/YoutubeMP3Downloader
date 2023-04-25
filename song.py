import os, eyed3

class Song:
    def __init__(self, file, path):
        self.filename = file
        self.file = eyed3.load(os.path.join(path, file))

        self.last_artist = ""
        self.last_album = ""

        ext = self.filename.rsplit(".", 1)
        if len(ext) > 1:
            self.extension = ext[1]
        else:
            self.extension = ''

    def set_tag(self, tag, value):
        if tag == "artist": self.file.tag.artist = value
        elif tag == "album": self.file.tag.album = value
        elif tag == "title": self.file.tag.title = value
        elif tag == "track_num": self.file.tag.track_num = value
        else: raise Exception(f"Unknown song file tag: <{tag}>.")

    def get_tag(self, tag):
        if tag == "artist": v = self.file.tag.artist
        elif tag == "album": v = self.file.tag.album
        elif tag == "title": v = self.file.tag.title
        elif tag == "track_num": v = self.file.tag.track_num[0]
        else: raise Exception(f"Unknown song file tag: <{tag}>.")
        
        if v == None: return ""
        return v
    
    def sort_attributes(self):
        if self.extension != "mp3":
            return ("", "", -1)
        t = self.get_tag("track_num")
        if t == '': t = -1
        return (self.get_tag("artist"), self.get_tag("album"), t)

    def save_tags(self):
        self.file.tag.save()
