from main import adb_controller

if __name__ == "__main__":
    controller = adb_controller()
    controller.post()
    controller.remove()