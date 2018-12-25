# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_ChonClient.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import server
from mainDisplay import Ui_SV_mainDisplay
import time


class Ui_dtLanDau(object):
    def setupUi(self, dtLanDau):
        dtLanDau.setObjectName("dtLanDau")
        dtLanDau.resize(1280, 800)
        self.dtLanDau = dtLanDau
        self.frame = QtWidgets.QFrame(dtLanDau)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/dmLanDau.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #4e9400;font: 25pt \\\"Arial\\\";color:#ffffff}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btDongTu = QtWidgets.QPushButton(self.frame)
        self.btDongTu.setGeometry(QtCore.QRect(560, 390, 181, 91))
        self.btDongTu.setObjectName("btDongTu")

        self.retranslateUi(dtLanDau)
        QtCore.QMetaObject.connectSlotsByName(dtLanDau)

    def retranslateUi(self, dtLanDau):
        _translate = QtCore.QCoreApplication.translate
        dtLanDau.setWindowTitle(_translate("dtLanDau", "Form"))
        self.btDongTu.setText(_translate("dtLanDau", "Đóng tủ"))
        
        self.setEvent()
    
    def setEvent(self):
        self.btDongTu.clicked.connect(self.btNext_click)

    def btNext_click(self):
        #cho luong thuc hien cong viec dong tu lan dau
        self.ui = Ui_SV_mainDisplay()
        self.ui.setupUi()
        self.ui.show()
        if server.isFullSceen:
            self.ui.showFullScreen()
        #dong form này lại---dong tu lan dau dong ca 2 ban 
        server.tuTraiPhai = 'A' # dong ca 2 ben tu
        server.dongMoTuFunction(0,0)
        self.dtLanDau.close()
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVChonClient = QtWidgets.QWidget()
    ui = Ui_dtLanDau()
    ui.setupUi(SVChonClient)
    SVChonClient.show()
    sys.exit(app.exec_())
"""