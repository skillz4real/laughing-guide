import subprocess
import file_handler
from datetime import datetime

class adb_controller:
    def __init__(self) -> None:
        pass

    def post_wha_story(self):
        subprocess.run('./post.sh'.split())
    
    def reboot():
        subprocess.run('./reboot.sh'.split())

if __name__ == "__main__":
    adb = adb_controller()
    fh = file_handler.file_handler()
    r = fh.push()
    if not r:
        with open('log.txt', 'a') as f:
            f.write(f'{datetime.now()}: Error while pushing files\n')
    with open('log.txt', 'a') as f:
        f.write(f'{datetime.now()}: \n')
    adb.reboot()