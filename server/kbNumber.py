# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kbNumber.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QLineEdit,QDialog ,QGridLayout, QLabel,QPushButton,QMainWindow,QApplication,QWidget,QHBoxLayout)

class Ui_Dialog(QDialog):
    def __init__(self,maxValue,showGroup=False):
        self.maxValue = maxValue
        super(Ui_Dialog,self).__init__()
        self.setObjectName("Dialog")
        self.resize(780, 480)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 780, 480))
        self.frame.setStyleSheet(".QFrame{background-color: #ffffff;}.QPushButton:pressed { background-color: #FF6E40} .QPushButton{font: 26pt \"Arial\";background-color: #4e9400;color: #ffffff;border-radius: 20px}.QLabel{font:  30pt \"Arial\";background-color: #ffffff;color: #000000;border: 2px solid gray;border-radius: 10px;padding: 0 8px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt1 = QtWidgets.QPushButton(self.frame)
        self.bt1.setGeometry(QtCore.QRect(40, 40, 121, 81))
        self.bt1.setObjectName("bt1")
        self.bt4 = QtWidgets.QPushButton(self.frame)
        self.bt4.setGeometry(QtCore.QRect(40, 150, 121, 81))
        self.bt4.setObjectName("bt4")
        self.bt7 = QtWidgets.QPushButton(self.frame)
        self.bt7.setGeometry(QtCore.QRect(40, 260, 121, 81))
        self.bt7.setObjectName("bt7")
        self.bt2 = QtWidgets.QPushButton(self.frame)
        self.bt2.setGeometry(QtCore.QRect(220, 40, 121, 81))
        self.bt2.setObjectName("bt2")
        self.bt5 = QtWidgets.QPushButton(self.frame)
        self.bt5.setGeometry(QtCore.QRect(220, 150, 121, 81))
        self.bt5.setObjectName("bt5")
        self.bt8 = QtWidgets.QPushButton(self.frame)
        self.bt8.setGeometry(QtCore.QRect(220, 260, 121, 81))
        self.bt8.setObjectName("bt8")
        self.bt0 = QtWidgets.QPushButton(self.frame)
        self.bt0.setGeometry(QtCore.QRect(220, 370, 121, 81))
        self.bt0.setObjectName("bt0")
        self.bt6 = QtWidgets.QPushButton(self.frame)
        self.bt6.setGeometry(QtCore.QRect(400, 150, 121, 81))
        self.bt6.setObjectName("bt6")
        self.bt3 = QtWidgets.QPushButton(self.frame)
        self.bt3.setGeometry(QtCore.QRect(400, 40, 121, 81))
        self.bt3.setObjectName("bt3")
        self.bt9 = QtWidgets.QPushButton(self.frame)
        self.bt9.setGeometry(QtCore.QRect(400, 260, 121, 81))
        self.bt9.setObjectName("bt9")
        self.btEnter = QtWidgets.QPushButton(self.frame)
        self.btEnter.setGeometry(QtCore.QRect(400, 370, 121, 81))
        self.btEnter.setObjectName("btEnter")
        self.btClear = QtWidgets.QPushButton(self.frame)
        self.btClear.setGeometry(QtCore.QRect(40, 370, 121, 81))
        self.btClear.setObjectName("btClear")
        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(560, 40, 181, 81))
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbValue.setObjectName("lbValue")
        self.btHuy = QtWidgets.QPushButton(self.frame)
        self.btHuy.setGeometry(QtCore.QRect(590, 230, 121, 81))
        self.btHuy.setObjectName("btHuy")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Keyboard"))

        self.bt1.setText(_translate("Dialog", "1"))
        self.bt4.setText(_translate("Dialog", "4"))
        self.bt7.setText(_translate("Dialog", "7"))
        self.bt2.setText(_translate("Dialog", "2"))
        self.bt5.setText(_translate("Dialog", "5"))
        self.bt8.setText(_translate("Dialog", "8"))
        self.bt0.setText(_translate("Dialog", "0"))
        self.bt6.setText(_translate("Dialog", "6"))
        self.bt3.setText(_translate("Dialog", "3"))
        self.bt9.setText(_translate("Dialog", "9"))
        self.btEnter.setText(_translate("Dialog", "Enter"))
        self.btClear.setText(_translate("Dialog", "Clear"))
        self.lbValue.setText(_translate("Dialog", "0"))
        self.btHuy.setText(_translate("Dialog", "Hủy"))

        self.setEvent()

    def setEvent(self):
        self.retrunVal = None
        self.btEnter.clicked.connect(self.btEnter_click)
        self.bt0.clicked.connect(self.bt0_click)
        self.bt1.clicked.connect(self.bt1_click)
        self.bt2.clicked.connect(self.bt2_click)
        self.bt3.clicked.connect(self.bt3_click)
        self.bt4.clicked.connect(self.bt4_click)
        self.bt5.clicked.connect(self.bt5_click)
        self.bt6.clicked.connect(self.bt6_click)
        self.bt7.clicked.connect(self.bt7_click)
        self.bt8.clicked.connect(self.bt8_click)
        self.bt9.clicked.connect(self.bt9_click)
        self.btClear.clicked.connect(self.btClear_click)
        self.btHuy.clicked.connect(self.btHuy_click)
        self.num = 0
    def numberPress(self,numIn):
        self.num = self.num*10 + numIn
        if self.num > self.maxValue:
            return
        self.lbValue.setText(str(self.num))

    def bt0_click(self):
        self.numberPress(0)

    def bt1_click(self):
        self.numberPress(1)
    
    def bt2_click(self):
        self.numberPress(2)
    def bt3_click(self):
        self.numberPress(3)
    def bt4_click(self):
        self.numberPress(4)
    def bt5_click(self):
        self.numberPress(5)
    def bt6_click(self):
        self.numberPress(6)
    def bt7_click(self):
        self.numberPress(7)
    def bt8_click(self):
        self.numberPress(8)
    def bt9_click(self):
        self.numberPress(9)    

    def btEnter_click(self):
        self.retrunVal = self.lbValue.text()
        self.accept()
    
    def btClear_click(self):
        self.num = int(int(self.lbValue.text())/10)
        self.lbValue.setText(str(self.num))
    def exec_(self):
        super(Ui_Dialog,self).exec_()
        return self.retrunVal
    def btHuy_click(self):
        self.close()
        
class MSG_Dialog(QDialog):
    def __init__(self):
        super(MSG_Dialog,self).__init__()
        self.setObjectName("Dialog")
        self.resize(650, 425)
        self.setStyleSheet(".QFrame{background-color: #4FC3F7;}.QPushButton:pressed { background-color: rgb(0, 0, 0)} .QPushButton{font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);border-radius: 20px}.QLabel{font: 75 30pt \"Arial\";background-color: #FF6E40;color: rgb(255, 255, 255);}")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 650, 450))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 60, 651, 91))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 260, 251, 101))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btEnter_click)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Lưu cài đặt thành công"))
        self.pushButton.setText(_translate("Dialog", "OK"))
    def exec_(self):
        super(MSG_Dialog,self).exec_()
    def btEnter_click(self):
        self.accept()
    
    