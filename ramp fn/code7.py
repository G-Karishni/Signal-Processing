# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""


#import the Libraries
import numpy as np
import matplotlib.pyplot as plt

#set the range of x axis
x=np.arange (0,10)

#assigning values for y
y=[x1 for x1 in list(x)]

plt.subplot (121) 
plt.plot (x,y) 
#plot is used to plot in continuous

plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('continuous unit ramp fn')

plt.subplot (122)
plt.stem(x,y)
#stem is used to plot in discrete

plt.xlabel('time') 
plt.ylabel('amplitude')
plt.title('discrete unit ramp fn')

#to plot/display two graphs in same window we need mention subplot fn
#subplot(rows coloumn position of that plot)

