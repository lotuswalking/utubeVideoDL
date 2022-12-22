from moviepy.editor import *
def charReplace(inStr):
    replacement=["@","_","(",")","|","-","/",":","《","》","：","“"," ",'"','（','）']
    for char in replacement:
        inStr = inStr.replace(char,"")
    return inStr
def convertToMp3(oldFileName):

    newFileName = oldFileName.replace("mp4", "mp3")
    video = VideoFileClip(oldFileName)
    video.audio.write_audiofile(newFileName)