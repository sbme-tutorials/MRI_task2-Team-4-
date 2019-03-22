
"""
Created on Fri Mar  8 20:25:39 2019

@author: pc
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap , QImage
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import cv2
import sys
from PIL import Image, ImageEnhance 
from imageio import imsave, imread
from phantom_gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL.ImageQt import ImageQt


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.Browse.clicked.connect(self.Browse_clicked)
        self.ui.showphantom.setMouseTracking(False)
    def Browse_clicked(self):
       self.fileName,_ = QFileDialog.getOpenFileName(self," "," ", "All Files (*) ;; Python Files (*.jpg)")
       if self.fileName:
         myImage = cv2.imread(self.fileName , cv2.IMREAD_GRAYSCALE)
         height, width = myImage.shape
         qImg = QImage(myImage.data, width, height, QImage.Format_Grayscale8).rgbSwapped()
         self.ui.showphantom.setPixmap(QPixmap.fromImage(qImg))# -*- coding: utf-8 -*-myImage = cv2.imread("armand.jpg", cv2.IMREAD_GRAYSCALE)
         height, width = myImage.shape
         qImg = QImage(myImage.data, width, height, QImage.Format_Grayscale8).rgbSwapped()
         self.ui.showphantom.setPixmap(QPixmap.fromImage(qImg))# -*- coding: utf-8 -*-
         self.ui.showphantom.setScaledContents(True)
         self.ui.showphantom.mouseMoveEvent=self.changeBrit
    def changeBrit(self, event):
           im = Image.open(self.fileName)
           enhancer = ImageEnhance.Brightness(im)
           enhanced_im = enhancer.enhance(1.8)
           enhanced_im.save('enhanced_pic.jpg')
           fileName1 = "enhanced_pic.jpg"
           pixmap = QtGui.QPixmap(fileName1)
           self.ui.showphantom.setPixmap(pixmap)


   #enhanced_im.save("enhanced.armand.jpg")
   #super().mousePressEvent(event)
    #print("armand.jpg" % (x,y))
   
app = QtWidgets.QApplication(sys.argv)
window = ApplicationWindow()
sys.exit(app.exec_())



   