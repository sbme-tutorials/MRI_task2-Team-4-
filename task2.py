# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1013, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMouseTracking(False)
        Form.setAutoFillBackground(False)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 70, 361, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.show_phantom = QtWidgets.QLabel(self.gridLayoutWidget)
        self.show_phantom.setText("")
        self.show_phantom.setObjectName("show_phantom")
        self.gridLayout_2.addWidget(self.show_phantom, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(390, 20, 361, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TR = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.TR.setObjectName("TR")
        self.gridLayout_3.addWidget(self.TR, 0, 0, 1, 1)
        self.FlipAngle = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.FlipAngle.setObjectName("FlipAngle")
        self.gridLayout_3.addWidget(self.FlipAngle, 0, 4, 1, 1)
        self.TE = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.TE.setObjectName("TE")
        self.gridLayout_3.addWidget(self.TE, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(380, 70, 381, 361))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.T2graph = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.T2graph.setObjectName("T2graph")
        self.gridLayout_4.addWidget(self.T2graph, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 1)
        self.T1graph = QtWidgets.QGraphicsView(self.gridLayoutWidget_3)
        self.T1graph.setObjectName("T1graph")
        self.gridLayout_4.addWidget(self.T1graph, 2, 0, 1, 1)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_6.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.PhantomSize_comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.PhantomSize_comboBox.setObjectName("PhantomSize_comboBox")
        self.gridLayout_6.addWidget(self.PhantomSize_comboBox, 0, 1, 1, 1)
        self.Property_Combobox = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.Property_Combobox.setObjectName("Property_Combobox")
        self.gridLayout_6.addWidget(self.Property_Combobox, 0, 0, 1, 1)
        self.Browse = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.Browse.setCheckable(False)
        self.Browse.setChecked(False)
        self.Browse.setObjectName("Browse")
        self.gridLayout_6.addWidget(self.Browse, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Browse.setText(_translate("Form", "Browse"))

