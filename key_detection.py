import keyboard
import pyautogui

while True:
    if keyboard.read_key()==15:
        keyboard.read_key()
        pyautogui.write(['space'])
        pyautogui.click(196,216, clicks=1)
        pyautogui.write(['right'])

        while (keyboard.read_key()!=14) & (keyboard.read_key()!=14):
            pass

    
        pyautogui.write(['backspace'])
        pyautogui.click(1136,383)
        pyautogui.write(['space'])
        continue


# import cv2

# vidcap = cv2.VideoCapture('/Users/teo/Desktop/summer_term/movies/the.outsiders.mp4')
# fps = vidcap.get(cv2.CAP_PROP_FPS)
# width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH )
# height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT )
# print(f"{fps} frames per second")
# print(f"{width} X {height} width X height")

# import pyautogui,time

# time.sleep(5)

# pyautogui.doubleClick(540,560)
# pyautogui.click(560,560)    
# pyautogui.click(550,550)
# pyautogui.click(550,570)



