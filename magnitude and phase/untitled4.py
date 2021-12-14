# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import numpy as np 
import matplotlib. pyplot as plt

t=np. linspace(-0.02,0.05, 1000)
plt.xlim([-0.02,0.05]) 
#Labeled the x,y axis and titled the graph 

plt.xlim ([-0.02,0.05]) 
plt.title('phase response')
plt.subplot (211)
plt.plot(t, np.abs (np.exp(2j*np. pi*50*t))) 
#abs is used for finding magnitude response

plt.xlabel('t')
plt.ylabel('|x|') 
plt.title('magnitude response')
plt.subplot (212)
plt.plot(t,np.angle(np.exp(2j*np.pi*50*t))) 
#angle is used for finding phase response

plt.xlabel('t')
plt.ylabel('|_x')
#Labeled the x,y axis and titled the graph