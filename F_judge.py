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


# In[3]:


def jugfe_fen(memory,num10,memory_wight):
    """评价操作"""
    import F_transform
    import F_suiji #随机函数，临时用
    
    print("开始对操作评分***")
    
    num2_=F_suiji.suijinum2() #暂时用随机函数代替
    
    #把二进制参数num2转化十进制参数num10
    num10_=F_transform.to2to10(num2_)
    
    if num10_==num10:
        print("该操作为无效操作")
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




