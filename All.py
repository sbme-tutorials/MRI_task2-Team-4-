# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:44:45 2019

@author: Asmaa
"""

import numpy as np

import matplotlib.pyplot as plt

PD= np.zeros([128,128],dtype=int)
PD[20:80,0:80]=np.full([60,80],255,dtype=int)
PD[80:128,50:80]=np.full([48,30],129,dtype=int)
PD[60:90,80:128]=np.full([30,48],195,dtype=int)

#print(PD)
T1= np.full([128,128],90,dtype=int)
T1[20:80,0:80]=np.full([60,80],900,dtype=int)
T1[80:128,50:80]=np.full([48,30],500,dtype=int)
T1[60:90,80:128]=np.full([30,48],150,dtype=int)

T1= (T1*255)//np.max(T1)


T2= np.full([128,128],150,dtype=int)
T2[20:80,0:80]=np.full([60,80],90,dtype=int)
T2[80:128,50:80]=np.full([48,30],40,dtype=int)
T2[60:90,80:128]=np.full([30,48],5,dtype=int)

T2= (T2*255)//np.max(T2)

All=np.concatenate([[PD],[T1],[T2]])

np.save("All128.npy", All)

imgplot = plt.imshow(T2,cmap="gray")                #ploting the array 

#imgplot = plt.imshow(All[0],cmap="gray")                #ploting the array 
