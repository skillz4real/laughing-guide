from main import adb_controller

if __name__ == "__main__":
    controller = adb_controller()
    adb_controller.post()
    controller.post()
    controller.remove()