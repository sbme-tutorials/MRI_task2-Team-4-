# -*- coding: utf-8 -*-

"""
Created on Thu Mar 21 08:05:46 2019

@author: Asmaa
"""

import numpy as np
import matplotlib.pyplot as plt
from math import exp,cos,sin,pi,sqrt
from Phantom import T1,T2
from PIL import Image


#theta=FA.text() #theta from text box
phSize=2
TR=25000
TE=100
theta=90
theta=(theta*pi)/180
Signal=np.zeros((phSize,phSize,3))
Signal[0:phSize,0:phSize,0]=np.zeros((phSize,phSize))
Signal[0:phSize,0:phSize,1]=np.zeros((phSize,phSize))
Signal[0:phSize,0:phSize,2]=np.ones((phSize,phSize))

Kspace=np.zeros((phSize,phSize),dtype=np.complex)
Spin_Vector=np.array([[0],[0],[1]])
RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])

print(Spin_Vector)
for i in range(phSize):   #kspacerow 
    for k in range(phSize):
        for m in range(phSize):
            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
            Decay=np.array([[exp(-TE/T2[k][m]),0,0],[0,exp(-TE/T2[k][m]),0],[0,0,exp(-TE/T1[k][m])]]) #3*3
            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1
           # Signal[k][m]=np.transpose(Spin_Vector) #32*32*3
          
    for j in range(phSize):
       #  print(i)
         Gy=(j/phSize)*(2*pi) #multi in cols
         Gx= (i/phSize)*(2*pi) # *rows
         for k in range(phSize):
             for m in range (phSize):          
                 alpha=Gx*k+Gy*m
                 x=Signal[k][m][0]
                 y=Signal[k][m][1]
                 z=sqrt(x**2+y**2)
                 Kspace[i][j]+=z*complex(cos(alpha),sin(alpha)) #remember to divied on 180 and make GX,Gy degrees
    Signal[0:phSize][0:phSize][0]=0
           # print(Signal)
    Signal[0:phSize][0:phSize][1]=0
    for k in range(phSize):
        for m in range (phSize):                    #print(Kspace)
            Signal[k][m][2]=(1-exp(-TR/T1[k][m]))


Kspace=np.fft.ifft2(Kspace)
Phantom=abs(Kspace)
plt.imshow(Phantom,cmap='gray')                                