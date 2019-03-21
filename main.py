# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PyQt5 import QtWidgets, QtCore
from task2 import Ui_Form

from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap , QImage
import sys 
from math import*
import numpy as np
import matplotlib.pyplot as plt


class ApplicationWindow(QtWidgets.QMainWindow):
    global myImg
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.Browse_clicked)
      
        
    def Browse_clicked (self) :
          # fileName, _filter = QFileDialog.getOpenFileName(self, "Title", "Default File","(*.py)")
          fileName, _ = QFileDialog.getOpenFileName(self," ", "","All Files (*);;Python Files (*.txt)")
          if fileName:
             All =np.load(filename)

            PD=All[0]
            T1=All[1]
            T2=All[2]
            
            Phantom = qimage2ndarray.array2qimage(PD)
            pixmap = QPixmap.fromImage(Phantom)
            self.ui.show_phantom.setPixmap(pixmap)
            print('by')
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
         
             
