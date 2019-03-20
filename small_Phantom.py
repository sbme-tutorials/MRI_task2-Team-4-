# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 07:06:52 2019

@author: Asmaa
"""
import numpy as np
import matplotlib.pyplot as plt
PD= np.zeros([20,20],dtype=int)

PD[4:13,5:14]=np.full([9,9],255,dtype=int)
PD[0:3,7:15]=np.full([3,8],129,dtype=int)
PD[8:16,10:18]=np.full([8,8],195,dtype=int)
print (PD)



np.savetxt("small_phantom.txt", PD, fmt="%s")   #Saving the array as a text file


f = open("small_phantom.txt", "rt")     #Opening the txt file
print ('\n Matrix f: \n',f.read())     #Reading it 

imgplot = plt.imshow(PD)                #ploting the array 


#plt.matshow(PD)
#plt.show()