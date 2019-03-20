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
#import cv2
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
             PD = open("small_phantom.txt", "rt")     #Opening the txt file
             print ('\n Matrix f: \n',PD.read())     #Reading it 
            imgplot = plt.imshow(PD.read())                #ploting the array feh moshkela hnaa
             self.ui.show_phantom(imgplot)
             print('by')
         
