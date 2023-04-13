import moviepy.editor as moviepy
import os

def to_mp4_converter(dir='/home/ftpuser/whacontent'):
    content = os.listdir(dir)
    for file in content:
        if str(file).lower().endswith('.mov'):    
            clip = moviepy.VideoFileClip(f"{dir}/{file}")
            clip.write_videofile(f"{file.rsplit('.',1)[0]}.mp4")

if __name__ == '__main__':
    i = input("would you like to specify a dir (defaults to whacontent in ftpuser's home): ")
    if i:
        to_mp4_converter(i)
    else:
        to_mp4_converter()