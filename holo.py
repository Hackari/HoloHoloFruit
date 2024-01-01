import pyautogui
import time

note_colors = {
    'w': (225, 50, 50),     # Red
    's': (52, 144, 246),    # Blue
    'a': (245, 197, 67),    # Yellow
    'd': (45, 235, 43),     # Green
    'space': (174, 49, 208) # Purple
}

while True:
    px = pyautogui.pixel(1950,1007)
    for note, color in note_colors.items():
        if px == color:
            print(note)
            time.sleep(0.1)
            pyautogui.keyDown(note)
            time.sleep(0.05)
            pyautogui.keyUp(note)

    