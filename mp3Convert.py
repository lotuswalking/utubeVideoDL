from pydub import AudioSegment
import os
subject = "The_Best_Relaxing_Classic_Romantic_Piano_Love_Songs"
oldFileName = 'd:\\mp3\\'+subject+'.mp4'
newFileName = 'd:\\mp3\\'+subject+'.mp3'
print('start to convert file:'+oldFileName)
sound = AudioSegment.from_file(oldFileName)
sound.export(newFileName, format='mp3')
os.remove(oldFileName)
print("Converted")
