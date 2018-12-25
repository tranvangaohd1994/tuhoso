# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setThongGio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QTimer
from kbNumber import Ui_Dialog
import uart

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setThongGio(object):
    def setupUi(self, setThongGio):
        setThongGio.setObjectName("setThongGio")
        setThongGio.resize(1280, 800)
        setThongGio.setStyleSheet("")
        self.setThongGio = setThongGio

        self.frame = QtWidgets.QFrame(setThongGio)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/hgtg.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 15px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}.MyQLineEdit{border: 2px solid black;border-radius: 10px;padding: 0 8px;font: bold 32px \"Arial\"; text-align: center;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btKichHoat = QtWidgets.QPushButton(self.frame)
        self.btKichHoat.setGeometry(QtCore.QRect(200, 620, 191, 80))
        self.btKichHoat.setObjectName("btKichHoat")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(477, 620, 160, 81))
        self.btExit.setObjectName("btExit")
        self.tbPhut = MyQLineEdit(self.frame)
        self.tbPhut.setGeometry(QtCore.QRect(480, 360, 151, 81))
        self.tbPhut.setObjectName("tbPhut")
        self.tbTimes = MyQLineEdit(self.frame)
        self.tbTimes.setGeometry(QtCore.QRect(480, 460, 151, 81))
       
        self.tbTimes.setObjectName("tbTimes")
        self.tbGio = MyQLineEdit(self.frame)
        self.tbGio.setGeometry(QtCore.QRect(220, 360, 151, 81))
       
        self.tbGio.setObjectName("tbGio")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(170, 560, 431, 55))
        self.grcdControl.setStyleSheet("#grcdControl{background-color:#ffffff;border-radius: 5px;}\n"
        ".QRadioButton {background-color:white;color:#4e9400;font:bold 24px \"Arial\";}.QRadioButton::indicator{width:30px;height:30px;border-radius:20px;} .QRadioButton::indicator:checked{background-color:       red;border: 2px solid #4e9400;}\n"
        ".QRadioButton::indicator:unchecked {border: 2px solid #4e9400;border-radius: 20px;}\n"
        "")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbAllDay = QtWidgets.QRadioButton(self.grcdControl)
        self.rbAllDay.setGeometry(QtCore.QRect(230, 5, 191, 50))
        self.rbAllDay.setObjectName("rbAllDay")
        self.rbOneDay = QtWidgets.QRadioButton(self.grcdControl)
        self.rbOneDay.setGeometry(QtCore.QRect(30, 5, 141, 50))
        self.rbOneDay.setChecked(True)
        self.rbOneDay.setObjectName("rbOneDay")

        self.retranslateUi(setThongGio)
        QtCore.QMetaObject.connectSlotsByName(setThongGio)

    def retranslateUi(self, setThongGio):
        _translate = QtCore.QCoreApplication.translate
        setThongGio.setWindowTitle(_translate("setThongGio", "Form"))
        self.btKichHoat.setText(_translate("setThongGio", "Kích hoạt"))
        self.btExit.setText(_translate("setThongGio", "Thoát"))
        self.tbPhut.setText(_translate("setThongGio", "10"))
        self.tbTimes.setText(_translate("setThongGio", "5"))
        self.tbGio.setText(_translate("setThongGio", "10"))
        self.rbAllDay.setText(_translate("setThongGio", "Tất cả ngày"))
        self.rbOneDay.setText(_translate("setThongGio", "1 Ngày"))
        
        self.setEvent()
    
    def setEvent(self):
        self.btExit.clicked.connect(self.btExit_click)
        self.tbGio.clicked.connect(self.tbGio_click)
        self.tbTimes.clicked.connect(self.tbTimes_click)
        self.tbPhut.clicked.connect(self.tbPhut_click)
        self.btKichHoat.clicked.connect(self.btKichHoat_click)
        timeThongGio = uart.dataAllJsonConfig["timeThongGio"]
        self.timeSplit = timeThongGio.split(':')
        self.tbGio.setText(self.timeSplit[0])
        self.tbPhut.setText(self.timeSplit[1])
        self.tbTimes.setText(self.timeSplit[2])
        if self.timeSplit[3] == '0': # ko kich hoat thong gio
            self.btKichHoat.setText("Kích hoạt")
            self.kichHoat = False
        else : #trang thai thong gio da kich hoat roi
            self.btKichHoat.setText("Bỏ\nKích hoạt")
            self.kichHoat = True

    def tbPhut_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbPhut.setText(value)
            self.timeSplit[1] = str(value)
    def tbTimes_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbTimes.setText(value)
            self.timeSplit[2] = str(value)
    def tbGio_click(self):
        dialogKey= Ui_Dialog(24)
        value = dialogKey.exec_()
        if value :
            self.tbGio.setText(value)
            self.timeSplit[0] = str(value)
   
    def btKichHoat_click(self):
        if self.kichHoat :
            self.btKichHoat.setText("Bỏ\nKích hoạt")
            self.timeSplit[3] = '1'
        else :
            self.btKichHoat.setText("Kích hoạt")
            self.timeSplit[3] = '0'
        self.kichHoat = not self.kichHoat
    def btExit_click(self):
        dtstr = self.timeSplit[0] +":"+ self.timeSplit[1] +":"+self.timeSplit[2]+":"+self.timeSplit[3] 
        uart.dataAllJsonConfig["timeThongGio"] = dtstr
        uart.saveConfig()
        print("save thong gio done ", uart.dataAllJsonConfig["timeThongGio"])
        self.setThongGio.close()


import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setThongGio = QtWidgets.QWidget()
    ui = Ui_setThongGio()
    ui.setupUi(setThongGio)
    setThongGio.show()
    sys.exit(app.exec_())
"""

