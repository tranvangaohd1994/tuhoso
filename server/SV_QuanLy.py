# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_GDQuanLy.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from keyboard import Ui_Keyboard
from svCaiDatPhuTro import Ui_SVCaiDatPhuTro
from SV_CaiDatNangCao import Ui_SVCaiDatNangCao
import uart

class Ui_SVQuanLy(object):
    def setupUi(self, SVQuanLy):
        SVQuanLy.setObjectName("SVQuanLy")
        SVQuanLy.resize(1280, 800)
        self.SVQuanLy = SVQuanLy

        self.frame = QtWidgets.QFrame(SVQuanLy)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}.QLabel{color:#F44336 ;font: 75  30pt \"Arial\";}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}#btBack{color:white;border-image: url(:/images/back.png);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(470, 180, 381, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(580, 650, 211, 111))
        self.btBack.setObjectName("btBack")
        self.btCaiDatPhuTro = QtWidgets.QPushButton(self.frame)
        self.btCaiDatPhuTro.setGeometry(QtCore.QRect(390, 340, 191, 151))
        self.btCaiDatPhuTro.setObjectName("btCaiDatPhuTro")
        self.btCaiDatNangCao = QtWidgets.QPushButton(self.frame)
        self.btCaiDatNangCao.setGeometry(QtCore.QRect(740, 340, 191, 151))
        self.btCaiDatNangCao.setObjectName("btCaiDatNangCao")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(340, 540, 681, 71))
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setObjectName("lbThongBao")

        self.retranslateUi(SVQuanLy)
        QtCore.QMetaObject.connectSlotsByName(SVQuanLy)

       
    def retranslateUi(self, SVQuanLy):
        _translate = QtCore.QCoreApplication.translate
        SVQuanLy.setWindowTitle(_translate("SVQuanLy", "Form"))
        self.lbtitle.setText(_translate("SVQuanLy", "Giao diện quản lý"))
        self.btBack.setText(_translate("SVQuanLy", "Quay lại"))
        self.btCaiDatPhuTro.setText(_translate("SVQuanLy", "Cài đặt\n"
            " Phụ trợ"))
        self.btCaiDatNangCao.setText(_translate("SVQuanLy", "Cài đặt\n"
            " Nâng cao"))
        self.setEvent()

    
    def setEvent(self):
        self.btCaiDatNangCao.clicked.connect(self.btCaiDatNangCao_click)
        self.btCaiDatPhuTro.clicked.connect(self.btCaiDatPhuTro_click)
        self.btBack.clicked.connect(self.SVQuanLy.close)
        
    def btCaiDatNangCao_click(self):
        dialogKey= Ui_Keyboard()
        value = dialogKey.exec_()
        if value != uart.dtMK and value != uart.dtMKHard:
            self.lbThongBao.setText("Nhập sai mật khẩu")
        else :
            self.lbThongBao.setText("")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_SVCaiDatNangCao()
            self.ui.setupUi(self.window)
            self.window.show()
            self.window.showFullScreen()
            self.SVQuanLy.close()
            
        
    def btCaiDatPhuTro_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SVCaiDatPhuTro()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.showFullScreen()
        self.SVQuanLy.close()
       

    

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVQuanLy = QtWidgets.QWidget()
    ui = Ui_SVQuanLy()
    ui.setupUi(SVQuanLy)
    SVQuanLy.show()
    sys.exit(app.exec_())

"""