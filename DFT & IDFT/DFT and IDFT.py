# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:30:40 2021

@author: karish
"""

import numpy as np
import matplotlib.pyplot as plt 

def dft(x1,N):
    plt.subplot(221)
    plt.stem(x1)
    plt.title("x[n]")
    m=len(x1)
    X1=[]
    for k1 in range(0,N):
        sum1=0
        for n1 in range(0,m):
            sum1=sum1+(x1[n1]*(np.exp(((-1j)*2*np.pi*n1*k1)/N)))
        X1.append(sum1)
    plt.subplot(222)
    plt.title("magnitude")
    plt.stem(np.abs(X1)) 
    plt.subplot(223)
    plt.xlabel("phase")
    plt.stem(np.angle(X1))
    return X1

def idft(X2,N):
    m=len(X2)
    x2=[]
    for n2 in range(0,N):
        sum2=0
        for k2 in range(0,m):
            sum2=sum2+(X2[k2]*(np.exp((1j*2*np.pi*n2*k2)/N)))
        x2.append(sum2/N)
    plt.subplot(224)
    plt.stem(x2)
    plt.xlabel("reconstructed")
    return x2
    

n=int(input("Enter length: "))
a=np.zeros(5)
for i in range(0,n):
    a[i]=input("enter the signal: ")
Y=dft(a,4)
Z=idft(Y,4)
