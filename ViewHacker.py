'''
author: @NukeSuraj
'''

import pyautogui as pg
import time
import random

url = input("Enter Video URL: ")
t = int(input("Enter Time Duration in Minutes(only): "))
T = 60*t
n = int(input("Enter Number of Times To Watch: "))

pg.hotkey('win','2') # 2 refers to the position of desired web browser in taskbar
for i in range(n):
    time.sleep(0.5)
    pg.hotkey('ctrl','shift','n') # opens incognito mode 
    time.sleep(0.5)
    pg.typewrite(url)
    pg.hotkey('enter')
    time.sleep(5)
    ti = random.randint(0,T) # creates a uniques watch time to make it safer to be detected(Just in case) 
    print(ti)
    time.sleep(ti)
    pg.hotkey('ctrl','w')
    time.sleep(0.5)