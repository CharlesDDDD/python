#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# In[19]:


#一个遍历文件夹下面全部文件的函数
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            if f.endswith('.xlsx'):
                fullname = os.path.join(root, f)
                yield fullname


# In[44]:


#base市场预测文件夹 我将名字换成market_pred 换成其他亦可
base = 'market_pred/'
x = 0
d_list = [0]*60
for i in findAllFile(base):
    data = pd.read_excel(i)
    rows = data.values
    #d_list即为列表 d_list[i]代表第i天的需求预测 先求和再算平均
    for k in range(60):
        d_list[k] += rows[3+2*(k//10)][k%10+1]
for j in range(60):
    d_list[j] = round(d_list[j]/100)
d_list

