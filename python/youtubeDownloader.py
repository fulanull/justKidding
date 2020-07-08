#Function to download videos from youtube
from pytube import YouTube, Stream




def downloadVideo(url, filename = None, filename_prefix = None):
    yt = YouTube(url)
    print(filename_prefix, filename)
    yt.streams.get_highest_resolution().download(output_path="downloaded", filename=filename, filename_prefix=filename_prefix)





downloadVideo("https://youtu.be/1I-3vJSC-Vo", None, filename_prefix="02")