#!/usr/bin/env python
# coding: utf-8

# In[2]:


def judge_key(memory_up,memory_down,memory_left,memory_right,memory_block):
    """判断按键"""
    import random
    import pyautogui
    print("正在选择操作***")
    key=random.randint(1,memory_up+memory_down+memory_left+memory_right+memory_block)
    if key>=1 and key<(memory_up+1):
        key1=1
        print("已选择操作：按键上")
        pyautogui.keyDown('up');pyautogui.press('4');pyautogui.keyUp('up')
    elif key>=(memory_up+1) and key<(memory_up+memory_down+1):
        key1=2
        print("已选择操作：按键下")
        pyautogui.keyDown('down');pyautogui.press('down');pyautogui.keyUp('down')   
    elif key>=(memory_up+memory_down+1) and key<(memory_up+memory_down+memory_left+1):
        key1=3
        print("已选择操作：按键左")
        pyautogui.keyDown('left');pyautogui.press('4');pyautogui.keyUp('left')
    elif key>=(memory_up+memory_down+memory_left+1) and key<(memory_up+memory_down+memory_left+memory_right+1):
        key1=4
        print("已选择操作：按键右")
        pyautogui.keyDown('right');pyautogui.press('4');pyautogui.keyUp('right')
    elif key>=(memory_up+memory_down+memory_left+memory_right+1) and key<(memory_up+memory_down+memory_left+memory_right+memory_block+1):
        key1=5
        print("已选择操作：按键空格")
        pyautogui.keyDown('space');pyautogui.press('4');pyautogui.keyUp('space')
    print(" ")
    return(key1)


# In[17]:


import F_pic
import F_transform
import time
import F_jietu


def jugfe_fen(memory,num10,memory_wight,num11):
    """评价操作"""
    #import F_suiji #随机函数，临时用
    
    print("开始对操作评分***")
    #time.sleep(3)
    print(" ")
    
    #num2_=F_suiji.suijinum2() #暂时用随机函数代替

    num10_=num10
    p11=0
    
    while num10_==num10 and p11==0:
        p11=F_pic.picpixel(343,146)
        print("开始读取屏幕变化***")
        
        filename='png.bmp'
        F_jietu.window_capture(filename)
        #time.sleep(3)

        #得到二进制参数num2
        print("正在处理图片***")

        print("开始将图片二值化***")
        #time.sleep(3)

        F_pic.picTo2() #图片二值化

        print("二值化完成")
        print(" ")
        #time.sleep(3)

        print("开始生成二进制编号***")
        #time.sleep(3)

        num2_=F_pic.pic200()

        print("二进制编号生成完成***")
        print(" ")
        #time.sleep(3)

        num2_=F_pic.pic200()

        print("读取完成")
        #time.sleep(3)
        print(" ")    

        #把二进制参数num2转化十进制参数num10
        num10_=F_transform.to2to10(num2_)
    
    print("开始对比事件状态***")
    num11_=F_pic.pic201()
    print("分析完毕 状态码为：%d" %num11_)
    print(" ")
    
    if num11>num11_ :
        return_=2
    else:
        if memory.__contains__(str(num10_))==False:
            print("该操作 按键加权得分：0分  事件加权得分：0分")
            return_=0
        else:
            #读取记忆值并赋值给memory_up,memory_down,memory_left,memory_right,memory_block,memory_wight
            memorylist=memory[str(num10_)]
            memory_up_,memory_down_,memory_left_,memory_right_,memory_block_,memory_wight_=memorylist
            if memory_wight_>memory_wight:
                print("该操作 按键加权得分：1分  事件加权得分：1分")
                return_=2
            else: 
                return_=0
    print(" ")            
    return(return_)
            
    
            
            
    


# In[ ]:




