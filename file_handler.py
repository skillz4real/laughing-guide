from main import adb_controller
from time import sleep

if __name__=="__main__":
    controller = adb_controller()
    controller.push()
    controller.reboot()
    sleep(50)
    controller.unlock()