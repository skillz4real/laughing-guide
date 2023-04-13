import subprocess

class adb_controller:
    def __init__(self) -> None:
        pass

    def unlock(self):
        subprocess.run('./unlock.sh'.split())

    def post(self):
        subprocess.run('./post_update.sh'.split())
    
    def clean(self):
        subprocess.run('./clean.sh'.split())
    
    def push(self):
        subprocess.run('./push_content_2_phone.sh'.split())    
    
    def reboot(self):
        subprocess.run('./reboot.sh'.split())

if __name__ == "__main__":
    adb = adb_controller()