# Youtube to MP3
A simple tkinter UI that handles downloading music from youtube videos or playlists as MP3 files.

Additional functionality to set MP3 metadata and rename those files once they have been downloaded.

![Screenshot](Screenshot.png)

### Usage
 - Run `YTMP3.py` through the command line (`python3 YTMP3.py`, I'll see about converting it to a working executable at some point, it has a bit of trouble with finding the working directory to save and edit files)
 - Copy and paste youtube video links into the input text box
   - These can take the form of the youtube shareable link (`https://youtu.be/<song_id>`) or full youtube watch links (`https://www.youtube.com/watch?<song_id>&<ignored_parameters>`)
   - Playlist links work, first the video IDs of each song are downloaded and then the MP3 downloads proceed for each song. Should take the form of `https://youtube.com/playlist?list=<playlist_id>`
 - Click `Start Download...`
 - As songs are downloaded you will be able to select them from the dropdown box to the right. Once a song is selected you can set its metadata and save it to the file.
   - For ease of use, if you tab through certain fields it will auto populate if the field is left empty:
      - Song Name auto populates to the Filename without file extensions
      - Artist auto populates to the last saved artist
      - Album auto populates to the last saved album

### Dependencies:
 - youtube_dl: https://pypi.org/project/youtube_dl/
 - eyed3: https://eyed3.readthedocs.io/en/latest/
 - ffmpeg needs to be added to your PATH: https://ffmpeg.org/

### Known Bugs:
 - Sometimes a youtube video download will randomly fail with a `403 Forbidden` error. It will keep track of each failure and paste the link at the bottom of the console logs once downloads are complete. You can retry the list afterwards and it will usually work on a second try. This is a problem with youtube.

### Eventual Roadmap:
 - Turn it into an executable file to save songs to a different directory
 - Multithreading to download multiple songs at once (requires big UI update to display progress differently)
 - Add songs to a download queue while a download is in progress
 - Refreshing songs sorts them by No Metadata (Alphabetical) -> Album (Alphabetical) -> Track Numbers
