# To fill SRM feedback form automatically

import pyautogui
import time

def press_tab():
    pyautogui.press('tab')
    time.sleep(0.1)

def press_down():
    pyautogui.press('down')
    time.sleep(0.1)

def fill_feedback():
    press_down()
    time.sleep(2)
    for _ in range(9):
        press_down()
    press_tab()

print("Get ready, and point your cursor at the first index position...")
time.sleep(3)

while True:
    fill_feedback()
