# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:44:45 2019

@author: Asmaa
"""

import numpy as np
import math
import matplotlib.pyplot as plt

PD= np.zeros([128,128],dtype=int)
PD[20:80,0:50]=np.full([60,50],255,dtype=int)
PD[41:80,51:100]=np.full([39,49],129,dtype=int)
PD[0:50,51:128]=np.full([50,77],195,dtype=int)

#print(PD)

T1= np.full([128,128],250,dtype=int)
T1[20:80,0:50]=np.full([60,50],4000,dtype=int)
T1[41:80,51:100]=np.full([39,49],500,dtype=int)
T1[0:50,51:128]=np.full([50,77],900,dtype=int)

T1= (T1*255)//np.max(T1)

T2= np.full([128,128],70,dtype=int)
T2[20:80,0:50]=np.full([60,50],2000,dtype=int)
T2[41:80,51:100]=np.full([39,49],40,dtype=int)
T2[0:50,51:128]=np.full([50,77],90,dtype=int)

T2= (T2*255)//np.max(T2)

All=np.concatenate([[PD],[T1],[T2]])
`

np.save("All.npy", All)

#imgplot = plt.imshow(PD,cmap="gray")                #ploting the array 

imgplot = plt.imshow(All[0],cmap="gray")                #ploting the array 
