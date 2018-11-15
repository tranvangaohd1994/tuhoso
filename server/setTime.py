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
        setTime.resize(1024, 600)
        setTime.setStyleSheet("")
        self.setTime =  setTime
        self.frame = QtWidgets.QFrame(setTime)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}.QPushButton:pressed { background-color: #4164ff}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 90, 1024, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(400, 230, 241, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(580, 230, 541, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(280, 480, 151, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(620, 480, 151, 101))
        self.btExit.setObjectName("btExit")
        self.tbPhut = MyQLineEdit(self.frame)
        self.tbPhut.setGeometry(QtCore.QRect(440, 280, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbPhut.setFont(font)
        self.tbPhut.setObjectName("tbPhut")
        self.tbSecond = MyQLineEdit(self.frame)
        self.tbSecond.setGeometry(QtCore.QRect(770, 280, 161, 61))
       
        self.tbSecond.setFont(font)
        self.tbSecond.setObjectName("tbSecond")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 230, 361, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbGio = MyQLineEdit(self.frame)
        self.tbGio.setGeometry(QtCore.QRect(90, 280, 191, 61))
        
        self.tbGio.setFont(font)
        self.tbGio.setObjectName("tbGio")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(350, 360, 351, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(580, 360, 541, 50))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tbMonth = MyQLineEdit(self.frame)
        self.tbMonth.setGeometry(QtCore.QRect(440, 410, 171, 61))
       
        self.tbMonth.setFont(font)
        self.tbMonth.setObjectName("tbMonth")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 360, 361, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.tbDay = MyQLineEdit(self.frame)
        self.tbDay.setGeometry(QtCore.QRect(90, 410, 191, 61))
        
        self.tbDay.setFont(font)
        self.tbDay.setObjectName("tbDay")
        self.tbYear = MyQLineEdit(self.frame)
        self.tbYear.setGeometry(QtCore.QRect(770, 410, 161, 61))
       
        self.tbYear.setFont(font)
        self.tbYear.setObjectName("tbYear")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 170, 361, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.lbTimeNow = QtWidgets.QLabel(self.frame)
        self.lbTimeNow.setGeometry(QtCore.QRect(410, 170, 541, 50))
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
        self.setEvent()

    def setEvent(self):
        self.btExit.clicked.connect(self.btExit_click)
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.showTime)
        self.ctimer.start(1000)
        self.btSave.clicked.connect(self.btSave_click)

        self.tbDay.clicked.connect(self.btDay_click)
        self.tbGio.clicked.connect(self.btGio_click)
        self.tbMonth.clicked.connect(self.btMonth_click)
        self.tbPhut.clicked.connect(self.btPhut_click)
        self.tbSecond.clicked.connect(self.btSecond_click)
        self.tbYear.clicked.connect(self.btYear_click)

    def btDay_click(self):
        dialogKey= Ui_Dialog(31)
        value = dialogKey.exec_()
        if value :
            self.tbDay.setText(value)

    def btGio_click(self):
        dialogKey= Ui_Dialog(24)
        value = dialogKey.exec_()
        if value :
            self.tbGio.setText(value)

    def btMonth_click(self):
        dialogKey= Ui_Dialog(12)
        value = dialogKey.exec_()
        if value :
            self.tbMonth.setText(value)

    def btPhut_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbPhut.setText(value)

    def btSecond_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbSecond.setText(value)
            
    def btYear_click(self):
        dialogKey= Ui_Dialog(3000)
        value = dialogKey.exec_()
        if value :
            self.tbYear.setText(value)

    def showTime(self):
        _date = strftime("%H:%M:%S , %d/%m/%Y")
        self.lbTimeNow.setText(str(_date))

    def btExit_click(self):
        self.ctimer.stop()
        self.setTime.close()

    def btSave_click(self):
        _date = "sudo hwclock --set --date "
        _date += '\"'+  str(self.tbYear.text()) + '-' + str(self.tbMonth.text()) + '-' + str(self.tbDay.text()) + ' '
        _date += str(self.tbGio.text()) + ':' + str(self.tbPhut.text()) + ':' + str(self.tbSecond.text())+ '+0700\"'

        call(_date ,shell=True)
        call('sudo hwclock -r',shell=True)
        call('sudo hwclock -s',shell=True)
        pass

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setTime = QtWidgets.QWidget()
    ui = Ui_setTime()
    ui.setupUi(setTime)
    setTime.show()
    sys.exit(app.exec_())

"""