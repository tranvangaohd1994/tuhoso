# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logTemp.ui'
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
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(50, 680, 191, 101))
        self.btBack.setObjectName("btBack")
        self.btTemHumi = QtWidgets.QPushButton(self.frame)
        self.btTemHumi.setGeometry(QtCore.QRect(50, 560, 191, 101))
        self.btTemHumi.setObjectName("btTemHumi")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 310, 111, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 490, 141, 50))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tbYear = QtWidgets.QLineEdit(self.frame)
        self.tbYear.setGeometry(QtCore.QRect(140, 480, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbYear.setFont(font)
        self.tbYear.setObjectName("tbYear")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 400, 131, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tbDay = QtWidgets.QLineEdit(self.frame)
        self.tbDay.setGeometry(QtCore.QRect(140, 310, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbDay.setFont(font)
        self.tbDay.setObjectName("tbDay")
        self.tbMonth = QtWidgets.QLineEdit(self.frame)
        self.tbMonth.setGeometry(QtCore.QRect(140, 390, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbMonth.setFont(font)
        self.tbMonth.setObjectName("tbMonth")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 240, 111, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tbNumTu = QtWidgets.QLineEdit(self.frame)
        self.tbNumTu.setGeometry(QtCore.QRect(140, 230, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbNumTu.setFont(font)
        self.tbNumTu.setObjectName("tbNumTu")
        self.grcdControl_2 = QtWidgets.QGroupBox(self.frame)
        self.grcdControl_2.setGeometry(QtCore.QRect(0, 110, 281, 131))
        self.grcdControl_2.setStyleSheet(".QRadioButton{font: 75 Bold 26pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}\n"
"")
        self.grcdControl_2.setTitle("")
        self.grcdControl_2.setObjectName("grcdControl_2")
        self.rbTu2_2 = QtWidgets.QRadioButton(self.grcdControl_2)
        self.rbTu2_2.setGeometry(QtCore.QRect(140, 39, 111, 71))
        self.rbTu2_2.setObjectName("rbTu2_2")
        self.rbTu1_2 = QtWidgets.QRadioButton(self.grcdControl_2)
        self.rbTu1_2.setGeometry(QtCore.QRect(10, 39, 111, 71))
        self.rbTu1_2.setChecked(True)
        self.rbTu1_2.setObjectName("rbTu1_2")

        self.retranslateUi(SV_Login)
        QtCore.QMetaObject.connectSlotsByName(SV_Login)

    def retranslateUi(self, SV_Login):
        _translate = QtCore.QCoreApplication.translate
        SV_Login.setWindowTitle(_translate("SV_Login", "Form"))
        self.btBack.setText(_translate("SV_Login", "Quay lại"))
        self.btTemHumi.setText(_translate("SV_Login", "Nhiệt độ"))
        self.label_7.setText(_translate("SV_Login", "Ngày"))
        self.label_5.setText(_translate("SV_Login", "Năm"))
        self.tbYear.setText(_translate("SV_Login", "2018"))
        self.label_3.setText(_translate("SV_Login", "Tháng"))
        self.tbDay.setText(_translate("SV_Login", "10"))
        self.tbMonth.setText(_translate("SV_Login", "10"))
        self.label_8.setText(_translate("SV_Login", "Tủ"))
        self.tbNumTu.setText(_translate("SV_Login", "1"))
        self.rbTu2_2.setText(_translate("SV_Login", "Phải"))
        self.rbTu1_2.setText(_translate("SV_Login", "Trái"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_Login = QtWidgets.QWidget()
    ui = Ui_SV_Login()
    ui.setupUi(SV_Login)
    SV_Login.show()
    sys.exit(app.exec_())

