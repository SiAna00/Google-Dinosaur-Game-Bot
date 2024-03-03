import pyautogui
import time

time.sleep(3)

pyautogui.moveTo(670, 1045)
pyautogui.click()

time.sleep(3)

pyautogui.write("https://elgoog.im/t-rex/")
pyautogui.hotkey("enter")

time.sleep(10)

pyautogui.hotkey("space")

while True:
    if pyautogui.pixel(420, 790)[0] == 83 or pyautogui.pixel(420, 710)[0] == 83:
        pyautogui.hotkey("space")
