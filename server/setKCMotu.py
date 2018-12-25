# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setKCMoTu.ui'
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

class Ui_setKCMoTu(object):
    def setupUi(self, setKCMoTu):
        setKCMoTu.setObjectName("setKCMoTu")
        setKCMoTu.resize(1280, 800)
        setKCMoTu.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setKCMoTu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/kcmt.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 15px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}.MyQLineEdit{border: 2px solid black;border-radius: 10px;padding: 0 8px;font: bold 32px \"Arial\"; text-align: center;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(210, 620, 161, 81))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(415, 620, 161, 81))
        self.btExit.setObjectName("btExit")
        self.tbKCHienTai = MyQLineEdit(self.frame)
        self.tbKCHienTai.setGeometry(QtCore.QRect(390, 330, 261, 81))
        self.tbKCHienTai.setObjectName("tbKCHienTai")
        self.tbKCCaiDat = MyQLineEdit(self.frame)
        self.tbKCCaiDat.setGeometry(QtCore.QRect(390, 430, 261, 81))
        
        self.tbKCCaiDat.setObjectName("tbKCCaiDat")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(70, 550, 681, 60))
        self.grcdControl.setStyleSheet("#grcdControl{background-color:#ffffff;border-radius: 5px;}\n"
        ".QRadioButton {background-color:white;color:#4e9400;font:bold 24px \"Arial\";}.QRadioButton::indicator{width:30px;height:30px;border-radius:20px;} .QRadioButton::indicator:checked{background-color:       red;border: 2px solid #4e9400;}\n"
        ".QRadioButton::indicator:unchecked {border: 2px solid #4e9400;border-radius: 20px;}\n"
        "")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbTuPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuPhai.setGeometry(QtCore.QRect(260, 5, 181, 50))
        self.rbTuPhai.setObjectName("rbTuPhai")
        self.rbTuTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuTrai.setGeometry(QtCore.QRect(20, 5, 181, 50))
        self.rbTuTrai.setChecked(True)
        self.rbTuTrai.setObjectName("rbTuTrai")
        self.rbToanBo = QtWidgets.QRadioButton(self.grcdControl)
        self.rbToanBo.setGeometry(QtCore.QRect(470, 5, 181, 50))
        self.rbToanBo.setObjectName("rbToanBo")

        self.retranslateUi(setKCMoTu)
        QtCore.QMetaObject.connectSlotsByName(setKCMoTu)

    def retranslateUi(self, setKCMoTu):
        _translate = QtCore.QCoreApplication.translate
        setKCMoTu.setWindowTitle(_translate("setKCMoTu", "Form"))
        self.btSave.setText(_translate("setKCMoTu", "Lưu"))
        self.btExit.setText(_translate("setKCMoTu", "Thoát"))
        self.tbKCHienTai.setText(_translate("setKCMoTu", "8"))
        self.rbTuPhai.setText(_translate("setKCMoTu", "Dãy Phải"))
        self.rbTuTrai.setText(_translate("setKCMoTu", "Dãy Trái"))
        self.rbToanBo.setText(_translate("setKCMoTu", "Toàn bộ"))

        self.setEvent()
        self.btExit.clicked.connect(setKCMoTu.close)

    def setEvent(self):
        self.tbKCHienTai.setText(str(int(server.dataSent2Client["Left_1"].dt2Pi2Ar[3])))

        self.tbKCCaiDat.clicked.connect(self.tbKCCaiDat_click)
        self.btSave.clicked.connect(self.btSave_click)
    def tbKCCaiDat_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbKCCaiDat.setText(value)

    def btSave_click(self):
        if len(self.tbKCCaiDat.text()) > 0 :
            if self.rbToanBo.isChecked():
                for tu in server.allConnection:
                    server.dataSent2Client[tu].dt2Pi2Ar[3] = int(self.tbKCCaiDat.text())
                    server.serverMain.sendMes2Client(tu , b'\xee\xee'+bytes(server.dataSent2Client[tu].dt2Pi2Ar))    

            elif  self.rbTuTrai.isChecked():
                for i in range(1,server.numClientLeft+1):
                    nameTu = "Left_"+str(i)
                    server.dataSent2Client[nameTu].dt2Pi2Ar[3] = int(self.tbKCCaiDat.text())
                    server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
           
            elif self.rbTuPhai.isChecked():
                for i in range(1,server.numClientRight+1):
                    nameTu = "Right_"+str(i)
                    server.dataSent2Client[nameTu].dt2Pi2Ar[3] = int(self.tbKCCaiDat.text())
                    server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
            
            dialog = MSG_Dialog()
            dialog.exec_()
import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setKCMoTu = QtWidgets.QWidget()
    ui = Ui_setKCMoTu()
    ui.setupUi(setKCMoTu)
    setKCMoTu.show()
    sys.exit(app.exec_())

"""