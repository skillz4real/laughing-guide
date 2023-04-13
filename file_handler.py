import os
from random import choice
from datetime import datetime
from adb_controller import adb_controller
import subprocess
#from ppadb.client import Client

class file_handler():
    def __init__(self) -> None:
        self.origin = r'/home/ftpuser/content/'
        self.old = r'/home/ftpuser/content/old/'

    def push(self):
        try:
            for i in range(48):
                dir = os.listdir(self.origin)
                file = choice(dir)
                subprocess.run(f'adb shell push {self.origin}{file} {self.dest}'.split())
                os.rename(f'{self.origin}{file}',f'{self.old}{file}')
            return 1
            
        except:
            return 0

    def remove(self):
        os.chdir("./dropbox/")
        os.remove('*')

if __name__ == "__main__":
    c = file_handler()
    adb = adb_controller()
    r = c
    if r:
        adb.post_wha_story()
    #c.remove()
    with open('log.txt', 'a') as f:
        f.write(f'main.py ran on {datetime.now()}\n')
