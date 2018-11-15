# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setTocDoDC.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setTocDoDc(object):
    def setupUi(self, setTocDoDc):
        setTocDoDc.setObjectName("setTocDoDc")
        setTocDoDc.resize(1280, 800)
        setTocDoDc.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setTocDoDc)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";\n"
        "background-color: rgb(0, 0, 0);\n"
        "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 421, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 590, 421, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 450, 431, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(470, 660, 161, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(740, 660, 161, 101))
        self.btExit.setObjectName("btExit")
        self.tbKCHienTai = QtWidgets.QLineEdit(self.frame)
        self.tbKCHienTai.setGeometry(QtCore.QRect(70, 330, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCHienTai.setFont(font)
        self.tbKCHienTai.setObjectName("tbKCHienTai")
        self.tbKCCaiDat = QtWidgets.QLineEdit(self.frame)
        self.tbKCCaiDat.setGeometry(QtCore.QRect(70, 520, 421, 61))
       
        self.tbKCCaiDat.setFont(font)
        self.tbKCCaiDat.setObjectName("tbKCCaiDat")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(890, 260, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(setTocDoDc)
        QtCore.QMetaObject.connectSlotsByName(setTocDoDc)

    def retranslateUi(self, setTocDoDc):
        _translate = QtCore.QCoreApplication.translate
        setTocDoDc.setWindowTitle(_translate("setTocDoDc", "Form"))
        self.label.setText(_translate("setTocDoDc", "Cài đặt tốc độ động cơ"))
        self.label_2.setText(_translate("setTocDoDc", "Hiện đang cài đặt"))
        self.label_3.setText(_translate("setTocDoDc", "Giá trị : 1-10"))
        self.label_4.setText(_translate("setTocDoDc", "Nhập tốc độ"))
        self.btSave.setText(_translate("setTocDoDc", "Lưu"))
        self.btExit.setText(_translate("setTocDoDc", "Thoát"))
        self.tbKCHienTai.setText(_translate("setTocDoDc", "8"))
        self.label_5.setText(_translate("setTocDoDc", "Hướng dẫn"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setTocDoDc = QtWidgets.QWidget()
    ui = Ui_setTocDoDc()
    ui.setupUi(setTocDoDc)
    setTocDoDc.show()
    sys.exit(app.exec_())

