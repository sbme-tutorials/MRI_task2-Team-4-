# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:21:13 2019

@author: pc
"""

def T2Prep(self,Signal,TR=1000,TE=200,theta=90):
                TR=int(self.ui.TR.text())

                theta=(theta*pi)/180
                T=3*T2
                Signal=np.zeros((self.height,self.width,3))
                Signal[0:self.height,0:self.width,0]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,1]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,2]=np.ones((self.height,self.width)) 
                RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                 
                for i in range(self.height):                 
                    for k in range(self.height):
                        for m in range(self.width):
                            E = exp(-T/self.T2[k][m])
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[E,0,0],[0,E,0],[0,0,exp(-T/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1 
                            theta=-1*theta
                            E = exp(-TE/self.T2[k][m])
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[E,0,0],[0,E,0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  
                
                
                
                
                return Signal