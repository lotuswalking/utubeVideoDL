# importing the module
from pytube import YouTube
from pydub import AudioSegment
import os

# YouTube('https://www.youtube.com/watch?v=PjvU9xUw_XY').streams.first().download()
url = 'https://www.youtube.com/watch?v='+'SgOBUJnVERo'
yt = YouTube(url)
print(yt.streams)
saveFolder = 'd:\\mp3\\'
oldFileName = saveFolder+yt.title.replace(" ", "_")+".mp4"
newFileName = saveFolder+yt.title.replace(" ", "_")+".mp3"
# 下载mp4音频
xx = yt.streams.filter(
    type="audio", mime_type="audio/mp4").order_by("abr").desc().first()
xx.download(output_path=saveFolder, skip_existing=True,
            filename=oldFileName)
print("file "+oldFileName+" is done!")
sound = AudioSegment.from_file(oldFileName)
sound.export(newFileName, format='mp3')
os.remove(oldFileName)
print("file "+newFileName+" had been converted")

# 下载mp4视频
# yt.streams.filter(progressive=True,mime_type='video/mp4').order_by('resolution').desc().first().download(saveFolder)
