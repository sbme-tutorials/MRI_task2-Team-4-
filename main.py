# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from bgrb import Ui_MainWindow
import sys
import math
from math import exp, cos, sin, pi, sqrt
import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QColor, QBrush, QPainter, QPen, QDragEnterEvent
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
from imageio import imsave, imread
import scipy.io as sio
import io
from time import sleep
import pyqtgraph as pg



class ApplicationWindow(QtWidgets.QMainWindow):
    global myImg
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.Browse_clicked)
        self.ui.showphantom.setMouseTracking(False)
        self.ui.comboBox.currentIndexChanged.connect(self.choose)
        self.ui.comboBox_2.currentIndexChanged.connect(self.choose_2)
        self.brit = 0
        self.points = QtGui.QPolygon()  #ae al points deh
        self.estna = False
        self.size = "128"
        self.state = "PD"
        self.ui.TE.clear()
        self.ui.TR.clear()
        self.ui.flipangle.clear()
        self.ui.TE.editingFinished.connect(self.Kspace)
        self.ui.TR.editingFinished.connect(self.Kspace)
        self.ui.flipangle.editingFinished.connect(self.Kspace)
        self.ui.tabWidget.setCurrentIndex(0)
        self.pen=[QtGui.QPen(QtCore.Qt.green),QtGui.QPen(QtCore.Qt.red),QtGui.QPen(QtCore.Qt.yellow),QtGui.QPen(QtCore.Qt.blue)]
        self.Pen1=[pg.mkPen('g'),pg.mkPen('r'),pg.mkPen('y'),pg.mkPen('b')]
        self.counter=-1
    def Browse_clicked(self):
       self.fileName,_ = QFileDialog.getOpenFileName(self," "," ", "All Files (*) ;; Python Files (*.jpg)")
       if self.fileName:
         All =np.load(self.fileName)
         PD=All[0]
         self.T1=All[1]
         self.T2=All[2]
         
         imsave("Pd.png", PD)
         imsave("T1.png", self.T1)
         imsave("T2.png", self.T2)
         
         self.myImage = cv2.imread("Pd.png" , cv2.IMREAD_GRAYSCALE)
         
         self.fileName0 = "Pd.png"
         self.fileName1 = "T1.png"
         self.fileName2 = "T2.png"
         
         self.height, self.width = self.myImage.shape
         
         self.pixmap = QtGui.QPixmap(self.fileName0)
         
         self.ui.showphantom.setScaledContents(True)
         self.ui.showphantom.setMouseTracking(False)
         
         self.ui.showphantom.mouseMoveEvent = self.changeBrit
         self.ui.showphantom.mousePressEvent = self.getClick
         
         self.ui.comboBox.currentIndexChanged.connect(self.choose)
         self.ui.comboBox_2.currentIndexChanged.connect(self.choose_2)
         
         self.estna = True
         self.Kspace()
    
    def mousePressEvent(self, e):
        self.points << e.pos()
        self.update()

# Get the pixel coordinates

    def getClick(self, event):
        #contrast
        if event.button() == Qt.LeftButton:
            self.left = True
            self.right = False
        if event.button() == Qt.RightButton:
            self.right = True
            self.left = False
           #Graph Painter 
        if event.button() == Qt.LeftButton:
            self.counter += 1
            x = event.pos().x()
            y = event.pos().y() 
            print("x = %d, y = %d" % (x,y))
            x1 = x * (self.myImage.shape[0]/512)
            y1 = y * (self.myImage.shape[0]/512)
            x1 = math.floor(x1)
            y1 = math.floor(y1)
            self.ui.showphantom.paint = True
            self.ui.showphantom.point.append([x,y ,self.pen[self.counter]])
            t = np.arange (0. , 500. ,1.)
            Mx = np.exp(-t /self.T2[x1][y1])
            Mz = 1-np.exp(-t/self.T1[x1][y1])
            self.ui.t1.plot(t , np.ravel(Mx),pen=self.Pen1[self.counter])
            self.ui.t2.plot(t , np.ravel(Mz),pen=self.Pen1[self.counter])
            self.TRline=self.TRline/500 
            self.TEline=self.TEline/500 
            self.ui.t1.addLine(x=self.TRline,pen='b')
            self.ui.t1.addLine(x=self.TEline,pen='r')
            self.ui.t2.addLine(x=self.TRline,pen='b')
            self.ui.t2.addLine(x=self.TEline,pen='r')       


        if event.button() == Qt.RightButton:
            self.ui.showphantom.point = []
            self.ui.t1.clear()
            self.ui.t2.clear()
            self.counter=-1


    def choose(self):
        self.state = self.ui.comboBox.currentText()
        if self.state == 'PD':
                self.pixmap = QtGui.QPixmap(self.fileName0)
        if self.state == 'T1':
                self.pixmap = QtGui.QPixmap(self.fileName1)
        if self.state == 'T2':
                self.pixmap = QtGui.QPixmap(self.fileName2)

    def choose_2 (self) :
        self.size = self.ui.comboBox_2.currentText()



# To change the brightness
    def changeBrit(self, event):
        if self.left:
           self.brit += 0.01
           im = Image.open(self.fileName0)
           enhancer = ImageEnhance.Brightness(im)
           enhanced_im = enhancer.enhance(self.brit)
           enhanced_im.save('enhanced_pic.jpg')
           fileName1 = "enhanced_pic.jpg"
           self.pixmap = QtGui.QPixmap(fileName1)
        if self.right:
           self.brit -= 0.01
           im = Image.open(self.fileName0)
           enhancer = ImageEnhance.Brightness(im)
           enhanced_im = enhancer.enhance(self.brit)
           enhanced_im.save('enhanced_pic.jpg')
           fileName1 = "enhanced_pic.jpg"
           self.pixmap = QtGui.QPixmap(fileName1)
    
            
    def Kspace(self):
        
                phSize=self.height
                print(phSize)
                TR=int(self.ui.TR.text())
                print(TR)
                self.TRline = TR 
                TE=int(self.ui.TE.text())
                print(TE)
                self.TEline = TE 
                theta=int(self.ui.flipangle.text())               
                print(theta)
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
                            Decay=np.array([[exp(-TE/self.T2[k][m]),0,0],[0,exp(-TE/self.T2[k][m]),0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
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
                            Signal[k][m][2]=(1-exp(-TR/self.T1[k][m]))
                
                Phantom=np.fft.fft2(Kspace)
                Phantom1=abs(Phantom)
                imsave("phantom.png", Phantom1)
                Kspace1=abs(Kspace)
                imsave("Kspace.png", Kspace1)
                ks = QtGui.QPixmap("Kspace.png")
                ks=ks.scaled(300,200)
                pixmap = QtGui.QPixmap("phantom.png")
                pixmap = pixmap.scaled(132, 200, QtCore.Qt.KeepAspectRatio)
               # pixmap=pixmap.scaled(512,512)
                 #self.ui.show_phantom.setScaledContents(True)
                self.ui.constImage.setPixmap(pixmap)
              #  self.ui.constImage.setPixmap(pixmap)
                self.ui.kspace.setPixmap(ks)


    def paintEvent(self, event):
        if self.estna:
            pixmap = self.pixmap
            if self.size == '128':
                pixmap = pixmap.scaled(128,128)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '64':
                pixmap = pixmap.scaled(64,64)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '32':
                pixmap = pixmap.scaled(32,32)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '3':
                pixmap = pixmap.scaled(3,3)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
    def Shep(self):
        def phantom (n = 256, p_type = 'Modified Shepp-Logan', ellipses = None):
        
        
                if (ellipses is None):
                        ellipses = _select_phantom (p_type)
                elif (np.size (ellipses, 1) != 6):
                        raise AssertionError ("Wrong number of columns in user phantom")
        
                # Blank image
                p = np.zeros ((n, n))
        
                # Create the pixel grid
                ygrid, xgrid = np.mgrid[-1:1:(1j*n), -1:1:(1j*n)]
        
                for ellip in ellipses:
                        I   = ellip [0]
                        a2  = ellip [1]**2
                        b2  = ellip [2]**2
                        x0  = ellip [3]
                        y0  = ellip [4]
                        phi = ellip [5] * np.pi / 180  # Rotation angle in radians
        
                        # Create the offset x and y values for the grid
                        x = xgrid - x0
                        y = ygrid - y0
        
                        cos_p = np.cos (phi)
                        sin_p = np.sin (phi)
        
                        # Find the pixels within the ellipse
                        locs = (((x * cos_p + y * sin_p)**2) / a2
                      + ((y * cos_p - x * sin_p)**2) / b2) <= 1
        
                        # Add the ellipse intensity to those pixels
                        p [locs] += I
        
                return p
        
        
        def _select_phantom (name):
                if (name.lower () == 'shepp-logan'):
                        e = _shepp_logan ()
                elif (name.lower () == 'modified shepp-logan'):
                        e = _mod_shepp_logan ()
                else:
                        raise ValueError ("Unknown phantom type: %s" % name)
        
                return e
        
        
        def _shepp_logan ():
                #  Standard head phantom, taken from Shepp & Logan
                return [[   2,   .69,   .92,    0,      0,   0],
                        [-.98, .6624, .8740,    0, -.0184,   0],
                        [-.02, .1100, .3100,  .22,      0, -18],
                        [-.02, .1600, .4100, -.22,      0,  18],
                        [ .01, .2100, .2500,    0,    .35,   0],
                        [ .01, .0460, .0460,    0,     .1,   0],
                        [ .02, .0460, .0460,    0,    -.1,   0],
                        [ .01, .0460, .0230, -.08,  -.605,   0],
                        [ .01, .0230, .0230,    0,  -.606,   0],
                        [ .01, .0230, .0460,  .06,  -.605,   0]]
        
        def _mod_shepp_logan ():
                #  Modified version of Shepp & Logan's head phantom,
                #  adjusted to improve contrast.  Taken from Toft.
                return [[   1,   .69,   .92,    0,      0,   0],
                        [-.80, .6624, .8740,    0, -.0184,   0],
                        [-.20, .1100, .3100,  .22,      0, -18],
                        [-.20, .1600, .4100, -.22,      0,  18],
                        [ .10, .2100, .2500,    0,    .35,   0],
                        [ .10, .0460, .0460,    0,     .1,   0],
                        [ .10, .0460, .0460,    0,    -.1,   0],
                        [ .10, .0460, .0230, -.08,  -.605,   0],
                        [ .10, .0230, .0230,    0,  -.606,   0],
                        [ .10, .0230, .0460,  .06,  -.605,   0]]
        P = phantom ()
        imsave("sheplogen.png",P)
        
        import os
        def load_lena():
            try:
                import scipy.misc
                l = scipy.misc.lena()
            except: # lena has been removed from scipy
                fname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data/lena.npz")
                f = np.load(fname)
                l = f['data']
                f.close()
            return l.astype(np.float32)
     




 

def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()        
