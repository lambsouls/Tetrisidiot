#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#转换用函数库


# In[30]:


def to2to10(num):
    """把二进制数num转换为十进制并返回"""
    num=str(num)
    return(int(num,2))


# In[40]:


def strToDict(strNum):
    """字符串转化为字典"""
    import json
    strNum2=json.loads(strNum)
    return (strNum2)


# In[ ]:




