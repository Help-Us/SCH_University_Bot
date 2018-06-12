#https://kminito.github.io/python/2018/04/08/mouse_coord.html
from pynput.mouse import Controller
import time

while(True):
    print("Current position: " + str(Controller().position))
    time.sleep(1)
