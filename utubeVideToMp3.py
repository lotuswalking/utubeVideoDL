from pytube import YouTube
from moviepy.editor import *
# pip install moviepy
# pip install pytube
# pip install python-vlc
import os


def convertToMp3(oldFileName):

    newFileName = oldFileName.replace("mp4", "mp3")
    video = VideoFileClip(oldFileName)
    video.audio.write_audiofile(newFileName)


# https://www.youtube.com/watch?v=yoZJWWrGbi4
# YouTube('https://www.youtube.com/watch?v=PjvU9xUw_XY').streams.first().download()
url = 'https://www.youtube.com/watch?v='+'wgDYap0iJqk'
yt = YouTube(url)
print(yt.streams.filter(type="video")[0])
saveFolder = 'd:\\mp4\\'
oldFileName = saveFolder + \
    yt.title.replace(" ", "_").replace(":", "").replace(
        "|", "").replace("-", "")+".mp4"
oldFileName = oldFileName.replace("/", "")
# 下载mp4音频
xx = yt.streams.filter(
    type="video", mime_type="video/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")
convertToMp3(oldFileName)
