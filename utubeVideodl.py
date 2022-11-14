# importing the module
from pytube import YouTube
from moviepy.editor import *
import os
# pip install moviepy
# pip install pytube
# pip install python-vlc


def convertToMp3(subject):
    oldFileName = 'd:\\mp4\\'+subject+'.mp4'
    newFileName = 'd:\\mp3\\'+subject+'.mp3'
    video = VideoFileClip(oldFileName)
    video.audio.write_audiofile(newFileName)


# https://www.youtube.com/watch?v=yoZJWWrGbi4
# YouTube('https://www.youtube.com/watch?v=PjvU9xUw_XY').streams.first().download()
url = 'https://www.youtube.com/watch?v='+'a_7Z7C_JCyo'
yt = YouTube(url)
print(yt.streams.filter(type="video"))
saveFolder = 'd:\\mp4\\'
oldFileName = saveFolder+yt.title.replace(" ", "_")+".mp4"
newFileName = saveFolder+yt.title.replace(" ", "_")+".mp3"
# 下载mp4音频
xx = yt.streams.filter(
    type="video", mime_type="video/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")

