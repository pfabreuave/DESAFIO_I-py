import pyautogui
import time

# time.sleep(10)
# posicion = pyautogui.position()
# Point(x=403, y=750)
# print(posicion)

pyautogui.moveTo(403, 750, duration = 1)
pyautogui.click()


# time.sleep(10)
# posicion = pyautogui.position()
# Point(x=76, y=10)
# print(posicion)

pyautogui.moveTo(76, 10, duration = 1)
pyautogui.click()

# time.sleep(10)
# posicion = pyautogui.position()
# # Point(x=439, y=308)
# print(posicion)

pyautogui.moveTo(439, 308, duration = 1)
pyautogui.click()

pyautogui.typewrite("youtube")
time.sleep(2)
pyautogui.hotkey('enter')
