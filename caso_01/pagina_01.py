import pyautogui
import time


pyautogui.hotkey("win", "r")

time.sleep(2)

pyautogui.write('chrome.exe "totidiversidade.com.br"', interval = 0.5)

time.sleep(2)

pyautogui.press("enter")