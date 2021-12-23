# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:31:46 2021

@author: cb.en.u4ece19116
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

def imp(fn,m,shift):
    fn=np.zeros(len(m))
    im=np.zeros(len(m))
    for i in m:
        if i==0:
            fn[i]=1
        else:
            fn[i]=0
    for i in m:
        if(i-shift)<0:
            im[i]=0
        else:
            im[i]=fn[i-shift]
    return im

n=np.arange(-1,4)
q=np.zeros(10)
x1=imp(q,n,0)
x2=imp(q,n,1)  

h1=np.zeros(10)
h2=np.zeros(10)

for i in range(0,3):
    h1[i]=0.5*x1[i]+0.5*x2[i]
plt.subplot(321)
plt.stem(h1)
plt.title("h1[n]")   

for i in range(0,3):
    h2[i]=0.5*x1[i]-0.5*x2[i]
plt.subplot(322)
plt.stem(h2)  
plt.title("h2[n]")   

def dtft(x,N):
    X=[]
    j=cmath.sqrt(-1)
    m=len(x)
    omega=np.linspace(0,2*np.pi,N)
    for i in range(0,m):
        sum=0
        for n in range(0,m):
            sum=(sum+x[n]*np.exp((-j)*omega[i]*n))
        X.append(sum)
    return X

H1=dtft(h1,10)
H2=dtft(h2,10)

plt.subplot(323)        
plt.plot(np.abs(H1))    
plt.ylabel("magnitude of H1")  
plt.subplot(325)    
plt.plot(np.angle(H1))
plt.ylabel("phase of H1")  

plt.subplot(324)        
plt.plot(np.abs(H2))    
plt.ylabel("magnitude of H2")  
plt.subplot(326)    
plt.plot(np.angle(H2))       
plt.ylabel("phase of H2")  