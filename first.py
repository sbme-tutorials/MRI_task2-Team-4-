# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(438, 332)
        self.image = QtWidgets.QLabel(Form)
        self.image.setGeometry(QtCore.QRect(40, 100, 351, 181))
        self.image.setText("")
        self.image.setObjectName("image")
        self.browse = QtWidgets.QPushButton(Form)
        self.browse.setGeometry(QtCore.QRect(9, 9, 89, 25))
        self.browse.setObjectName("browse")
        self.combo = QtWidgets.QComboBox(Form)
        self.combo.setGeometry(QtCore.QRect(264, 9, 151, 25))
        self.combo.setObjectName("combo")
        self.combo.addItem("")
        self.combo.addItem("")
        self.combo.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.browse.setText(_translate("Form", "PushButton"))
        self.combo.setItemText(0, _translate("Form", "PD"))
        self.combo.setItemText(1, _translate("Form", "T1"))
        self.combo.setItemText(2, _translate("Form", "T2"))

