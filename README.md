# Youtube to MP3
A simple application to handle downloading a list of youtube videos or playlists as MP3 files.

Additional functionality to set MP3 metadata and rename those files once they have been downloaded.

<img src='resources/Screenshot.png' width='500'>

### Application
There are two ways to run the application.
 1. Run the python code through the command line directly with `python YTMP3.py`
 2. Run the [YTMP3.exe](dist/YTMP3.exe) executable. This is a standalone file and can be downloaded directly from github, it does not require the rest of the repo to function (simply navigate to the file and click `download`)

### Requirements:
These requirements are *only* required for running the application through the command line or building the executable through `build.bat`. They are *not* required for running the built `YTMP3.exe` executable.
  - yt-dlp: https://pypi.org/project/yt-dlp/ (`pip install yt-dlp`)
  - eyed3: https://eyed3.readthedocs.io/en/latest/ (`pip install eyed3`)
  - The ffmpeg executable needs to be added to `resources/`
    - There is a current build of ffmpeg in [resources/ffmpeg.zip](resources/ffmpeg.zip), unzip this and move `ffmpeg.exe` to `resources/`

### Usage
 - Copy and paste youtube video links into the input text box
   - These can take the form of the youtube shareable link (`https://youtu.be/<song_id>`) or full youtube watch links (`https://www.youtube.com/watch?<song_id>&<ignored_parameters>`)
   - Playlist links work, first the video IDs of each song are downloaded and then the MP3 downloads proceed for each song. Should take the form of `https://youtube.com/playlist?list=<playlist_id>`
 - Click `Start Download...`
 - As songs are downloaded you will be able to select them from the dropdown box to the right. Once a song is selected you can set its metadata and save it to the file.
   - For ease of use, if you tab through certain fields it will auto populate if the field is left empty:
      - Song Name auto populates to the Filename without file extensions
      - Artist auto populates to the last saved artist
      - Album auto populates to the last saved album
      - Hitting `Return` while in Track Number (the last entry field) will save the current song and load the next song (if available)

### Build
 - The attached `build.bat` batch script will construct an executable to use in `/dist`.
 - `/build` can be safely deleted after the build is complete.
 - Requires pyinstaller (`pip install pyinstaller`)

### Known Bugs:
 - Downloads can randomly fail with a `403 Not Found` error, retrying the download typically works. This is an issue with Youtube.
 - When downloading files through the built executable, ffmpeg will frequently open and close terminals when creating the mp3 if `--windowed` is set in the build script.
   - Mitigated for now by allowing the executable to open a terminal window, although its ugly and useless

### Eventual Roadmap:
 - Add songs to a download queue while a download is in progress
 - Fix the ffmpeg windowed issue
