import cv2
import numpy as np
import pyautogui

# Define the pixel position to monitor
pixel_x = 583
pixel_y = 428


try:
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot(region=(580,420, 1, 1))
      
      #  screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


       # if screenshot[0, 0][0] == green_color:
        if np.array(screenshot)[0][0][0] == 75:
            pyautogui.click()

except KeyboardInterrupt:
    print("Monitoring stopped by user.")