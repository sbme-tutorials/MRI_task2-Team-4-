# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:17:57 2019

@author: pc
"""

 def spinecho(self,TR=1000,TE=200,theta=90):
        
                self.width
#                print(phSize)
                TR=int(self.ui.TR.text())
#                print(TR)
                self.TRline = TR 
                TE=int(self.ui.TE.text())
#                print(TE)
                self.TEline = TE 
                theta=int(self.ui.flipangle.text())               
#                print(theta)
                theta=(theta*pi)/180
                r=TE/2
                Signal=np.zeros((self.height,self.width,3))
                Signal[0:self.height,0:self.width,0]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,1]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,2]=np.ones((self.height,self.width)) 
                Kspace=np.zeros((self.height,self.width),dtype=np.complex)
                RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                
                 #kspace
                for i in range(self.height):   ## enter Kspace rows 
                    
                    for k in range(self.height):
                        for m in range(self.width):
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[exp(-r/self.T2[k][m]),0,0],[0,exp(-r/self.T2[k][m]),0],[0,0,exp(-r/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1 
                            theta=2*theta
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[exp(-r/self.T2[k][m]),0,0],[0,exp(-r/self.T2[k][m]),0],[0,0,exp(-r/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1 
                            
                    QtGui.QApplication.processEvents()
                    for j in range(self.height): # enter Kspace columns
                         Gy=(j/self.height)*(2*pi) #multi in cols
                         Gx= (i/self.width)*(2*pi) # *rows
                         for k in range(self.height):
                             for m in range (self.width):          
                                 alpha=Gx*k+Gy*m
                                 x=Signal[k][m][0]
                                 y=Signal[k][m][1]
                                 z=sqrt(x**2+y**2)
                                                                
                                 Kspace[i][j]+=z*complex(cos(alpha),sin(alpha)) #remember to divied on 180 and make GX,Gy degrees
                    QtGui.QApplication.processEvents()    
                    Signal[0:self.height][0:self.width][0]=0
                    Signal[0:self.height][0:self.width][1]=0
                    #spoiler
                    for k in range(self.height):
                        for m in range (self.width):                    #print(Kspace)
                            Signal[k][m][2]=(1-exp(-TR/self.T1[k][m]))