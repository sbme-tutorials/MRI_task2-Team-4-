# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtWidgets, QtCore
from task2 import Ui_Form
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap , QImage, QPainter
import sys 
from math import*
import qimage2ndarray  
import numpy as np
import matplotlib.pyplot as plt
from math import exp,cos,sin,pi



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

            Kspace=np.fft.ifft2(Kspace)
            Phantom = qimage2ndarray.array2qimage(Kspace)
            pixmap = QPixmap.fromImage(Phantom)
            self.ui.show_phantom.setScaledContents(True)
            self.ui.show_phantom.setPixmap(pixmap)
            print('by')
          
         
            
    
        
def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()        
