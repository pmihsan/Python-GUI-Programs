import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

def takeScreenshot():
    screenShot = pyautogui.screenshot()
    savePath = asksaveasfilename()
    screenShot.save(savePath+"_screenshot.png")
    
button = tk.Button(text="Take Screenshot", command=takeScreenshot, font=10)
canvas.create_window(150, 150, window=button)

root.mainloop()