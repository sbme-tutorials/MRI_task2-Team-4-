from PyQt5 import QtWidgets, QtCore, QtGui
from first import Ui_Form
from PyQt5.QtWidgets import QFileDialog, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QImage,QPainter*
import sys
import cv2
import numpy as np
from array import * 
from PIL import Image, ImageEnhance 

class ApplicationWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.browse.clicked.connect(self.browse_clicked)
        self.ui.image.mousePressEvent = self.getPos
        self.ui.image.mouseMoveEvent = self.getPos
        self.ui.combo.currentIndexChanged.connect(self.choose)


    def browse_clicked(self):
        filename, _filter = QFileDialog.getOpenFileName(self, "Title", "Default File", "All Files (*);;Image Files (*.png)")
        if filename:
            All =np.load(filename)
            PD=All[0]
            T1=All[1]
            T2=All[2]            
            rectangle = QRectF(self.x,self.y, 2.0, 2.0)
            painter = QPainter(self)
            painter.drawRect(rectangle)
            pixmap = QPixmap(fileName)
            pixmap = pixmap.scaled(int(pixmap.height()), int(pixmap.width()), QtCore.Qt.KeepAspectRatio)
            self.ui.image.setScaledContents(True)
            self.ui.image.setPixmap(pixmap)
            
            
            

    def getPos(self , event):
        self.x = event.pos().x()
        self.y = event.pos().y() 
        print("x = %d, y = %d" % (x,y))
        px = self.PD[x,y]
        print (px)

    def choose(self):
        state = self.ui.combo.currentText() 
        if state == "PD" :
            print ("PD")
        elif state == "T1" :
            print ("T1")
        else :
            print("T2")

def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()