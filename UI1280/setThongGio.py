# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setThongGio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setThongGio(object):
    def setupUi(self, setThongGio):
        setThongGio.setObjectName("setThongGio")
        setThongGio.resize(1280, 800)
        setThongGio.setStyleSheet("")
        self.setThongGio = setThongGio
        self.frame = QtWidgets.QFrame(setThongGio)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}.QPushButton:pressed { background-color: #4164ff}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1301, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 380, 351, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(160, 470, 541, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btKichHoat = QtWidgets.QPushButton(self.frame)
        self.btKichHoat.setGeometry(QtCore.QRect(860, 630, 151, 101))
        self.btKichHoat.setObjectName("btKichHoat")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1070, 630, 151, 101))
        self.btExit.setObjectName("btExit")
        self.tbPhut = QtWidgets.QLineEdit(self.frame)
        self.tbPhut.setGeometry(QtCore.QRect(710, 370, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbPhut.setFont(font)
        self.tbPhut.setObjectName("tbPhut")
        self.tbTimes = QtWidgets.QLineEdit(self.frame)
        self.tbTimes.setGeometry(QtCore.QRect(710, 460, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbTimes.setFont(font)
        self.tbTimes.setObjectName("tbTimes")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(230, 290, 361, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbGio = QtWidgets.QLineEdit(self.frame)
        self.tbGio.setGeometry(QtCore.QRect(710, 280, 321, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbGio.setFont(font)
        self.tbGio.setObjectName("tbGio")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(30, 610, 511, 121))
        self.grcdControl.setStyleSheet("QLabel{color: rgb(255, 255, 255);font: 75 Bold 20pt \"Ubuntu\";}.QRadioButton{font: 75 Bold 20pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}\n"
"")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbAllDay = QtWidgets.QRadioButton(self.grcdControl)
        self.rbAllDay.setGeometry(QtCore.QRect(310, 10, 191, 100))
        self.rbAllDay.setObjectName("rbAllDay")
        self.rbOneDay = QtWidgets.QRadioButton(self.grcdControl)
        self.rbOneDay.setGeometry(QtCore.QRect(30, 10, 201, 100))
        self.rbOneDay.setChecked(True)
        self.rbOneDay.setObjectName("rbOneDay")

        self.retranslateUi(setThongGio)
        QtCore.QMetaObject.connectSlotsByName(setThongGio)

    def retranslateUi(self, setThongGio):
        _translate = QtCore.QCoreApplication.translate
        setThongGio.setWindowTitle(_translate("setThongGio", "Form"))
        self.label.setText(_translate("setThongGio", "Cài đặt thông gió"))
        self.label_2.setText(_translate("setThongGio", "Phút"))
        self.label_4.setText(_translate("setThongGio", "Thời gian thông gió(Phút)"))
        self.btKichHoat.setText(_translate("setThongGio", "Kích hoạt"))
        self.btExit.setText(_translate("setThongGio", "Thoát"))
        self.tbPhut.setText(_translate("setThongGio", "10"))
        self.tbTimes.setText(_translate("setThongGio", "5"))
        self.label_6.setText(_translate("setThongGio", "Giờ"))
        self.tbGio.setText(_translate("setThongGio", "10"))
        self.rbAllDay.setText(_translate("setThongGio", "Tất cả ngày"))
        self.rbOneDay.setText(_translate("setThongGio", "1 Ngày"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setThongGio = QtWidgets.QWidget()
    ui = Ui_setThongGio()
    ui.setupUi(setThongGio)
    setThongGio.show()
    sys.exit(app.exec_())

