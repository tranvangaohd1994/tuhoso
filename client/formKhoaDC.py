# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formKhoaDC.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  QTimer
import client

class Ui_FormKhoaDC(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        self.Form = Form
        self.frameKhoaDC = QtWidgets.QFrame(Form)
        self.frameKhoaDC.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frameKhoaDC.setStyleSheet(".QFrame{background-image: url(:/images/khoaDC.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 10px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}")
        self.frameKhoaDC.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameKhoaDC.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameKhoaDC.setObjectName("frameKhoaDC")
        self.btExit = QtWidgets.QPushButton(self.frameKhoaDC)
        self.btExit.setGeometry(QtCore.QRect(560, 560, 171, 81))
        self.btExit.setObjectName("btExit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btExit.setText(_translate("Form", "Quay lại"))

        self.setEvent()

    def setEvent(self):
        self.btExit.clicked.connect(self.btExit_click)
        self.ctimer = QTimer(self.Form)
        self.ctimer.timeout.connect(self.showTemp)
        self.ctimer.start(300)
    def showTemp(self):
        if client.isWaiting != 3 :
            self.ctimer.stop()
            self.Form.close()

    def btExit_click(self):
        client.isWaiting = 2
        client.ThClientMain.sent2Server(b'\xef\xed')
        self.ctimer.stop()
        self.Form.close()
import resources

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

'''