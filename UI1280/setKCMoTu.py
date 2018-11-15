# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setKCMoTu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setKCMoTu(object):
    def setupUi(self, setKCMoTu):
        setKCMoTu.setObjectName("setKCMoTu")
        setKCMoTu.resize(1280, 800)
        setKCMoTu.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setKCMoTu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 120, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";\n"
            "background-color: rgb(0, 0, 0);\n"
            "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 230, 421, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 570, 421, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 420, 421, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(850, 650, 151, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1070, 650, 141, 101))
        self.btExit.setObjectName("btExit")
        self.tbKCHienTai = QtWidgets.QLineEdit(self.frame)
        self.tbKCHienTai.setGeometry(QtCore.QRect(60, 300, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCHienTai.setFont(font)
        self.tbKCHienTai.setObjectName("tbKCHienTai")
        self.tbKCCaiDat = QtWidgets.QLineEdit(self.frame)
        self.tbKCCaiDat.setGeometry(QtCore.QRect(60, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCCaiDat.setFont(font)
        self.tbKCCaiDat.setObjectName("tbKCCaiDat")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(830, 260, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(setKCMoTu)
        QtCore.QMetaObject.connectSlotsByName(setKCMoTu)

    def retranslateUi(self, setKCMoTu):
        _translate = QtCore.QCoreApplication.translate
        setKCMoTu.setWindowTitle(_translate("setKCMoTu", "Form"))
        self.label.setText(_translate("setKCMoTu", "Cài đặt khoảng cách mở tủ"))
        self.label_2.setText(_translate("setKCMoTu", "Hiện đang cài đặt"))
        self.label_3.setText(_translate("setKCMoTu", "Giá trị : 30-100"))
        self.label_4.setText(_translate("setKCMoTu", "Nhập Khoảng cách"))
        self.btSave.setText(_translate("setKCMoTu", "Lưu"))
        self.btExit.setText(_translate("setKCMoTu", "Thoát"))
        self.tbKCHienTai.setText(_translate("setKCMoTu", "80"))
        self.label_5.setText(_translate("setKCMoTu", "Hướng dẫn"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setKCMoTu = QtWidgets.QWidget()
    ui = Ui_setKCMoTu()
    ui.setupUi(setKCMoTu)
    setKCMoTu.show()
    sys.exit(app.exec_())

