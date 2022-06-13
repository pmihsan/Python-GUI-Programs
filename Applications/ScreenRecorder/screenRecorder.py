import cv2
import numpy as np
import pyautogui
import keyboard

# Get the size of the screen using pyautogui
screen_size = tuple(pyautogui.size())

# Define the format and create video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (screen_size))

while True:
    # Capture Screen
    img = pyautogui.screenshot()

    #Convert image into numpy array
    img = np.array(img)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    out.write(img)

    # To Exit press q to terminate
    if(keyboard.is_pressed('q')):
        print("Recording Stopped")
        break

out.release()
cv2.destroyAllWindows()
