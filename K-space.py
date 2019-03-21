# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:05:46 2019

@author: Asmaa
"""

import numpy as np
from math import*
 #theta=FA.text() #theta from text box
phSize=128
RF=TR
theta=90
delta_t=0
omega=pi*TR*delta_t
theta=(theta*pi)/180
Kspace=np.zeros([128,128])

print (theta)
Spin_Vector=np.array([[0],[0],[1]])
print(Spin_Vector)
for i in range (1,phSize):
    RX=np.array([[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]])
    Spin_Vector=np.dot(RX,Spin_Vector)
    RX-Y=np.array([[cos(omega.delta_t),-sin(omega.delta_t),0],[sin(omega.delta_t),cos(omega.delta_t),0],[0,0,1]])
    Spin_Vector=np.dot(RX-Y,Spin_Vector)
    Decay=([[math.exp(-delta_t/T2[i]),0,0],[0,math.exp(-delta_t/T2[i]),0],[0,0,math.exp(-delta_t/T2[i])]])
    Spin_Vector=np.dot(Decay,Spin_Vector)
    Gx_step= ((i-1)/phSize)*2*pi
    
    for j in range (1,phSize):
      Gy_step=((j-1)/phSize)*2*pi 
      total_theta=(Gx_step*i+Gy_step*j)
      Kspace[i,k]+=math.exp(total_theta)*Spin_Vector
      Spin_Vector=np.array([[0],[0],[1-math.exp(delta_t[i]/T1[i])]])+Spin_Vector 
    
      
    