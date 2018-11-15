# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setPassword.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setPassword(object):
    def setupUi(self, setPassword):
        setPassword.setObjectName("setPassword")
        setPassword.resize(1280, 800)
        setPassword.setStyleSheet("")
        self.setPassword = setPassword
        self.frame = QtWidgets.QFrame(setPassword)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF3D00;font: 75 24pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 26pt \"Ubuntu\";color:#0091EA}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1301, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 250, 211, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 570, 361, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 400, 221, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(780, 630, 191, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1060, 630, 191, 101))
        self.btExit.setObjectName("btExit")
        self.tbMkCu = QtWidgets.QLineEdit(self.frame)
        self.tbMkCu.setGeometry(QtCore.QRect(60, 300, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbMkCu.setFont(font)
        self.tbMkCu.setText("")
        self.tbMkCu.setObjectName("tbMkCu")
        self.tbMkMoiVerify = QtWidgets.QLineEdit(self.frame)
        self.tbMkMoiVerify.setGeometry(QtCore.QRect(60, 630, 361, 51))

        self.tbMkMoiVerify.setFont(font)
        self.tbMkMoiVerify.setText("")
        self.tbMkMoiVerify.setObjectName("tbMkMoiVerify")
        self.tbMkMoi = QtWidgets.QLineEdit(self.frame)
        self.tbMkMoi.setGeometry(QtCore.QRect(60, 460, 361, 61))
       
        self.tbMkMoi.setFont(font)
        self.tbMkMoi.setText("")
        self.tbMkMoi.setObjectName("tbMkMoi")
        self.btThemVanTay = QtWidgets.QPushButton(self.frame)
        self.btThemVanTay.setGeometry(QtCore.QRect(780, 460, 191, 101))
        self.btThemVanTay.setObjectName("btThemVanTay")
        self.btXoaVanTay = QtWidgets.QPushButton(self.frame)
        self.btXoaVanTay.setGeometry(QtCore.QRect(1060, 460, 191, 101))
        self.btXoaVanTay.setObjectName("btXoaVanTay")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(760, 180, 501, 231))
        self.lbThongBao.setStyleSheet("")
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setWordWrap(True)
        self.lbThongBao.setObjectName("lbThongBao")

        self.retranslateUi(setPassword)
        QtCore.QMetaObject.connectSlotsByName(setPassword)

    def retranslateUi(self, setPassword):
        _translate = QtCore.QCoreApplication.translate
        setPassword.setWindowTitle(_translate("setPassword", "Form"))
        self.label.setText(_translate("setPassword", "Cài đặt mật khẩu"))
        self.label_2.setText(_translate("setPassword", "Mật khẩu cũ"))
        self.label_3.setText(_translate("setPassword", "Nhập lại mật khẩu mới"))
        self.label_4.setText(_translate("setPassword", "Mật khẩu mới"))
        self.btSave.setText(_translate("setPassword", "Lưu"))
        self.btExit.setText(_translate("setPassword", "Thoát"))
        self.btThemVanTay.setText(_translate("setPassword", "Thêm vân tay"))
        self.btXoaVanTay.setText(_translate("setPassword", "Xóa vân tay"))
        self.lbThongBao.setText(_translate("setPassword", "Đang quét vân tay! Vui lòng đặt tay vào cảm biến vân tay."))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setPassword = QtWidgets.QWidget()
    ui = Ui_setPassword()
    ui.setupUi(setPassword)
    setPassword.show()
    sys.exit(app.exec_())

