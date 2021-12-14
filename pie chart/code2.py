# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import matplotlib.pyplot as plt

#intialize the plot
fig = plt.figure()
# you can define size of the window 15 
# eg: fig= plt.figure (figsize=(20,10))

ax1 = fig.add_subplot (121)
ax2 = fig.add_subplot (122)

#plot the data
ax1.bar ([1,2,3], [3,4,5])
ax2.barh([0.5,1,2.5], [0,1,2])
ax1.axvline (0.65)
ax2.axhline (0.45)

#plot the graph
plt.show()
