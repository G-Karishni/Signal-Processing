# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:00:00 2021

@author: karish
"""

import matplotlib.pyplot as plt

day = [1,2,3,4,5]
sleep = [7,8,2,11,5]
eat = [2,3,6,1,7]
code = [5,8,5,11,3]
movies= [8,5,1,4,8]

#give respective values for your variable for 5 days count 18 
#'b' as blue, 'g' as green, 'n as red, 'c' as cyan 19 
#'m' as magenta, 'y' as yellow, 'k' as black, 'w' as white

slices=[8,5,5,6]
#slice the data according ur requirement 

activities=['sleep', 'eat', 'code', 'movies']
cols=['g','m', 'r','b']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode= (0,0.1,0,0),
        autopct='%1.1f%%')
        
plt. title('Pie plot')
plt.show()