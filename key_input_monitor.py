from pyautogui import press
import time
import pyautogui





pyautogui.typewrite('Hello world!')
pyautogui.typewrite('Hello world!', interval=0.25)
pyautogui.hotkey('shift','ctrl', 'left')
pyautogui.hotkey('ctrl', 'c') 
pyautogui.press('right')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v') 
