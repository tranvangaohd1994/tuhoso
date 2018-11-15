# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setThemTu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setThemTu(object):
    def setupUi(self, setThemTu):
        setThemTu.setObjectName("setThemTu")
        setThemTu.resize(1280, 800)
        setThemTu.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setThemTu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 34pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1280, 71))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btThem = QtWidgets.QPushButton(self.frame)
        self.btThem.setGeometry(QtCore.QRect(490, 600, 211, 101))
        self.btThem.setObjectName("btThem")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(90, 600, 171, 101))
        self.btExit.setObjectName("btExit")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(460, 260, 661, 121))
        self.grcdControl.setStyleSheet("QLabel{color: rgb(255, 255, 255);font: 75 Bold 20pt \"Ubuntu\";}.QRadioButton{font: 75 Bold 20pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}\n"
"")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbbenPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbbenPhai.setGeometry(QtCore.QRect(430, 10, 191, 100))
        self.rbbenPhai.setObjectName("rbbenPhai")
        self.rbBenTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbBenTrai.setGeometry(QtCore.QRect(30, 10, 201, 100))
        self.rbBenTrai.setChecked(True)
        self.rbBenTrai.setObjectName("rbBenTrai")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 341, 191))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.btXoa = QtWidgets.QPushButton(self.frame)
        self.btXoa.setGeometry(QtCore.QRect(890, 600, 191, 101))
        self.btXoa.setObjectName("btXoa")
        self.lbTrai = QtWidgets.QLabel(self.frame)
        self.lbTrai.setGeometry(QtCore.QRect(560, 410, 101, 61))
        self.lbTrai.setStyleSheet("")
        self.lbTrai.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbTrai.setObjectName("lbTrai")
        self.lbPhai = QtWidgets.QLabel(self.frame)
        self.lbPhai.setGeometry(QtCore.QRect(950, 410, 101, 61))
        self.lbPhai.setStyleSheet("")
        self.lbPhai.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbPhai.setObjectName("lbPhai")

        self.retranslateUi(setThemTu)
        QtCore.QMetaObject.connectSlotsByName(setThemTu)

    def retranslateUi(self, setThemTu):
        _translate = QtCore.QCoreApplication.translate
        setThemTu.setWindowTitle(_translate("setThemTu", "Form"))
        self.label.setText(_translate("setThemTu", "Quản lý hệ thống giá"))
        self.btThem.setText(_translate("setThemTu", "Thêm  1 cột"))
        self.btExit.setText(_translate("setThemTu", "Thoát"))
        self.rbbenPhai.setText(_translate("setThemTu", "Bên Phải"))
        self.rbBenTrai.setText(_translate("setThemTu", "Bên Trái"))
        self.label_6.setText(_translate("setThemTu", "Số cột hiện tại\n"
"so với tủ Master:"))
        self.btXoa.setText(_translate("setThemTu", "Xóa 1 cột"))
        self.lbTrai.setText(_translate("setThemTu", "2"))
        self.lbPhai.setText(_translate("setThemTu", "0"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setThemTu = QtWidgets.QWidget()
    ui = Ui_setThemTu()
    ui.setupUi(setThemTu)
    setThemTu.show()
    sys.exit(app.exec_())

