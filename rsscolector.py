"""
Created on Thu Sep 8 9:32:05 2022

@author: boyro
"""

import pyautogui
import time

print(pyautogui.size())


#pygui.moveTo(100, 100, duration = 1)

#print(pygui.position())

#pyautogui.click(100, 100)
#pyautogui.scroll(200)
#pyautogui.typewrite("hello Geeks !")
#time.sleep(10)


def do_atacks(monitor_configuration,total_yields,march_time,town_position):
    
    while total_yields > 0:
        yield_rss(monitor_configuration,town_position)
        time.sleep(march_time)    
        total_yields -= 1
    return

def yield_rss(monitor_configuration,town_position):
    if monitor_configuration == 1:
        capture_location_up(monitor_configuration)
    else :
        capture_location_down(monitor_configuration)
    return


def capture_location_up(monitor_configuration):
    if monitor_configuration == 1:
        pyautogui.moveTo(870, 476, duration = 1)
        pyautogui.click(870, 476)
        
    else :
        pyautogui.moveTo(300, 300, duration = 1)
        pyautogui.click(300, 300)
        pyautogui.click(300, 300)
    return

def capture_location_down(monitor_configuration):
    if monitor_configuration == 1:
        pyautogui.moveTo(1054, 590, duration = 1)
        pyautogui.click(1054, 590,)
    else :
        pyautogui.moveTo(300, 300, duration = 1)
        pyautogui.click(300, 300)
        pyautogui.click(300, 300)
    return