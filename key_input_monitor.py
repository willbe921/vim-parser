from pyautogui import press
import time
import pyautogui


time.sleep(2)
cam_id_list = ['1','2','3']


dict = {'1':[1,3,5],'2':[2,0.5,1],'3':[1,3,2]}



# pyautogui.typewrite('Hello world!')
# pyautogui.typewrite('Hello world!', interval=0.25)
for i in range(3):

    for cam_id in cam_id_list:
        pyautogui.hotkey(cam_id,interval=dict[cam_id][i])


# pyautogui.hotkey('1',interval=1) 
# pyautogui.hotkey('3',interval=1)
# pyautogui.hotkey('5',interval=1)
# pyautogui.hotkey('2',interval=1)
# pyautogui.hotkey('4',interval=1)

# pyautogui.hotkey('shift','ctrl', 'left')
# pyautogui.hotkey('ctrl', 'c') 
# pyautogui.press('right')
# pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 'v') 
