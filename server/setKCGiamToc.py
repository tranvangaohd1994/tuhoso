# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setKCGiamToc.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from kbNumber import Ui_Dialog , MSG_Dialog
from PyQt5.QtCore import pyqtSignal
import server

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setKCGiamToc(object):
    def setupUi(self, setKCGiamToc):
        setKCGiamToc.setObjectName("setKCGiamToc")
        setKCGiamToc.resize(1280, 800)
        setKCGiamToc.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setKCGiamToc)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 421, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 580, 421, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 420, 421, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(830, 640, 141, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1100, 640, 131, 101))
        self.btExit.setObjectName("btExit")
        self.tbKCHienTai = MyQLineEdit(self.frame)
        self.tbKCHienTai.setGeometry(QtCore.QRect(50, 300, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCHienTai.setFont(font)
        self.tbKCHienTai.setObjectName("tbKCHienTai")
        self.tbKCCaiDat = MyQLineEdit(self.frame)
        self.tbKCCaiDat.setGeometry(QtCore.QRect(50, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCCaiDat.setFont(font)
        self.tbKCCaiDat.setObjectName("tbKCCaiDat")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(830, 230, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(setKCGiamToc)
        QtCore.QMetaObject.connectSlotsByName(setKCGiamToc)
        self.btExit.clicked.connect(setKCGiamToc.close)

    def retranslateUi(self, setKCGiamToc):
        _translate = QtCore.QCoreApplication.translate
        setKCGiamToc.setWindowTitle(_translate("setKCGiamToc", "Form"))
        self.label.setText(_translate("setKCGiamToc", "Cài đặt khoảng cách giảm tốc"))
        self.label_2.setText(_translate("setKCGiamToc", "Hiện đang cài đặt"))
        self.label_3.setText(_translate("setKCGiamToc", "Giá trị : 1-100"))
        self.label_4.setText(_translate("setKCGiamToc", "Nhập Khoảng cách"))
        self.btSave.setText(_translate("setKCGiamToc", "Lưu"))
        self.btExit.setText(_translate("setKCGiamToc", "Thoát"))
        self.label_5.setText(_translate("setKCGiamToc", "Hướng dẫn"))
        
        self.setEvent()

    def setEvent(self):
        
        self.tbKCHienTai.setText(str(int(server.dataSent2Client["Left_1"].dt2Pi2Ar[7])))
        self.tbKCCaiDat.clicked.connect(self.tbKCCaiDat_click)
        self.btSave.clicked.connect(self.btSave_click)
    def tbKCCaiDat_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbKCCaiDat.setText(value)
    def btSave_click(self):
        for i in range(1,server.numClientLeft+1):
            nameTu = "Left_"+str(i)
            server.dataSent2Client[nameTu].dt2Pi2Ar[7] = int(self.tbKCCaiDat.text())
            
            server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
        
        dialog = MSG_Dialog()
        dialog.exec_()




import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setKCGiamToc = QtWidgets.QWidget()
    ui = Ui_setKCGiamToc()
    ui.setupUi(setKCGiamToc)
    setKCGiamToc.show()
    sys.exit(app.exec_())

"""