# import keyboard

# while True:
#     if keyboard.read_key()==15:
#         keyboard.read_key()
#         keyboard.read_key()
#         if keyboard.read_key()==14:
#             print('ok pair')
#             continue

# # print(keyboard.read_key())

import cv2

vidcap = cv2.VideoCapture('/Users/teo/Desktop/summer_term/movies/the.outsiders.mp4')
fps = vidcap.get(cv2.CAP_PROP_FPS)
width = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH )
height = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT )
print(f"{fps} frames per second")
print(f"{width} X {height} width X height")
