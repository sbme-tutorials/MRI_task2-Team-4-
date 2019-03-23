# -*- coding: utf-8 -*-

"""
Created on Thu Mar 21 08:05:46 2019

@author: Asmaa
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp,cos,sin,pi
from Phantom import T1,T2
from PIL import Image


#theta=FA.text() #theta from text box
phSize=32
TR=25000
TE=100
theta=90
theta=(theta*pi)/180
Signal=np.zeros([32,32,3])
Kspace=np.zeros([32,32],dtype=np.complex)
Spin_Vector=np.array([[0],[0],[1]])
#print(Spin_Vector.shape)
for i in range(32):   #kspacerow 
        for k in range(phSize):
            for m in range(phSize):
                RX=np.array([[1,0,0],[0,cos(theta),-sin(theta)],[0,sin(theta),cos(theta)]])
                #print(RX)
                #print(Spin_Vector)
                Spin_Vector=np.dot(RX,Spin_Vector)  #3*1
               # print(Spin_Vector)
                Decay=np.array([[exp(-TE/T1[k,m]),0,0],[0,exp(-TE/T1[k,m]),0],[0,0,1-exp(-TR/T2[k,m])]]) #3*3
               #print(Decay)
                Spin_Vector=np.dot(Decay,Spin_Vector)  #3*1
               # print(Spin_Vector)
                Signal[k,m]=np.transpose(Spin_Vector) #32*32*3
                #print(Signal[i,j])
        for j in range(32):
                Gy=(i/phSize)*(2*pi/180)
                Gx= (j/phSize)*(2*pi/180)
                for k in range(32):
                    for m in range (32):          
                        alpha=Gx*m+Gy*k
                        x=Signal[k,m,0]
                        y=Signal[k,m,1]
                        z=abs(x+y)
                        Signal[k,m]=z*complex(cos(alpha),sin(alpha))
                        Kspace[i,j]+=Signal[k,m,0]+Signal[k,m,1]
                
