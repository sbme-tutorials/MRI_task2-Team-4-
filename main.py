# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from task2 import Ui_Form
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap , QImage, QPainter
import sys 
import cv2
from math import*
import qimage2ndarray  
import numpy as np
import matplotlib.pyplot as plt
from imageio import imsave
from math import exp,cos,sin,pi,sqrt
from PIL import Image



class ApplicationWindow(QtWidgets.QMainWindow):
    global myImg
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.Browse_clicked)
      
        
    def Browse_clicked (self) :
        filename, _ = QFileDialog.getOpenFileName(self," ", "","All Files (*);;Python Files (*.txt)")
        if filename:
                All =np.load(filename)
                PD=All[0]
                T1=All[1]
                T2=All[2]
                phSize=32
                TR=2500
                TE=50
                theta=90
                theta=(theta*pi)/180
                Signal=np.zeros((phSize,phSize,3))
                Signal[0:phSize,0:phSize,0]=np.zeros((phSize,phSize))
                Signal[0:phSize,0:phSize,1]=np.zeros((phSize,phSize))
                Signal[0:phSize,0:phSize,2]=np.ones((phSize,phSize)) 
                Kspace=np.zeros((phSize,phSize),dtype=np.complex)
                RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                for i in range(phSize):   #kspacerow 
                    for k in range(phSize):
                        for m in range(phSize):
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[exp(-TE/T2[k][m]),0,0],[0,exp(-TE/T2[k][m]),0],[0,0,exp(-TE/T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1                        
                    for j in range(phSize):
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
                    Signal[0:phSize][0:phSize][1]=0
                    for k in range(phSize):
                        for m in range (phSize):                    #print(Kspace)
                            Signal[k][m][2]=(1-exp(-TR/T1[k][m]))
                
                Phantom=np.fft.fft2(Kspace)
                Phantom1=abs(Phantom)
                Phantom2 = qimage2ndarray.array2qimage(Phantom1)
                imsave("phantom.png", Phantom1)
                pixmap = QtGui.QPixmap("phantom.png")
                pixmap=pixmap.scaled(512,512)
                 #self.ui.show_phantom.setScaledContents(True)
                self.ui.show_phantom.setPixmap(pixmap)
                print('by')

         
            
    
        
def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()        