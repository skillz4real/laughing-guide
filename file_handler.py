from main import adb_controller
from time import sleep
from datetime import datetime

if __name__=="__main__":
    try:
        controller = adb_controller()
        controller.push()
        controller.reboot()
        sleep(50)
        controller.unlock()
        with open('log.txt', 'a+') as f:
            f.write(f'{datetime.now()}: sucessfully pushed file 2 android rebooted and unlocked phone. Ready 4 action\n')

    except:
        with open('log.txt', 'a+') as f:
            f.write(f'{datetime.now()}:Error happened. The dir are probably empty\n')
