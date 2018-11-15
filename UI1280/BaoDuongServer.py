# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaoDuongServer.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BaoDuongServer(object):
    def setupUi(self, BaoDuongServer):
        BaoDuongServer.setObjectName("BaoDuongServer")
        BaoDuongServer.resize(1280, 800)
        self.frame = QtWidgets.QFrame(BaoDuongServer)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#lbtitle{color:red ;font: 75  30pt bold \"Ubuntu\";}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #c9ffbc;font: 75 20pt bold \"Ubuntu\";}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(320, 130, 661, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btTiepTuc = QtWidgets.QPushButton(self.frame)
        self.btTiepTuc.setGeometry(QtCore.QRect(930, 610, 161, 111))
        self.btTiepTuc.setObjectName("btTiepTuc")
        self.grRight = QtWidgets.QGroupBox(self.frame)
        self.grRight.setGeometry(QtCore.QRect(450, 210, 391, 391))
        self.grRight.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Ubuntu\";}")
        self.grRight.setTitle("")
        self.grRight.setObjectName("grRight")
        self.lbCoichip = QtWidgets.QLabel(self.grRight)
        self.lbCoichip.setGeometry(QtCore.QRect(10, 110, 371, 41))
        self.lbCoichip.setObjectName("lbCoichip")
        self.lbCBChayTrong = QtWidgets.QLabel(self.grRight)
        self.lbCBChayTrong.setGeometry(QtCore.QRect(10, 260, 331, 41))
        self.lbCBChayTrong.setObjectName("lbCBChayTrong")
        self.lbCBChayNgoai = QtWidgets.QLabel(self.grRight)
        self.lbCBChayNgoai.setGeometry(QtCore.QRect(10, 320, 331, 41))
        self.lbCBChayNgoai.setObjectName("lbCBChayNgoai")
        self.lbQuatGio = QtWidgets.QLabel(self.grRight)
        self.lbQuatGio.setGeometry(QtCore.QRect(10, 160, 371, 41))
        self.lbQuatGio.setObjectName("lbQuatGio")
        self.lbDenThap = QtWidgets.QLabel(self.grRight)
        self.lbDenThap.setGeometry(QtCore.QRect(10, 210, 371, 41))
        self.lbDenThap.setObjectName("lbDenThap")
        self.lbTempIn = QtWidgets.QLabel(self.grRight)
        self.lbTempIn.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.lbTempIn.setObjectName("lbTempIn")
        self.lbTempOut = QtWidgets.QLabel(self.grRight)
        self.lbTempOut.setGeometry(QtCore.QRect(10, 60, 341, 41))
        self.lbTempOut.setObjectName("lbTempOut")
        self.btThoat = QtWidgets.QPushButton(self.frame)
        self.btThoat.setGeometry(QtCore.QRect(200, 600, 161, 111))
        self.btThoat.setObjectName("btThoat")
        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(490, 640, 330, 50))
        self.lbValue.setObjectName("lbValue")

        self.retranslateUi(BaoDuongServer)
        QtCore.QMetaObject.connectSlotsByName(BaoDuongServer)

    def retranslateUi(self, BaoDuongServer):
        _translate = QtCore.QCoreApplication.translate
        BaoDuongServer.setWindowTitle(_translate("BaoDuongServer", "Form"))
        self.lbtitle.setText(_translate("BaoDuongServer", "Thông tin bảo dưỡng"))
        self.btTiepTuc.setText(_translate("BaoDuongServer", "Tiếp tục"))
        self.lbCoichip.setText(_translate("BaoDuongServer", "Còi chip"))
        self.lbCBChayTrong.setText(_translate("BaoDuongServer", "Cảm biến cháy trong"))
        self.lbCBChayNgoai.setText(_translate("BaoDuongServer", "Cảm biến cháy ngoài"))
        self.lbQuatGio.setText(_translate("BaoDuongServer", "Quạt thông gió"))
        self.lbDenThap.setText(_translate("BaoDuongServer", "Đèn tháp 3 màu"))
        self.lbTempIn.setText(_translate("BaoDuongServer", "Cảm biến nhiệt độ trong"))
        self.lbTempOut.setText(_translate("BaoDuongServer", "Cảm biến nhiệt độ ngoài"))
        self.btThoat.setText(_translate("BaoDuongServer", "Thoát"))
        self.lbValue.setText(_translate("BaoDuongServer", "Waiting"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaoDuongServer = QtWidgets.QWidget()
    ui = Ui_BaoDuongServer()
    ui.setupUi(BaoDuongServer)
    BaoDuongServer.show()
    sys.exit(app.exec_())

