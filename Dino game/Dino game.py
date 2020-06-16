import pyautogui
from PIL import Image, ImageGrab
import time
def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
    for i in range(500, 590):
        for j in range(200, 225):
           if(data[i,j]<100):
                hit("down")
                return
    for i in range(500, 600):
        for j in range(225, 260):
            if(data[i,j]<100):
                hit("up")
                return

    return



print("Game start in 2 seconds")
time.sleep(2)
hit('up')
while True:
    image = ImageGrab.grab().convert('L')
    data=image.load()
    iscollide(data)

    '''for i in range(510, 550):
        for j in range(227, 260):
           data[i,j]=0

    for i in range(490, 540):
        for j in range(200, 227):
          data[i,j]=171
    image.show()
    break'''
