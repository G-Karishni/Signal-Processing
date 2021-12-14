# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import matplotlib.pyplot as plt

#x axis values
x = [1,2,3]
#y axis coressponding values
y = [2,4,1]

#plotting points
plt.plot(x,y)

#Label the axis
plt.xlabel('x axis')
plt.ylabel('y axis')

#name the graph
plt.title("my graph")
plt.show()

#click run !!