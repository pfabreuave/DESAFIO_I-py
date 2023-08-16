import pyautogui
import time

# Esperar un tiempo específico
time.sleep(2)

# Obtener la posición actual del mouse
x, y = pyautogui.position()
print(f"Posición actual del mouse: {x}, {y}")
