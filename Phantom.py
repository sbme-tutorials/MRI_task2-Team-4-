# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:44:45 2019

@author: Asmaa
"""

import numpy as np
import matplotlib.pyplot as plt

PD= np.zeros([128,128],dtype=int)
PD[20:80,0:50]=np.full([60,50],255,dtype=int)
PD[41:80,51:100]=np.full([39,49],129,dtype=int)
PD[0:50,51:128]=np.full([50,77],195,dtype=int)


imgplot = plt.imshow(PD)                #ploting the array 
