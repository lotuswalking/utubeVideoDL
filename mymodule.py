from pytube import YouTube
from moviepy.editor import *

def charReplace(inStr):
    replacement = ["@", "_", "(", ")", "|", "-", "/", ":",
                   "《", "》", "：", "“", " ", '"', '（', '）', "#", " "]
    for char in replacement:
        inStr = inStr.replace(char, "")
    return inStr

def downloadVideo(waithId,newName,convert_to_mp3):
    if 'https://www.youtube' in waithId:
        url = waithId
    else:
        url = 'https://www.youtube.com/watch?v='+waithId
    yt = YouTube(url)
    print(yt.streams.filter(type="video"))
    saveFolder = 'd:\\mp4\\'
    oldFileName = saveFolder+newName+".mp4"
    # 下载mp4音频
    xx = yt.streams.filter(type="video", mime_type="video/mp4").order_by("abr").desc().first()
    xx.download(output_path=saveFolder, skip_existing=True,filename=oldFileName)
    print("file "+oldFileName+" is done!")
    if convert_to_mp3:
        convertToMp3(fileName=oldFileName)

def convertToMp3(fileName):
    newFileName = fileName.replace(".mp4", ".mp3")
    video = VideoFileClip(fileName)
    video.audio.write_audiofile(newFileName)

def delete_first_line():
    with open('data.txt', 'r+') as f:
        lines = f.readlines()

        if lines:
            first_line = lines[0]
            lines = lines[1:]

            f.seek(0)
            f.writelines(lines)

            f.truncate()

    # Do something with the first line
    print(first_line.strip())
    newFileName = oldFileName.replace(".mp4", ".mp3")
    video = VideoFileClip(oldFileName)
    video.audio.write_audiofile(newFileName)
