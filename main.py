#importing Tkinter Library
import time

#importing filedialog from tkinter
from tkinter import filedialog

#importing pyautogui for taking screenshot
import pyautogui as pyg

#to get access over operating sysytem like getting paths
import os

#for fetching date time of the system
import datetime


n = 4
stars = 1

#opening dialog box using tkinter
folder = filedialog.askdirectory()


for i in range(n):
  current = datetime.datetime.now().replace(microsecond=0)
  format = " %y_%b_%d_%H_%M_%S"
  new_time = datetime.datetime.strftime(current, format)
  for j in range(0, n-1):
    print(" ", end = "")
  print("* "*stars)

#delay of 5 seconds after every iteration
  time.sleep(5)

#taking screenshot of each iteration line by line
  screen = pyg.screenshot()

#making file name unique by their timestamp
  file = os.path.join(folder, f"hello{new_time}.png")

#saving screenshot
  screen.save(file)
  stars += 1
  n -= 1