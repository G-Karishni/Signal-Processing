# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:04:42 2021

@author: karish
"""

import numpy as np
import matplotlib.pyplot as plt

#shifting operation
def shift(im,m,shift):
    fn=np.zeros(len(m))
    for i in m:
        if (i-shift)<0:
            fn[i]=0
        else:
            fn[i]=im[i-shift]
    return fn

n=np.arange(0,5,1)
q=np.zeros(len(n))
#impulse signal
for i in n:
        if i == 0:
            q[i]=1
        else:
            q[i]=0
i1=shift(q,n,0)
i2=shift(q,n,1)
i3=shift(q,n,2)

x1=np.zeros(len(n))
for i in n:
    x1[i] = 0.5*i1[i]+0.5*i2[i]+0.5*i3[i]

h=np.array([3,2,1])
j=np.append(h,np.zeros(len(n)-len(h)))
h1=shift(j,n,1)
h2=shift(j,n,2)

y=np.zeros(len(n))
#reflection and time shift method
for i in n:
    y[i] = 0.5*j[i]+0.5*h1[i]+0.5*h2[i]
    
x=np.zeros(len(h))
for i in range(len(h)):
    x[i]=x1[i]
#checking using in-built convolution command    
y1 = np.convolve(x,h)

plt.subplot(211)
plt.stem(y1)
plt.title("using inbuilt convolution")
plt.subplot(212)
plt.stem(y)
plt.title("using reflection and time shift formula")