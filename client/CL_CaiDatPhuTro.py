# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CL_CaiDatPhuTro.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import client

class Ui_CL_CaiDatPhuTro(object):
    def setupUi(self, CL_CaiDatPhuTro):
        CL_CaiDatPhuTro.setObjectName("CL_CaiDatPhuTro")
        CL_CaiDatPhuTro.resize(1280, 800)
        self.frame = QtWidgets.QFrame(CL_CaiDatPhuTro)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}#lbtitle{color:red ;font: 75  30pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}#btBack{color:white;border-image: url(:/images/back.png);}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(480, 130, 381, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBatDen = QtWidgets.QPushButton(self.frame)
        self.btBatDen.setGeometry(QtCore.QRect(310, 290, 191, 101))
        self.btBatDen.setObjectName("btBatDen")
        self.btTatDen = QtWidgets.QPushButton(self.frame)
        self.btTatDen.setGeometry(QtCore.QRect(830, 290, 191, 101))
        self.btTatDen.setObjectName("btTatDen")
        self.btCheDoBaoDuong = QtWidgets.QPushButton(self.frame)
        self.btCheDoBaoDuong.setGeometry(QtCore.QRect(310, 480, 191, 101))
        self.btCheDoBaoDuong.setObjectName("btCheDoBaoDuong")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(830, 480, 191, 101))
        self.btBack.setObjectName("btBack")

        self.retranslateUi(CL_CaiDatPhuTro)
        QtCore.QMetaObject.connectSlotsByName(CL_CaiDatPhuTro)

    def retranslateUi(self, CL_CaiDatPhuTro):
        _translate = QtCore.QCoreApplication.translate
        CL_CaiDatPhuTro.setWindowTitle(_translate("CL_CaiDatPhuTro", "Form"))
        self.lbtitle.setText(_translate("CL_CaiDatPhuTro", "Cài đặt phụ trợ"))
        self.btBatDen.setText(_translate("CL_CaiDatPhuTro", "Bật đèn"))
        self.btTatDen.setText(_translate("CL_CaiDatPhuTro", "Tắt đèn"))
        self.btCheDoBaoDuong.setText(_translate("CL_CaiDatPhuTro", "Bảo dưỡng"))
        self.btBack.setText(_translate("CL_CaiDatPhuTro", "Quay lại"))
        
        self.setEvent()
        self.btBack.clicked.connect(CL_CaiDatPhuTro.close)

    def setEvent(self):
        self.btBatDen.clicked.connect(self.btBatDen_clicked)
        self.btTatDen.clicked.connect(self.btTatDen_clicked)

    def btBatDen_clicked(self):
        for i in range(0,8):
            client.DataCamBien[i] = 0x00

        client.DataCamBien[0]=0x31
        client.sentCambien()
        pass
    def btTatDen_clicked(self):
        for i in range(0,8):
            client.DataCamBien[i] = 0x00
            
        client.DataCamBien[0]=0x30
        client.sentCambien()
        pass
        


import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CL_CaiDatPhuTro = QtWidgets.QWidget()
    ui = Ui_CL_CaiDatPhuTro()
    ui.setupUi(CL_CaiDatPhuTro)
    CL_CaiDatPhuTro.show()
    sys.exit(app.exec_())

"""