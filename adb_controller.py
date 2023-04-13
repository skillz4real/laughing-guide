import moviepy.editor as moviepy
import os

dir = '/home/ftpuser/whacontent'
content = os.listdir(dir)
for file in dir:
    if file.endswith():
        pass
    clip = moviepy.VideoFileClip(f"{dir}/{file}")
    clip.write_videofile(f"{file.rsplit('.',1)[0]}.mp4")