import pyautogui
import time
note = 'space'

def presss():
    pyautogui.keyDown(note)
    time.sleep(0.05)
    pyautogui.keyUp(note)    

while True:
    presss()
    presss()
    presss()
    time.sleep(5)

