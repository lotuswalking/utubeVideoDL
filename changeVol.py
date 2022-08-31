from pydub import AudioSegment
import os
subject = "我爱你中国"
# oldFileName = 'd:\\mp3\\'+subject+'.mp4'
newFileName = 'd:\\mp3\\'+subject+'.mp3'
# print('start to convert file:'+oldFileName)
sound = AudioSegment.from_file(newFileName)
loader = sound + 100
print(sound)
sound.export(newFileName, format='mp3')
print("Converted")
