import subprocess

class adb_controller:
    def __init__(self) -> None:
        pass

    def post_wha_story(self):
        subprocess.run('./post.sh'.split)
    
    def reboot():
        subprocess.run('./reboot.sh'.split())

if __name__ == "__main__":
    adb = adb_controller()
    adb.reboot()