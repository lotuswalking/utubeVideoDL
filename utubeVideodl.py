# importing the module
from pytube import YouTube
from moviepy.editor import *
import os
# pip install moviepy
# pip install pytube
# pip install python-vlc

def charReplace(inStr):
    replacement=["@","_","(",")","|","-","/",":","《","》","：","“"," ",'"','（','）']
    for char in replacement:
        inStr = inStr.replace(char,"")
    return inStr
# https://www.youtube.com/watch?v=yoZJWWrGbi4
# YouTube('https://www.youtube.com/watch?v=PjvU9xUw_XY').streams.first().download()
url = 'https://www.youtube.com/watch?v='+'v5Vq62nS-5U'
yt = YouTube(url)
print(yt.streams.filter(type="video").order_by("abr").desc.first())
saveFolder = 'd:\\mp4\\'
oldFileName = saveFolder + charReplace(yt.title)+".mp4"
# 下载mp4音频
xx = yt.streams.filter(
    type="video", mime_type="video/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")

