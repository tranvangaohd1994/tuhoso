# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setTocDoDC.ui'
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

class Ui_setTocDoDc(object):
    def setupUi(self, setTocDoDc):
        setTocDoDc.setObjectName("setTocDoDc")
        setTocDoDc.resize(1280, 800)
        setTocDoDc.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setTocDoDc)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}#tbKCCaiDat{background-color:#B2FF59;font: 75 32pt \"Arial\";}\n"
            "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 250, 421, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 560, 421, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 420, 431, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(850, 640, 161, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1060, 640, 161, 101))
        self.btExit.setObjectName("btExit")
        self.tbKCHienTai = MyQLineEdit(self.frame)
        self.tbKCHienTai.setGeometry(QtCore.QRect(70, 310, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCHienTai.setFont(font)
        self.tbKCHienTai.setObjectName("tbKCHienTai")
        self.tbKCCaiDat = MyQLineEdit(self.frame)
        self.tbKCCaiDat.setGeometry(QtCore.QRect(70, 490, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbKCCaiDat.setFont(font)
        self.tbKCCaiDat.setObjectName("tbKCCaiDat")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(850, 250, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(50, 640, 481, 121))
        self.grcdControl.setStyleSheet(".QRadioButton{font: 75 Bold 26pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbTuPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuPhai.setGeometry(QtCore.QRect(260, 10, 181, 100))
        self.rbTuPhai.setObjectName("rbTuPhai")
        self.rbTuTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuTrai.setGeometry(QtCore.QRect(20, 10, 181, 100))
        self.rbTuTrai.setChecked(True)
        self.rbTuTrai.setObjectName("rbTuTrai")

        self.retranslateUi(setTocDoDc)
        QtCore.QMetaObject.connectSlotsByName(setTocDoDc)
        self.btExit.clicked.connect(setTocDoDc.close)
        
    def retranslateUi(self, setTocDoDc):
        _translate = QtCore.QCoreApplication.translate
        setTocDoDc.setWindowTitle(_translate("setTocDoDc", "Form"))
        self.label.setText(_translate("setTocDoDc", "Cài đặt tốc độ động cơ"))
        self.label_2.setText(_translate("setTocDoDc", "Hiện đang cài đặt"))
        self.label_3.setText(_translate("setTocDoDc", "Giá trị : 1-10"))
        self.label_4.setText(_translate("setTocDoDc", "Nhập tốc độ"))
        self.btSave.setText(_translate("setTocDoDc", "Lưu"))
        self.btExit.setText(_translate("setTocDoDc", "Thoát"))
        self.label_5.setText(_translate("setTocDoDc", "Hướng dẫn"))
        self.rbTuPhai.setText(_translate("setTocDoDc", "Tủ phải"))
        self.rbTuTrai.setText(_translate("setTocDoDc", "Tủ trái"))

        self.setEvent()

    def setEvent(self):
        if self.rbTuTrai.isChecked() and server.numClientLeft > 0 :
            self.tbKCHienTai.setText(str(int(server.dataSent2Client["Left_1"].dt2Pi2Ar[6])))
        elif self.rbTuPhai.isChecked() and server.numClientRight > 0:
            self.tbKCHienTai.setText(str(int(server.dataSent2Client["Right_1"].dt2Pi2Ar[6])))
        else :
            self.tbKCHienTai.setText('0')

        self.tbKCCaiDat.clicked.connect(self.tbKCCaiDat_click)
        self.btSave.clicked.connect(self.btSave_click)
    def tbKCCaiDat_click(self):
        dialogKey= Ui_Dialog(10)
        value = dialogKey.exec_()
        if value :
            self.tbKCCaiDat.setText(value)
    def btSave_click(self):
        #neu tu duoc chon cai dat thi se luu cai dat va gui cho tu do
        if self.rbTuTrai.isChecked():
            firstName = 'Left_'
            maxTu = server.numClientLeft
        else :
            firstName = 'Right_'
            maxTu = server.numClientRight

        for i in range(1,maxTu+1):
            nameTu = firstName+str(i)
            server.dataSent2Client[nameTu].dt2Pi2Ar[6] = int(self.tbKCCaiDat.text())
            server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))

        dialog = MSG_Dialog()
        dialog.exec_()




import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setTocDoDc = QtWidgets.QWidget()
    ui = Ui_setTocDoDc()
    ui.setupUi(setTocDoDc)
    setTocDoDc.show()
    sys.exit(app.exec_())

"""