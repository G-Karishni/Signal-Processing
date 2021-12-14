# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""


import numpy as np
import matplotlib.pyplot as plt 

#set Limits for x and y axis
x = np.arange (-1,8,1)
y = np.arange (-1,8,1)

for i in list (y+1):
           if(i>=0):
             y[i]=1 
           elif(i<0):
             y[i]=0

#unit step fn is 1 from 0 to infinity and before that

plt.subplot (121)
plt.plot (y)
#plot is used for continous terms

plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('continuous unit step fn')
plt.subplot (122)
plt.stem(y)
#stem is used for discrete terms

plt.xlabel('n index')
plt.ylabel('amplitude') 
plt.title('discrete unit step fn')