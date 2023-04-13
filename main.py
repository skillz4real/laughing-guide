import subprocess
import moviepy.editor as moviepy
import os
class adb_controller:
    def __init__(self) -> None:
        pass

    def unlock(self):
        subprocess.run('./unlock.sh'.split())

    def post(self):
        subprocess.run('./post_update.sh'.split())
    
    def clean(self):
        subprocess.run('./clean_phone.sh'.split())
    
    def push(self):
        subprocess.run('./push_content_2_phone.sh'.split())    
    
    def reboot(self):
        subprocess.run('./reboot.sh'.split())

    def remove(self):
        subprocess.run('./remove.sh'.split())
class media_processor:
    def __init__(self) -> None:
        pass

    def to_mp4_converter(self, dir='/home/ftpuser/whacontent/'):
        content = os.listdir(dir)
        for file in content:
            if str(file).lower().endswith('.mov'):    
                clip = moviepy.VideoFileClip(f"{dir}{file}")
                clip.write_videofile(f"{dir}{file.rsplit('.',1)[0]}.mp4")
if __name__ == "__main__":
    adb = adb_controller()