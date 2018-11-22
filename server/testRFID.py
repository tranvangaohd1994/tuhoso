# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setTime.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
from time import strftime
from subprocess import call

from kbNumber import Ui_Dialog

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setTime(object):
    def setupUi(self, setTime):
        setTime.setObjectName("setTime")
        setTime.resize(1280, 800)
        setTime.setStyleSheet("")
        self.setTime =  setTime
        self.frame = QtWidgets.QFrame(setTime)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}.QPushButton:pressed { background-color: #4164ff}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt  \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-17, 120, 1321, 71))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(520, 310, 241, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(700, 310, 541, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(400, 650, 181, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(710, 650, 181, 101))
        self.btExit.setObjectName("btExit")
        self.tbPhut = QtWidgets.QLineEdit(self.frame)
        self.tbPhut.setGeometry(QtCore.QRect(560, 370, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbPhut.setFont(font)
        self.tbPhut.setObjectName("tbPhut")
        self.tbSecond = QtWidgets.QLineEdit(self.frame)
        self.tbSecond.setGeometry(QtCore.QRect(890, 370, 161, 61))
        
        self.tbSecond.setFont(font)
        self.tbSecond.setObjectName("tbSecond")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 310, 361, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbGio = QtWidgets.QLineEdit(self.frame)
        self.tbGio.setGeometry(QtCore.QRect(210, 370, 191, 61))
        
        self.tbGio.setFont(font)
        self.tbGio.setObjectName("tbGio")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(470, 470, 351, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(700, 470, 541, 50))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tbMonth = QtWidgets.QLineEdit(self.frame)
        self.tbMonth.setGeometry(QtCore.QRect(560, 540, 171, 61))
        
        self.tbMonth.setFont(font)
        self.tbMonth.setObjectName("tbMonth")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 470, 361, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tbDay = QtWidgets.QLineEdit(self.frame)
        self.tbDay.setGeometry(QtCore.QRect(210, 540, 191, 61))
        
        self.tbDay.setFont(font)
        self.tbDay.setObjectName("tbDay")
        self.tbYear = QtWidgets.QLineEdit(self.frame)
        self.tbYear.setGeometry(QtCore.QRect(890, 540, 161, 61))
        
        self.tbYear.setFont(font)
        self.tbYear.setObjectName("tbYear")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(160, 240, 361, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lbTimeNow = QtWidgets.QLabel(self.frame)
        self.lbTimeNow.setGeometry(QtCore.QRect(540, 240, 541, 50))
        self.lbTimeNow.setStyleSheet("")
        self.lbTimeNow.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTimeNow.setObjectName("lbTimeNow")

        self.retranslateUi(setTime)
        QtCore.QMetaObject.connectSlotsByName(setTime)

    def retranslateUi(self, setTime):
        _translate = QtCore.QCoreApplication.translate
        setTime.setWindowTitle(_translate("setTime", "Form"))
        self.label.setText(_translate("setTime", "Điều chỉnh thời gian"))
        self.label_2.setText(_translate("setTime", "Phút"))
        self.label_4.setText(_translate("setTime", "Giây"))
        self.btSave.setText(_translate("setTime", "Lưu"))
        self.btExit.setText(_translate("setTime", "Thoát"))
        self.tbPhut.setText(_translate("setTime", "10"))
        self.tbSecond.setText(_translate("setTime", "5"))
        self.label_6.setText(_translate("setTime", "Giờ"))
        self.tbGio.setText(_translate("setTime", "10"))
        self.label_3.setText(_translate("setTime", "Tháng"))
        self.label_5.setText(_translate("setTime", "Năm"))
        self.tbMonth.setText(_translate("setTime", "10"))
        self.label_7.setText(_translate("setTime", "Ngày"))
        self.tbDay.setText(_translate("setTime", "10"))
        self.tbYear.setText(_translate("setTime", "2018"))
        self.label_8.setText(_translate("setTime", "Thời gian hiện tại :"))
        self.lbTimeNow.setText(_translate("setTime", "11:23:21 09/10/2018"))
        

import resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setTime = QtWidgets.QWidget()
    ui = Ui_setTime()
    ui.setupUi(setTime)
    setTime.show()
    sys.exit(app.exec_())

