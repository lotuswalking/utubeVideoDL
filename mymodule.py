
    newFileName = oldFileName.replace(".mp4", ".mp3")
    video = VideoFileClip(oldFileName)
    video.audio.write_audiofile(newFileName)