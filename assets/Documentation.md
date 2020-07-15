# YouTube Helper

A GUI wrapper for <a href="https://github.com/ytdl-org/youtube-dl" target="_blank">YouTube-dl</a>.

### Functionalities:

- Perform YouTube searches
- Drag and Drop or Paste (Ctrl+V) into the GUI to import links
- Supported site links follow that of <a href="https://ytdl-org.github.io/youtube-dl/supportedsites.html" target="_blank">YouTube-dl</a>
- Select streams for downloading

### FFMPEG Post Processing

For postprocessing such as merging of DASH audios and videos or converting to other formats,

the <a href="https://ffmpeg.org/" target="_blank">ffmpeg</a> libraries will be required.

- For Windows, download from the following link:

<a href="https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.3-win64-static.zip" target="_blank">https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-4.3-win64-static.zip</a>

and either extract ffmpeg.exe to this folder or add to path

- For MacOS, install via brew:

```brew install ffmpeg```

- For Ubuntu, install via apt-get:

```sudo apt install ffmpeg```

Run the program via
```python main.py```

### YouTube API Key

In order to perform YouTube searches, please obtain an API Key for the YouTube Data API as follows:

1. Go to <a href="https://console.developers.google.com/" target="_blank">https://console.developers.google.com/</a> and create a project under your Google account.
2. Click on the ```+ Enable API and Servies``` link.
3. Select the ```YouTube Data API v3``` and enable this API.
4. Click on ```Create credentials``` and create an API Key.
5. Save your API Key into ```api_key.txt``` in this folder.
