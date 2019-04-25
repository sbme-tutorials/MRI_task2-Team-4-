# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:58:51 2019

@author: pc
"""

def IR(self,Signal,T1 = 1000):
                TR=int(self.ui.TR.text())

                theta=pi
                TE=T1*np.log(2)
                Signal=np.zeros((self.height,self.width,3))
                Signal[0:self.height,0:self.width,0]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,1]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,2]=np.ones((self.height,self.width)) 
                RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                 
                for i in range(self.height):                 
                    for k in range(self.height):
                        for m in range(self.width):
                            E = exp(-TE/self.T2[k][m])
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[E,0,0],[0,E,0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1 
                
                
                
                
                return Signal