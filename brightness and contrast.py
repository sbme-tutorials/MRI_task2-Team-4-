# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 20:25:39 2019

@author: pc
"""
from Task2 import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap , QImage
import numpy as np
import cv2
import sys
from PIL import Image, ImageEnhance 
def Browse_clicked2 (self) :
   def mouseMoveEvent(self, event):
   global myImage
   myImage = cv2.imread("enhanced.armand.jpg", cv2.IMREAD_GRAYSCALE)
   height, width = myImage.shape
   qImg = QImage(myImage.data, width, height, QImage.Format_Grayscale8).rgbSwapped()
   pixmap = QPixmap.fromImage(qImg)
   self.ui.showphatom.setPixmap(QPixmap.fromImage(qI
   self.ui.image.mouseMoveEvent = self.getPos
def getPos(self, event):   
        x = event.pos().x()
        y = event.pos().y() 
   
   im = Image.open("armand.jpg")
   enhancer = ImageEnhance.Brightness(im)
   enhanced_im = enhancer.enhance(3.8)
   enhanced_im.save("enhanced.armand.jpg")
   super().mousePressEvent(event)
    print("armand.jpg" % (x,y))
   
   




   