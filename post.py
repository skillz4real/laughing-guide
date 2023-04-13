from main import adb_controller
from datetime import datetime

if __name__ == "__main__":
    controller = adb_controller()
    controller.post()
    controller.remove()
    with open('log.txt', 'a+') as f:
        f.write(f'{datetime.now()}: New status update posted\n')
