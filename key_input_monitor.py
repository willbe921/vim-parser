from pyautogui import press
import time
import pyautogui
import pandas as pd
from collections import deque

def get_each_part_time(list_a):
    list_a=list_a[1:]
    new_list = []
    for ind ,ele in enumerate(list_a):
        if ind!=0:
            new_list.append(round(list_a[ind]-list_a[ind-1],3))
        else:
            new_list.append(ele)
        # print(new_list)
    
    return new_list


def load_csv_return_cam_time():
    csv_file = pd.read_csv('./cam_time.csv')
    time_list = csv_file['time']
    cam_list = csv_file['cam'][:-1]
    new_time_list= []
    # print(time_list)
    for cut_t in time_list:
        min=int(cut_t.split(':')[0])
        sec=int(cut_t.split(':')[1])
        ms=int(cut_t.split(':')[2])
        # print('min s ms:',min,sec,ms)
        min_con = round(min*60+sec+ms*(1/60),3)
        # print(min_con)
        new_time_list.append(min_con)
    new_time_list=get_each_part_time(new_time_list)
    print(new_time_list)
    print('cam len',len(cam_list))
    print('time len',len(new_time_list))
    # print(type(cam_list[0]))

    return cam_list,new_time_list






time.sleep(2)
# cam_id_list = ['1','2','3','4']
# list1=[2.1,3.4,4.3,5,6.5]
# list2=[1.1,2.4,4.3,6,7.5]
# list3=[0.5,2.4,3.6,4.5,6]
# # dict = {'1':[],'2':[],'3':[]}
# dict = dict([i,[]] for i in cam_id_list)
# print('dict',dict)

# list1 = get_each_part_time(list1)
# list2 = get_each_part_time(list2)
# list3 = get_each_part_time(list3)


# list1_q = deque(list1)
# list2_q = deque(list2)
# list3_q = deque(list3)
# # print(list1_q)
# # print(list1_q.popleft())
# # print(list1_q)



# print(list_1)


# dict['1']=list1_q
# dict['2']=list2_q
# dict['3']=list3_q




# # pyautogui.typewrite('Hello world!')
# # pyautogui.typewrite('Hello world!', interval=0.25)
# for i in range(3):

#     for cam_id in cam_id_list:
#         pyautogui.hotkey(cam_id,interval=dict[cam_id][i])


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



def hotkey_input(camid_list,cut_time_list):

    print('camid_list:',camid_list)

    pyautogui.hotkey('a',interval=0) 
    # pyautogui.hotkey('b',interval=0) 
    # pyautogui.hotkey('c',interval=0) 
    # pyautogui.hotkey('d',interval=0) 
    # pyautogui.hotkey('1',interval=2)
    # pyautogui.hotkey('2',interval=2)
    # pyautogui.hotkey('1',interval=0)


    for i in range(len(camid_list)):
        print('cam id:',camid_list[i])
        cam_id_key = ['1','2','3','4']

        print('now :',cut_time_list[i],cam_id_key[int(camid_list[i])-1])
        t1=time.time()
        pyautogui.press(cam_id_key[int(camid_list[i]-1)],interval=cut_time_list[i]-0.1) 
        t2=time.time()
        print('time spend:',t2-t1)
   


if __name__ == '__main__':
    camid_list,cut_time_list=load_csv_return_cam_time()
    time.sleep(3)
    hotkey_input(camid_list,cut_time_list)
# 

