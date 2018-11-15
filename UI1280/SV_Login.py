# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_Login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SV_Login(object):
    def setupUi(self, SV_Login):
        SV_Login.setObjectName("SV_Login")
        SV_Login.resize(1280, 800)
        self.frame = QtWidgets.QFrame(SV_Login)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}#lbtitle{color:#F44336 ;font: 75  36pt bold \"Ubuntu\";}#lbThongBao{color:#F44336 ;font: 75  30pt bold \"Ubuntu\";}#lbtitle2{color:#2196F3 ;font: 75  30pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(420, 130, 471, 71))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(590, 530, 191, 101))
        self.btBack.setObjectName("btBack")
        self.tbInput = QtWidgets.QLineEdit(self.frame)
        self.tbInput.setGeometry(QtCore.QRect(450, 330, 421, 71))
        self.tbInput.setObjectName("tbInput")
        self.lbtitle2 = QtWidgets.QLabel(self.frame)
        self.lbtitle2.setGeometry(QtCore.QRect(480, 260, 381, 61))
        self.lbtitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle2.setObjectName("lbtitle2")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(180, 440, 961, 51))
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setObjectName("lbThongBao")

        self.retranslateUi(SV_Login)
        QtCore.QMetaObject.connectSlotsByName(SV_Login)

    def retranslateUi(self, SV_Login):
        _translate = QtCore.QCoreApplication.translate
        SV_Login.setWindowTitle(_translate("SV_Login", "Form"))
        self.lbtitle.setText(_translate("SV_Login", "Giao diện quản lý"))
        self.btBack.setText(_translate("SV_Login", "Quay lại"))
        self.lbtitle2.setText(_translate("SV_Login", "Nhập mật khẩu"))
        self.lbThongBao.setText(_translate("SV_Login", "nhap sai mat khau"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_Login = QtWidgets.QWidget()
    ui = Ui_SV_Login()
    ui.setupUi(SV_Login)
    SV_Login.show()
    sys.exit(app.exec_())

