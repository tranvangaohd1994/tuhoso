# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_ChonTuCaiDat.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SV_ChonDMTu(object):
    def setupUi(self, SV_ChonDMTu):
        SV_ChonDMTu.setObjectName("SV_ChonDMTu")
        SV_ChonDMTu.resize(1280, 800)
        self.frame = QtWidgets.QFrame(SV_ChonDMTu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}.QLabel{color:#F44336 ;font: 75  34pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 26pt bold \"Ubuntu\";}#btBack{color:white;border-image: url(:/images/back.png);}QCheckBox{font: 75 Bold 30pt \"Ubuntu\";color: white;background-color: #55007f;}.QCheckBox::indicator{width: 30px;height: 30px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(450, 140, 431, 81))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(150, 620, 211, 111))
        self.btBack.setObjectName("btBack")
        self.btChon = QtWidgets.QPushButton(self.frame)
        self.btChon.setGeometry(QtCore.QRect(570, 620, 211, 111))
        self.btChon.setObjectName("btChon")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(210, 260, 901, 261))
        self.grcdControl.setStyleSheet(".QRadioButton{font: 75 Bold 26pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbTu2 = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTu2.setGeometry(QtCore.QRect(570, 70, 171, 100))
        self.rbTu2.setObjectName("rbTu2")
        self.rbTu1 = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTu1.setGeometry(QtCore.QRect(190, 70, 161, 100))
        self.rbTu1.setChecked(True)
        self.rbTu1.setObjectName("rbTu1")
        self.btChon_2 = QtWidgets.QPushButton(self.frame)
        self.btChon_2.setGeometry(QtCore.QRect(940, 620, 211, 111))
        self.btChon_2.setObjectName("btChon_2")

        self.retranslateUi(SV_ChonDMTu)
        QtCore.QMetaObject.connectSlotsByName(SV_ChonDMTu)

    def retranslateUi(self, SV_ChonDMTu):
        _translate = QtCore.QCoreApplication.translate
        SV_ChonDMTu.setWindowTitle(_translate("SV_ChonDMTu", "Form"))
        self.lbtitle.setText(_translate("SV_ChonDMTu", "Chọn tủ cài đặt"))
        self.btBack.setText(_translate("SV_ChonDMTu", "Quay lại"))
        self.btChon.setText(_translate("SV_ChonDMTu", "Cài Đặt"))
        self.rbTu2.setText(_translate("SV_ChonDMTu", "Tủ phải"))
        self.rbTu1.setText(_translate("SV_ChonDMTu", "Tủ trái"))
        self.btChon_2.setText(_translate("SV_ChonDMTu", "Tiếp"))

import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_ChonDMTu = QtWidgets.QWidget()
    ui = Ui_SV_ChonDMTu()
    ui.setupUi(SV_ChonDMTu)
    SV_ChonDMTu.show()
    sys.exit(app.exec_())

