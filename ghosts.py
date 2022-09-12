"""
Created on Wed Sep 7 20:42:26 2022

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


def do_atacks(total_atacks,monitor_configuration,march_time):
    
    while total_atacks >= 1:
        i = 0
        while i < 1:
            i += 1
            if i == 8:
                #enhanced
                do_enhanced_atack(monitor_configuration)
            else:
                #normal
                do_normal_atack(monitor_configuration)
                #march time 
            time.sleep(march_time)    
        total_atacks -= 1
    return

def do_normal_atack(monitor_configuration):
    if monitor_configuration == 1:
        pyautogui.moveTo(300, 300, duration = 1)
        pyautogui.click(300, 300)
        pyautogui.click(300, 300)
    else :
        pyautogui.moveTo(300, 300, duration = 1)
        pyautogui.click(300, 300)
        pyautogui.click(300, 300)
    return
def do_enhanced_atack(monitor_configuration):
    if monitor_configuration == 1:
        pyautogui.moveTo(100, 100, duration = 1)
        pyautogui.click(100, 100)
    else :
        pyautogui.moveTo(100, 100, duration = 1)
        pyautogui.click(100, 100)
    return