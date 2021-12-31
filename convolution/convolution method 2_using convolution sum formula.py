# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:10:00 2021

@author: karish
"""

import numpy as np
from matplotlib import pyplot as plt

h = [3,2,1]
x = [0.5,0.5,0.5]

N1 = len(x)
N2 = len(h)
N = N1+N2-1
y = np.zeros(N)

y1 = np.convolve(x,h)
m = N-N1
n = N-N2

x =np.pad(x,(0,m),'constant')
h =np.pad(h,(0,n),'constant')

#Linear convolution using convolution sum formula
for n in range (N):
    for k in range (N):
        if n >= k:
             y[n] = y[n]+x[k]*h[n-k]
         
plt.subplot(211)
plt.title('using convolution sum')
plt.stem(y)

plt.subplot(212)
plt.title('using numpy built-in function')
plt.stem(y1)
