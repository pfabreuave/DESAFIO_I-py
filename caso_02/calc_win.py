import pyautogui
import time


pyautogui.hotkey("win", "r")

time.sleep(2)

pyautogui.write('calc.exe', interval = 0.5)

time.sleep(2)

pyautogui.press("enter")