#!/usr/bin/env python
# coding: utf-8

# In[47]:


def memory_read():
    """读取记忆"""
    import json
    with open("memory.json", encoding="utf-8") as f:
        str1 = f.read()
        str2=eval(str1)
        
        memory = json.loads(str2) 
    print("已读入记忆")
    return(memory)


# In[49]:


def memory_write(memory):
    """写入记忆"""
    import json
    memory2=json.dumps(memory)
    with open("memory.json", "w", encoding='utf-8') as f:
        json.dump(memory2, f, indent=2, sort_keys=True)
    print("已写入记忆")
    print(" ")
    


# In[13]:


"""读取事件记忆"""


# In[12]:


"""写入事件记忆"""


# In[ ]:




