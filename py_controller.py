import os
from random import choice

class py_controller:
    def move(self):
        dir = os.listdir()
        file = choice(dir)
        os.rename(file,f"dropbox/{file}")

    def remove(self):
        os.chdir("./dropbox/")
        os.remove('*')

if __name__ == "__main__":
    c = py_controller()
    c.move()
    os.system("./script.sh")
    c.remove()
