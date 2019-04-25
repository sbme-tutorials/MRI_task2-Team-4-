# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




    def ssfp(self,TR=1000,TE=200,theta=180):
        
  
                theta=(theta*pi)/180
                Signal=np.zeros((self.height,self.width,3))
                Signal[0:self.height,0:self.width,0]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,1]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,2]=np.ones((self.height,self.width)) 
                Kspace=np.zeros((self.height,self.width),dtype=np.complex)
                
                # Kspace 
                for i in range(self.height):   ## enter Kspace rows 
                    if i==0:
                        theta=theta/2
                        RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                    for k in range(self.height):
                        for m in range(self.width):         
                            if i==0:
                                E = exp(-TE/(2*self.T2[k][m]))
                                Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                                Decay=np.array([[E,0,0],[0,E,0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
                                Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1
                            else :
                                E = exp(-TE/self.T2[k][m])
                                Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                                Decay=np.array([[E,0,0],[0,E,0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
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
                    theta=-1*theta
                    if i==0:
                        theta=-2*theta
                        RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                    for k in range(self.height):
                        for m in range (self.width):                    #print(Kspace)
                            Signal[k][m][2]=(1-exp(-TR/self.T1[k][m]))
                            #kspace finished 
                
                
                # start to constrcted Phantom
                Phantom=np.fft.fft2(Kspace)
                Phantom1=abs(Phantom)
                imsave("phantom.png", Phantom1)
                Kspace1=abs(ssKspace)
                imsave("Kspace.png", Kspace1)
                ks = QtGui.QPixmap("Kspace.png")
                ks=ks.scaled(300,200)
                pixmap = QtGui.QPixmap("phantom.png")
                pixmap = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio) 
                self.ui.constImage.setPixmap(pixmap)
                self.ui.kspace.setPixmap(ks)
                QtGui.QApplication.processEvents()
                print('kspace')

               
 

