# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import numpy as np
import matplotlib.pyplot as plt

#set ranges of x and y axis
y = np.arange (-1,8,1) 
x= np.arange (-1,8,1)

#make y array with zeros as its elements
for i in list(y):
     y[i]=0           #assign 1 for x=1 (for x at 1)
     y[2]=1           #here for our given range y=1 for x=2

#display the graph
plt.stem(x,y)
plt.xlabel ('n index')
plt.ylabel('amplitude')
plt.title('discrete unit impulse fn')