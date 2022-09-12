"""
Created on Wed Sep 7 20:40:19 2022

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

def do_tasks(max_amought,auto_complete_task,monitor_configuration,refreshers,type):

    


    return




def claim_tasks(max_amought,auto_complete_task,monitor_configuration):

    if auto_complete_task:
        #if premiun level allows insta completition of all task
        if monitor_configuration == 1:
            pyautogui.moveTo(100, 100, duration = 1)
            pyautogui.click(100, 100)
        else:
            pyautogui.moveTo(100, 100, duration = 1)
            pyautogui.click(100, 100)
        max_amought = 0
    else:
        while max_amought > 0:
            if monitor_configuration == 1:
                pyautogui.moveTo(300, 300, duration = 1)
                pyautogui.click(300, 300)
                pyautogui.click(300, 300)
            else:
                pyautogui.moveTo(300, 300, duration = 1)
                pyautogui.click(300, 300)
                pyautogui.click(300, 300)
            max_amought -= 1        
    return