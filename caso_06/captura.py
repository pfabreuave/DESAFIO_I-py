import pyautogui

# Capturar la pantalla completa
screenshot = pyautogui.screenshot()

# Capturar un área específica de la pantalla
area = (100, 100, 300, 300)
screenshot = pyautogui.screenshot(region=area)
screenshot.save("captura.png")
