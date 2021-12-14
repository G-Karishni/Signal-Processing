# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import matplotlib.pyplot as plt

#points of scattered plot  
plt.scatter ([0.3,3.8, 1.2, 2.5], [11, 25,9,26], color='darkgreen', marker='^')
plt.scatter ([1.3,2.8, 1.2,3.5], [15, 25,19,16], color='blue',marker='*')

#set Limits for xaxis
plt.xlim (0.5,4.5)

plt.show()
#plot the graph

#click Run !!