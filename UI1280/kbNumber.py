# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kbNumber.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(780, 480)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 780, 480))
        self.frame.setStyleSheet(".QFrame{background-color: #4FC3F7;}.QPushButton:pressed { background-color: #FF6E40} .QPushButton{font: 75 32pt bold \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);border-radius: 20px}.QLabel{font: 75 30pt bold \"Ubuntu\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt1 = QtWidgets.QPushButton(self.frame)
        self.bt1.setGeometry(QtCore.QRect(40, 40, 121, 81))
        self.bt1.setObjectName("bt1")
        self.bt4 = QtWidgets.QPushButton(self.frame)
        self.bt4.setGeometry(QtCore.QRect(40, 150, 121, 81))
        self.bt4.setObjectName("bt4")
        self.bt7 = QtWidgets.QPushButton(self.frame)
        self.bt7.setGeometry(QtCore.QRect(40, 260, 121, 81))
        self.bt7.setObjectName("bt7")
        self.bt2 = QtWidgets.QPushButton(self.frame)
        self.bt2.setGeometry(QtCore.QRect(220, 40, 121, 81))
        self.bt2.setObjectName("bt2")
        self.bt5 = QtWidgets.QPushButton(self.frame)
        self.bt5.setGeometry(QtCore.QRect(220, 150, 121, 81))
        self.bt5.setObjectName("bt5")
        self.bt8 = QtWidgets.QPushButton(self.frame)
        self.bt8.setGeometry(QtCore.QRect(220, 260, 121, 81))
        self.bt8.setObjectName("bt8")
        self.bt0 = QtWidgets.QPushButton(self.frame)
        self.bt0.setGeometry(QtCore.QRect(220, 370, 121, 81))
        self.bt0.setObjectName("bt0")
        self.bt6 = QtWidgets.QPushButton(self.frame)
        self.bt6.setGeometry(QtCore.QRect(400, 150, 121, 81))
        self.bt6.setObjectName("bt6")
        self.bt3 = QtWidgets.QPushButton(self.frame)
        self.bt3.setGeometry(QtCore.QRect(400, 40, 121, 81))
        self.bt3.setObjectName("bt3")
        self.bt9 = QtWidgets.QPushButton(self.frame)
        self.bt9.setGeometry(QtCore.QRect(400, 260, 121, 81))
        self.bt9.setObjectName("bt9")
        self.btEnter = QtWidgets.QPushButton(self.frame)
        self.btEnter.setGeometry(QtCore.QRect(400, 370, 121, 81))
        self.btEnter.setObjectName("btEnter")
        self.btClear = QtWidgets.QPushButton(self.frame)
        self.btClear.setGeometry(QtCore.QRect(40, 370, 121, 81))
        self.btClear.setObjectName("btClear")
        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(560, 60, 181, 81))
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbValue.setObjectName("lbValue")
        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(540, 170, 221, 241))
        self.grcdControl.setStyleSheet(".QRadioButton{font: 75 Bold 26pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbTuPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuPhai.setGeometry(QtCore.QRect(20, 130, 181, 100))
        self.rbTuPhai.setObjectName("rbTuPhai")
        self.rbTuTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuTrai.setGeometry(QtCore.QRect(20, 10, 181, 100))
        self.rbTuTrai.setChecked(True)
        self.rbTuTrai.setObjectName("rbTuTrai")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bt1.setText(_translate("Dialog", "1"))
        self.bt4.setText(_translate("Dialog", "4"))
        self.bt7.setText(_translate("Dialog", "7"))
        self.bt2.setText(_translate("Dialog", "2"))
        self.bt5.setText(_translate("Dialog", "5"))
        self.bt8.setText(_translate("Dialog", "8"))
        self.bt0.setText(_translate("Dialog", "0"))
        self.bt6.setText(_translate("Dialog", "6"))
        self.bt3.setText(_translate("Dialog", "3"))
        self.bt9.setText(_translate("Dialog", "9"))
        self.btEnter.setText(_translate("Dialog", "Enter"))
        self.btClear.setText(_translate("Dialog", "Clear"))
        self.lbValue.setText(_translate("Dialog", "123"))
        self.rbTuPhai.setText(_translate("Dialog", "Tủ phải"))
        self.rbTuTrai.setText(_translate("Dialog", "Tủ trái"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

