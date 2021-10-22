import cv2
from pytesseract import pytesseract
from pytesseract import Output
import numpy as np
from PIL import ImageGrab
import pyautogui
import wmi
import keyboard as k
import functions as fc

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
cv2.namedWindow("Screen")

while True:
    img = ImageGrab.grab(bbox=(0, 210, 500, 245)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    words_in_range = pytesseract.image_to_string(frame)

    if not words_in_range.__contains__("83."):
        pyautogui.keyDown("w")
        if words_in_range.__contains__("83."):
            pyautogui.keyUp("w")
        

    print(words_in_range)

    cv2.imshow("Screen", frame)
    if cv2.waitKey(1) & 0Xff == ord("q"):
        break

cv2.destroyAllWindows()