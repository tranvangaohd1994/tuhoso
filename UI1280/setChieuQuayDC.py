# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setChieuQuayDC.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setChieuQuayDC(object):
    def setupUi(self, setChieuQuayDC):
        setChieuQuayDC.setObjectName("setChieuQuayDC")
        setChieuQuayDC.resize(1280, 800)
        setChieuQuayDC.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setChieuQuayDC)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 34pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 120, 1280, 71))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(220, 580, 171, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(480, 580, 171, 101))
        self.btExit.setObjectName("btExit")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(890, 250, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(160, 360, 511, 121))
        self.grcdControl.setStyleSheet("QLabel{color: rgb(255, 255, 255);font: 75 Bold 20pt \"Ubuntu\";}.QRadioButton{font: 75 Bold 20pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbstSpinRight = QtWidgets.QRadioButton(self.grcdControl)
        self.rbstSpinRight.setGeometry(QtCore.QRect(310, 10, 191, 100))
        self.rbstSpinRight.setObjectName("rbstSpinRight")
        self.rbstSpinLeft = QtWidgets.QRadioButton(self.grcdControl)
        self.rbstSpinLeft.setGeometry(QtCore.QRect(30, 10, 201, 100))
        self.rbstSpinLeft.setChecked(True)
        self.rbstSpinLeft.setObjectName("rbstSpinLeft")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 250, 701, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(setChieuQuayDC)
        QtCore.QMetaObject.connectSlotsByName(setChieuQuayDC)

    def retranslateUi(self, setChieuQuayDC):
        _translate = QtCore.QCoreApplication.translate
        setChieuQuayDC.setWindowTitle(_translate("setChieuQuayDC", "Form"))
        self.label.setText(_translate("setChieuQuayDC", "Cài đặt chiều quay động cơ"))
        self.btSave.setText(_translate("setChieuQuayDC", "Lưu"))
        self.btExit.setText(_translate("setChieuQuayDC", "Thoát"))
        self.label_5.setText(_translate("setChieuQuayDC", "Hướng dẫn"))
        self.rbstSpinRight.setText(_translate("setChieuQuayDC", "Quay Thuận"))
        self.rbstSpinLeft.setText(_translate("setChieuQuayDC", "Quay Nghịch"))
        self.label_6.setText(_translate("setChieuQuayDC", "Cài đặt chiều quay động cơ mở tủ"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setChieuQuayDC = QtWidgets.QWidget()
    ui = Ui_setChieuQuayDC()
    ui.setupUi(setChieuQuayDC)
    setChieuQuayDC.show()
    sys.exit(app.exec_())

