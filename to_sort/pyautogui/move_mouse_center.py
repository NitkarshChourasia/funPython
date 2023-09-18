import pyautogui
import time
# Get the size of the monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the coordinates of the center of the screen.
x, y = screenWidth / 2, screenHeight / 2

# Move the mouse to the center of the screen.

for repeat in range(5):
    pyautogui.moveTo(x, y)
    time.sleep(1)

print("Execution done.")