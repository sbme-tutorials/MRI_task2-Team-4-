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
           
             
def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()     