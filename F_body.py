#!/usr/bin/env python
# coding: utf-8

# In[28]:


def body2(num10):
    """检查是否在游戏中并控制"""
    import F_testing
    
    a=False
    #循环开始
    while a==False:
        #判断是否在游戏中（调用状态检测函数）
        a=F_testing.testing1(num10)
        #否 延迟0.1s，进入循环
        #是 打破循环

