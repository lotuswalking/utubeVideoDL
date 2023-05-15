from pytube import YouTube
from moviepy.editor import *
import mimetypes
def charReplace(inStr):
    replacement = ["@", "_", "(", ")", "|", "-", "/", ":",
                   "《", "》", "：", "“", " ", '"', '（', '）', "#", " "]
    for char in replacement:
        inStr = inStr.replace(char, "")
    return inStr


def getFiles(path):
    file_list = os.listdir(path)
    file_data = []
    for filename in file_list:
        # print(filename)
        filepath = os.path.join(path, filename)
        mimetype, encoding = mimetypes.guess_type(filepath)
        if mimetype:
            try:
                filesize = os.path.getsize(filepath)/1024/1024
            except:
                filesize = 0
            filesize = '%.1f MB' % filesize
            file_data.append({
                'filename': filename,
                'mimetype': mimetype,
                'filesize': filesize
            })
    # print(file_data)
    return file_data
def downloadVideo(waithId,newName,convert_to_mp3):
    if 'https://www.youtube' in waithId:
        url = waithId
    else:
        url = 'https://www.youtube.com/watch?v='+waithId
    yt = YouTube(url)
    # yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    print(f"there are {len(yt.streams)} streams in the url")
    saveFolder = 'd:\\mp4\\'
    oldFileName = saveFolder+newName+".mp4"
    # 下载mp4音频
    xx = yt.streams.filter(type="video").order_by("abr").desc().first()
    xx.download(output_path=saveFolder, skip_existing=True,filename=oldFileName)
    # print("file "+oldFileName+" is done!")
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
