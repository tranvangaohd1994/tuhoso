# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setDieuKienVanHanh.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from kbNumber import Ui_Dialog

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setDieuKienVanHanh(object):
    def setupUi(self, setDieuKienVanHanh):
        setDieuKienVanHanh.setObjectName("setDieuKienVanHanh")
        setDieuKienVanHanh.resize(1280, 800)
        setDieuKienVanHanh.setStyleSheet("")
        self.setDieuKienVanHanh = setDieuKienVanHanh

        
        self.frame = QtWidgets.QFrame(setDieuKienVanHanh)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/cdmtvh.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 15px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}.MyQLineEdit{border: 2px solid black;border-radius: 10px;padding: 0 8px;font: bold 32px \"Arial\"; text-align: center;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(300, 630, 161, 81))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(520, 630, 161, 81))
        self.btExit.setObjectName("btExit")
        self.tbTempFrom = MyQLineEdit(self.frame)
        self.tbTempFrom.setGeometry(QtCore.QRect(305, 390, 151, 81))
        self.tbTempFrom.setObjectName("tbTempFrom")
        self.tbTempTo = MyQLineEdit(self.frame)
        self.tbTempTo.setGeometry(QtCore.QRect(520, 390, 151, 81))
        self.tbTempTo.setObjectName("tbTempTo")
        self.tbHumiTo = MyQLineEdit(self.frame)
        self.tbHumiTo.setGeometry(QtCore.QRect(520, 520, 151, 81))
        self.tbHumiTo.setObjectName("tbHumiTo")
        self.tbHumiFrom = MyQLineEdit(self.frame)
        self.tbHumiFrom.setGeometry(QtCore.QRect(305, 520, 151, 81))
        self.tbHumiFrom.setObjectName("tbHumiFrom")

        self.retranslateUi(setDieuKienVanHanh)
        QtCore.QMetaObject.connectSlotsByName(setDieuKienVanHanh)

    def retranslateUi(self, setDieuKienVanHanh):
        _translate = QtCore.QCoreApplication.translate
        setDieuKienVanHanh.setWindowTitle(_translate("setDieuKienVanHanh", "Form"))
        self.btSave.setText(_translate("setDieuKienVanHanh", "Lưu"))
        self.btExit.setText(_translate("setDieuKienVanHanh", "Thoát"))
        self.tbTempFrom.setText(_translate("setDieuKienVanHanh", ""))
        self.tbTempTo.setText(_translate("setDieuKienVanHanh", ""))
        self.tbHumiTo.setText(_translate("setDieuKienVanHanh", ""))
        self.tbHumiFrom.setText(_translate("setDieuKienVanHanh", ""))

        self.setEvent()

    def setEvent(self) :
        self.btExit.clicked.connect(self.setDieuKienVanHanh.close)

        self.tbTempTo.clicked.connect(self.tbTempTo_click)
        self.tbTempFrom.clicked.connect(self.tbTempFrom_click)
        self.tbHumiTo.clicked.connect(self.tbHumiTo_click)
        self.tbHumiFrom.clicked.connect(self.tbHumiFrom_click)

        self.btSave.clicked.connect(self.btSave_click)
        self.kichHoat = False

    def tbTempTo_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbTempTo.setText(value)

    def tbTempFrom_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbTempFrom.setText(value)

    def tbHumiTo_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbHumiTo.setText(value)
    
    def tbHumiFrom_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbHumiFrom.setText(value)


    def btSave_click(self):
        pass



import resources

"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setDieuKienVanHanh = QtWidgets.QWidget()
    ui = Ui_setDieuKienVanHanh()
    ui.setupUi(setDieuKienVanHanh)
    setDieuKienVanHanh.show()
    sys.exit(app.exec_())

"""