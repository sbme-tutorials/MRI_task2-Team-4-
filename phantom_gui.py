# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phantom_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageEnhance 
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import cv2
import sys
from PyQt5.QtGui import QPixmap , QImage
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 903)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.T2 = QtWidgets.QTabWidget(self.centralwidget)
        self.T2.setObjectName("T2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.showphantom = QtWidgets.QLabel(self.tab)
        self.showphantom.setMaximumSize(QtCore.QSize(520, 520))
        self.showphantom.setObjectName("showphantom")
        self.gridLayout.addWidget(self.showphantom, 1, 4, 1, 4)
        self.Browse = QtWidgets.QPushButton(self.tab)
        self.Browse.setObjectName("Browse")
        self.gridLayout.addWidget(self.Browse, 0, 6, 1, 1)
        self.viewT1 = QtWidgets.QGraphicsView(self.tab)
        self.viewT1.setMaximumSize(QtCore.QSize(300, 300))
        self.viewT1.setObjectName("viewT1")
        self.gridLayout.addWidget(self.viewT1, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMaximumSize(QtCore.QSize(50, 50))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.viewT2 = QtWidgets.QGraphicsView(self.tab)
        self.viewT2.setMaximumSize(QtCore.QSize(300, 300))
        self.viewT2.setObjectName("viewT2")
        self.gridLayout.addWidget(self.viewT2, 4, 6, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMaximumSize(QtCore.QSize(50, 50))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 2, 1, 1)
        self.TR = QtWidgets.QTextEdit(self.tab)
        self.TR.setMaximumSize(QtCore.QSize(100, 100))
        self.TR.setObjectName("TR")
        self.gridLayout.addWidget(self.TR, 6, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setMaximumSize(QtCore.QSize(50, 50))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 7, 1, 1)
        self.flipangle = QtWidgets.QTextEdit(self.tab)
        self.flipangle.setMaximumSize(QtCore.QSize(100, 100))
        self.flipangle.setObjectName("flipangle")
        self.gridLayout.addWidget(self.flipangle, 6, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMaximumSize(QtCore.QSize(70, 70))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 5, 1, 1)
        self.TE = QtWidgets.QTextEdit(self.tab)
        self.TE.setMaximumSize(QtCore.QSize(100, 100))
        self.TE.setObjectName("TE")
        self.gridLayout.addWidget(self.TE, 6, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMaximumSize(QtCore.QSize(50, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 6, 1, 1)
        self.T2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(24, 340, 441, 301))
        self.label.setMaximumSize(QtCore.QSize(520, 520))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(580, 330, 441, 301))
        self.label_2.setMaximumSize(QtCore.QSize(520, 520))
        self.label_2.setObjectName("label_2")
        self.flipangle2 = QtWidgets.QTextEdit(self.tab_2)
        self.flipangle2.setGeometry(QtCore.QRect(470, 50, 100, 87))
        self.flipangle2.setMaximumSize(QtCore.QSize(100, 100))
        self.flipangle2.setObjectName("flipangle2")
        self.T2.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.T2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1127, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.T2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    #def Browse_clicked2 (self) :
       # myImage = cv2.imread("armand.jpg", cv2.IMREAD_GRAYSCALE)
       # height, width = myImage.shape
       #qImg = QImage(myImage.data, width, height, QImage.Format_Grayscale8).rgbSwapped())
       #pixmap = QPixmap.fromImage(qImg)
      # self.ui.showphatom.setPixmap(QPixmap.fromImage(qI))
    #def mouseMoveEvent(self, event):
        #if event.buttons() == QtCore.Qt.LeftButton:
          # im = Image.open("armand.jpg")
          # enhancer = ImageEnhance.Brightness(im)
          # enhanced_im = enhancer.enhance(3.8)
       # elif event.buttons() == QtCore.Qt.RightButton:
          # im = Image.open("armand.jpg")
           #enhancer = ImageEnhance.Brightness(im)
           #enhanced_im = enhancer.enhance(3.8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.showphantom.setText(_translate("MainWindow", "TextLabel"))
        self.showphantom.setMouseTracking(True)
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "    T1"))
        self.label_3.setText(_translate("MainWindow", "        TE"))
        self.label_7.setText(_translate("MainWindow", "        TR"))
        self.label_6.setText(_translate("MainWindow", "Flip Angle"))
        self.label_5.setText(_translate("MainWindow", "    T2"))
        self.T2.setTabText(self.T2.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.T2.setTabText(self.T2.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

