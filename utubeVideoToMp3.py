from pytube import YouTube

# pip install moviepy
# pip install pytube
# pip install python-vlc
import os
from mymodule import *


# https://www.youtube.com/watch?v=yoZJWWrGbi4
# YouTube('https://www.youtube.com/watch?v=PjvU9xUw_XY').streams.first().download()
url = 'https://www.youtube.com/watch?v='+'2aBNmb4m9eg'
yt = YouTube(url)
print(yt.streams.filter(type="video")[0])
saveFolder = 'd:\\mp4\\'
oldFileName = saveFolder + charReplace(yt.title)+".mp4"
# 下载mp4音频
xx = yt.streams.filter(
    type="video", mime_type="video/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")
convertToMp3(oldFileName)
