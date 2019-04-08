# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:44:45 2019

@author: Asmaa
"""

import numpy as np

import matplotlib.pyplot as plt

PD= np.zeros([2,2],dtype=int)
PD[0:1,0:1]=np.full([1,1],255,dtype=int)
PD[1:2,0:2 ]=np.full([1,2],129,dtype=int)

T1= np.full([2,2],90,dtype=int)
T1[0:1,0:1]=np.full([1,1],900,dtype=int)
T1[1:2,0:2 ]=np.full([1,2],500,dtype=int)

T1= (T1*255)//np.max(T1)

T2= np.full([2,2],30,dtype=int)
T2[0:1,0:1]=np.full([1,1],90,dtype=int)
T2[1:2,0:2 ]=np.full([1,2],40,dtype=int)

T2= (T2*255)//np.max(T2)

All=np.concatenate([[PD],[T1],[T2]])

np.save("All2.npy", All)

imgplot = plt.imshow(T2,cmap="gray")                #ploting the array 

#imgplot = plt.imshow(All[0],cmap="gray")                #ploting the array 
