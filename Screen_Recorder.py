import pyautogui
import numpy
import cv2
from win32api import GetSystemMetrics
import datetime as dt

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

current_dt = dt.datetime.now().strftime('%d-%m-%Y %I-%M-%S')
file_name = current_dt + '.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(file_name, fourcc, 10.0, (screen_width, screen_height))

while True:
    img = pyautogui.screenshot()
    img_np = numpy.array(img)
    img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder', img_np)
    video.write(img_rgb)
    if cv2.waitKey(10) == ord('q'):
        break
