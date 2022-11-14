from moviepy.editor import *
subject = "2022_破百万古风歌曲十首超好听的古风歌曲"
oldFileName = 'd:\\mp4\\'+subject+'.mp4'
newFileName = 'd:\\mp3\\'+subject+'.mp3'
video = VideoFileClip(oldFileName)
video.audio.write_audiofile(newFileName)
