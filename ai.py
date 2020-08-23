#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#调用函数库
import F_transform
import F_body
#import F_suiji #随机函数，临时用
import F_testing
import F_memory
import F_judge
import json
import time
import F_jietu
import F_pic

input("press Enter")

#事件参数定义，num2为二进制参数，num10为十进制参数
num2=1
num10=1
#把json读入字典memory
memory={"key":[1,2,3,4,5,6]}
memory=F_memory.memory_read()


#自学习过程
while num2>0 and num10>0: #待修改
    
    print("——"*20)
    
    #读取屏幕
    filename='png.bmp'
    F_jietu.window_capture(filename)
    print("已读取屏幕")
    print(" ")
    
    #得到二进制参数num2
    print("正在处理图片***")
    F_pic.picTo2() #图片二值化
    
    
    num2=F_pic.pic200() #暂时用随机函数代替
    
    #把二进制参数num2转化十进制参数num10
    num10=F_transform.to2to10(num2)
    
    #输出事件参数
    print("事件编号:%d" %num10)
    print(" ")
    
    #检查是否为游戏中状态，不是就让他进入游戏中
    F_body.body2(num10)
    
    
    #检查字典里是否有该事件
    memory_if=memory.__contains__(str(num10))
    
    if memory_if==False:
    #无，输出已创建新事件
        
        #把记忆写入新的初始记忆写入memory
        memorystr="{\"%d\":[10,10,10,10,10,0]}" %num10
        memoryDict=F_transform.strToDict(memorystr)
        memory.update(memoryDict)#合并2个字典
        
        
        print("已创建新事件:%d" %num10)
        
        print(" ")
        
    print("已读取事件%d的记忆:" %num10)
    
    #读取记忆值并赋值给memory_up,memory_down,memory_left,memory_right,memory_block,memory_wight
    memorylist=memory[str(num10)]
    memory_up,memory_down,memory_left,memory_right,memory_block,memory_wight=memorylist
    
    print("按键上权重:%d 按键下权重:%d 按键左权重:%d 按键右权重:%d 按键空格权重:%d 事件权重分:%d" %(memory_up,memory_down,memory_left,memory_right,memory_block,memory_wight))
    print(" ")
    
    #做出按键判断
    key=F_judge.judge_key(memory_up,memory_down,memory_left,memory_right,memory_block)
    
    #评价操作
    Fen=F_judge.jugfe_fen(memory,num10,memory_wight)
    print("正在思考与总结***")
    #time.sleep(1)
    
    #加分
    if Fen==2:
        if key==1:
            memorylist[0]=memory_up+1
        elif key==2:
            memorylist[1]=memory_down+1
        elif key==3:
            memorylist[2]=memory_left+1
        elif key==4:
            memorylist[3]=memory_right+1
        elif key==5:
            memorylist[4]=memory_block+1
        memorylist[0]=memory_weight+1
    
    #写入记忆
    F_memory.memory_write(memory)    
    
input("press Enter")


# In[ ]:




