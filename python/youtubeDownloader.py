#Function to download videos from youtube
from pytube import YouTube, Stream


def show_progress_bar(stream: Stream, chunk: bytes, bytes_remaining: int):
# def show_progress_bar(stream, chunk, file_handler, bytes_remaining):
    print("Oi:", bytes_remaining )
    return

def downloadVideo(url, filename = None, filename_prefix = None):
    yt = YouTube(url)
    yt.register_on_progress_callback(show_progress_bar)
    print(filename_prefix, filename)
    yt.streams.get_highest_resolution().download(output_path="downloaded", filename=filename, filename_prefix=filename_prefix)





downloadVideo("https://youtu.be/1I-3vJSC-Vo", None, filename_prefix="02")