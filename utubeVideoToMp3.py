
from pytube import YouTube

# pip install moviepy
# pip install pytube
# pip install python-vlc
import os
from mymodule import *



url = 'https://www.youtube.com/watch?v='+'27Gqgxoka2o'
newTitle = "莫問歸期"
yt = YouTube(url, proxies={'http': 'http://10.62.220.124:9080'})
print(yt.streams.filter(type="video")[0])
saveFolder = 'd:\\mp4\\'
oldFileName = saveFolder + newTitle + ".mp4"
# 下载mp4音频
xx = yt.streams.filter(
    type="video", mime_type="video/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")
convertToMp3(oldFileName)
# os.remove(oldFileName)
