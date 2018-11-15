# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keybroad.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QLineEdit,QDialog ,QGridLayout, QLabel,QPushButton,QMainWindow,QApplication,QWidget,QHBoxLayout)

class Ui_Keyboard(QDialog):
    def __init__(self):
        super(Ui_Keyboard,self).__init__()
        self.returnValue=""
        self.setObjectName("Keyboard")
        self.resize(1280, 800)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-color: #4FC3F7;}.QPushButton:pressed { background-color: #FF6E40} .QPushButton{font: 75 34pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);border-radius: 20px}.QLabel{font: 75 34pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt1 = QtWidgets.QPushButton(self.frame)
        self.bt1.setGeometry(QtCore.QRect(155, 140, 100, 100))
        self.bt1.setObjectName("bt1")
        self.bt4 = QtWidgets.QPushButton(self.frame)
        self.bt4.setGeometry(QtCore.QRect(530, 140, 100, 100))
        self.bt4.setObjectName("bt4")
        self.bt7 = QtWidgets.QPushButton(self.frame)
        self.bt7.setGeometry(QtCore.QRect(905, 140, 100, 100))
        self.bt7.setObjectName("bt7")
        self.bt2 = QtWidgets.QPushButton(self.frame)
        self.bt2.setGeometry(QtCore.QRect(280, 140, 100, 100))
        self.bt2.setObjectName("bt2")
        self.bt5 = QtWidgets.QPushButton(self.frame)
        self.bt5.setGeometry(QtCore.QRect(655, 140, 100, 100))
        self.bt5.setObjectName("bt5")
        self.bt8 = QtWidgets.QPushButton(self.frame)
        self.bt8.setGeometry(QtCore.QRect(1030, 140, 100, 100))
        self.bt8.setObjectName("bt8")
        self.bt0 = QtWidgets.QPushButton(self.frame)
        self.bt0.setGeometry(QtCore.QRect(30, 140, 100, 100))
        self.bt0.setObjectName("bt0")
        self.bt6 = QtWidgets.QPushButton(self.frame)
        self.bt6.setGeometry(QtCore.QRect(780, 140, 100, 100))
        self.bt6.setObjectName("bt6")
        self.bt3 = QtWidgets.QPushButton(self.frame)
        self.bt3.setGeometry(QtCore.QRect(405, 140, 100, 100))
        self.bt3.setObjectName("bt3")
        self.bt9 = QtWidgets.QPushButton(self.frame)
        self.bt9.setGeometry(QtCore.QRect(1155, 140, 100, 100))
        self.bt9.setObjectName("bt9")
        self.btEnter = QtWidgets.QPushButton(self.frame)
        self.btEnter.setGeometry(QtCore.QRect(710, 670, 141, 111))
        self.btEnter.setObjectName("btEnter")
        self.btClear = QtWidgets.QPushButton(self.frame)
        self.btClear.setGeometry(QtCore.QRect(490, 670, 141, 111))
        self.btClear.setObjectName("btClear")
        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(0, 0, 1281, 91))
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbValue.setObjectName("lbValue")
        self.btY = QtWidgets.QPushButton(self.frame)
        self.btY.setGeometry(QtCore.QRect(655, 270, 100, 100))
        self.btY.setObjectName("btY")
        self.btR = QtWidgets.QPushButton(self.frame)
        self.btR.setGeometry(QtCore.QRect(405, 270, 100, 100))
        self.btR.setObjectName("btR")
        self.btP = QtWidgets.QPushButton(self.frame)
        self.btP.setGeometry(QtCore.QRect(1155, 270, 100, 100))
        self.btP.setObjectName("btP")
        self.btT = QtWidgets.QPushButton(self.frame)
        self.btT.setGeometry(QtCore.QRect(530, 270, 100, 100))
        self.btT.setObjectName("btT")
        self.btI = QtWidgets.QPushButton(self.frame)
        self.btI.setGeometry(QtCore.QRect(905, 270, 100, 100))
        self.btI.setObjectName("btI")
        self.btU = QtWidgets.QPushButton(self.frame)
        self.btU.setGeometry(QtCore.QRect(780, 270, 100, 100))
        self.btU.setObjectName("btU")
        self.btO = QtWidgets.QPushButton(self.frame)
        self.btO.setGeometry(QtCore.QRect(1030, 270, 100, 100))
        self.btO.setObjectName("btO")
        self.btQ = QtWidgets.QPushButton(self.frame)
        self.btQ.setGeometry(QtCore.QRect(30, 270, 100, 100))
        self.btQ.setObjectName("btQ")
        self.btE = QtWidgets.QPushButton(self.frame)
        self.btE.setGeometry(QtCore.QRect(280, 270, 100, 100))
        self.btE.setObjectName("btE")
        self.btW = QtWidgets.QPushButton(self.frame)
        self.btW.setGeometry(QtCore.QRect(155, 270, 100, 100))
        self.btW.setObjectName("btW")
        self.btS = QtWidgets.QPushButton(self.frame)
        self.btS.setGeometry(QtCore.QRect(215, 400, 100, 100))
        self.btS.setObjectName("btS")
        self.btD = QtWidgets.QPushButton(self.frame)
        self.btD.setGeometry(QtCore.QRect(340, 400, 100, 100))
        self.btD.setObjectName("btD")
        self.btK = QtWidgets.QPushButton(self.frame)
        self.btK.setGeometry(QtCore.QRect(965, 400, 100, 100))
        self.btK.setObjectName("btK")
        self.btL = QtWidgets.QPushButton(self.frame)
        self.btL.setGeometry(QtCore.QRect(1090, 400, 100, 100))
        self.btL.setObjectName("btL")
        self.btA = QtWidgets.QPushButton(self.frame)
        self.btA.setGeometry(QtCore.QRect(90, 400, 100, 100))
        self.btA.setObjectName("btA")
        self.btF = QtWidgets.QPushButton(self.frame)
        self.btF.setGeometry(QtCore.QRect(465, 400, 100, 100))
        self.btF.setObjectName("btF")
        self.btH = QtWidgets.QPushButton(self.frame)
        self.btH.setGeometry(QtCore.QRect(715, 400, 100, 100))
        self.btH.setObjectName("btH")
        self.btJ = QtWidgets.QPushButton(self.frame)
        self.btJ.setGeometry(QtCore.QRect(840, 400, 100, 100))
        self.btJ.setObjectName("btJ")
        self.btG = QtWidgets.QPushButton(self.frame)
        self.btG.setGeometry(QtCore.QRect(590, 400, 100, 100))
        self.btG.setObjectName("btG")
        self.btX = QtWidgets.QPushButton(self.frame)
        self.btX.setGeometry(QtCore.QRect(340, 540, 100, 100))
        self.btX.setObjectName("btX")
        self.btC = QtWidgets.QPushButton(self.frame)
        self.btC.setGeometry(QtCore.QRect(465, 540, 100, 100))
        self.btC.setObjectName("btC")
        self.btZ = QtWidgets.QPushButton(self.frame)
        self.btZ.setGeometry(QtCore.QRect(215, 540, 100, 100))
        self.btZ.setObjectName("btZ")
        self.btV = QtWidgets.QPushButton(self.frame)
        self.btV.setGeometry(QtCore.QRect(590, 540, 100, 100))
        self.btV.setObjectName("btV")
        self.btN = QtWidgets.QPushButton(self.frame)
        self.btN.setGeometry(QtCore.QRect(840, 540, 100, 100))
        self.btN.setObjectName("btN")
        self.btM = QtWidgets.QPushButton(self.frame)
        self.btM.setGeometry(QtCore.QRect(965, 540, 100, 100))
        self.btM.setObjectName("btM")
        self.btB = QtWidgets.QPushButton(self.frame)
        self.btB.setGeometry(QtCore.QRect(715, 540, 100, 100))
        self.btB.setObjectName("btB")
        
        #self.showFullScreen()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Keyboard", "Keyboard"))
        self.bt1.setText(_translate("Keyboard", "1"))
        self.bt4.setText(_translate("Keyboard", "4"))
        self.bt7.setText(_translate("Keyboard", "7"))
        self.bt2.setText(_translate("Keyboard", "2"))
        self.bt5.setText(_translate("Keyboard", "5"))
        self.bt8.setText(_translate("Keyboard", "8"))
        self.bt0.setText(_translate("Keyboard", "0"))
        self.bt6.setText(_translate("Keyboard", "6"))
        self.bt3.setText(_translate("Keyboard", "3"))
        self.bt9.setText(_translate("Keyboard", "9"))
        self.btEnter.setText(_translate("Keyboard", "Enter"))
        self.btClear.setText(_translate("Keyboard", "Clear"))
        self.lbValue.setText(_translate("Keyboard", ""))
        self.btY.setText(_translate("Keyboard", "Y"))
        self.btR.setText(_translate("Keyboard", "R"))
        self.btP.setText(_translate("Keyboard", "P"))
        self.btT.setText(_translate("Keyboard", "T"))
        self.btI.setText(_translate("Keyboard", "I"))
        self.btU.setText(_translate("Keyboard", "U"))
        self.btO.setText(_translate("Keyboard", "O"))
        self.btQ.setText(_translate("Keyboard", "Q"))
        self.btE.setText(_translate("Keyboard", "E"))
        self.btW.setText(_translate("Keyboard", "W"))
        self.btS.setText(_translate("Keyboard", "S"))
        self.btD.setText(_translate("Keyboard", "D"))
        self.btK.setText(_translate("Keyboard", "K"))
        self.btL.setText(_translate("Keyboard", "L"))
        self.btA.setText(_translate("Keyboard", "A"))
        self.btF.setText(_translate("Keyboard", "F"))
        self.btH.setText(_translate("Keyboard", "H"))
        self.btJ.setText(_translate("Keyboard", "J"))
        self.btG.setText(_translate("Keyboard", "G"))
        self.btX.setText(_translate("Keyboard", "X"))
        self.btC.setText(_translate("Keyboard", "C"))
        self.btZ.setText(_translate("Keyboard", "Z"))
        self.btV.setText(_translate("Keyboard", "V"))
        self.btN.setText(_translate("Keyboard", "N"))
        self.btM.setText(_translate("Keyboard", "M"))
        self.btB.setText(_translate("Keyboard", "B"))


        self.setEvent()
    def setEvent(self):
        self.btEnter.clicked.connect(self.btEnter_click)
        self.bt0.clicked.connect(self.bt0_click)
        self.bt1.clicked.connect(self.bt1_click)
        self.bt2.clicked.connect(self.bt2_click)
        self.bt3.clicked.connect(self.bt3_click)
        self.bt4.clicked.connect(self.bt4_click)
        self.bt5.clicked.connect(self.bt5_click)
        self.bt6.clicked.connect(self.bt6_click)
        self.bt7.clicked.connect(self.bt7_click)
        self.bt8.clicked.connect(self.bt8_click)
        self.bt9.clicked.connect(self.bt9_click)
        self.btQ.clicked.connect(self.btQ_click)
        self.btW.clicked.connect(self.btW_click)
        self.btE.clicked.connect(self.btE_click)
        self.btR.clicked.connect(self.btR_click)
        self.btT.clicked.connect(self.btT_click)
        self.btY.clicked.connect(self.btY_click)
        self.btU.clicked.connect(self.btU_click)
        self.btI.clicked.connect(self.btI_click)
        self.btO.clicked.connect(self.btO_click)
        self.btP.clicked.connect(self.btP_click)
        self.btA.clicked.connect(self.btA_click)
        self.btS.clicked.connect(self.btS_click)
        self.btD.clicked.connect(self.btD_click)
        self.btF.clicked.connect(self.btF_click)
        self.btG.clicked.connect(self.btG_click)
        self.btH.clicked.connect(self.btH_click)
        self.btJ.clicked.connect(self.btJ_click)
        self.btK.clicked.connect(self.btK_click)
        self.btL.clicked.connect(self.btL_click)
        self.btZ.clicked.connect(self.btZ_click)
        self.btX.clicked.connect(self.btX_click)
        self.btC.clicked.connect(self.btC_click)
        self.btV.clicked.connect(self.btV_click)
        self.btB.clicked.connect(self.btB_click)
        self.btN.clicked.connect(self.btN_click)
        self.btM.clicked.connect(self.btM_click)
        self.btClear.clicked.connect(self.btClear_click)

    def exec_(self):
        super(Ui_Keyboard,self).exec_()
        return self.returnValue

    def numberPress(self, charIn):
        self.returnValue += charIn
        self.lbValue.setText(self.returnValue)
    def bt0_click(self):
        self.numberPress('0')
    def bt1_click(self):
        self.numberPress('1')
    def bt2_click(self):
        self.numberPress('2')
    def bt3_click(self):
        self.numberPress('3')
    def bt4_click(self):
        self.numberPress('4')
    def bt5_click(self):
        self.numberPress('5')
    def bt6_click(self):
        self.numberPress('6')
    def bt7_click(self):
        self.numberPress('7')
    def bt8_click(self):
        self.numberPress('8')
    def bt9_click(self):
        self.numberPress('9')  
    def btQ_click(self):
        self.numberPress('Q')
    def btW_click(self):
        self.numberPress('W')
    def btE_click(self):
        self.numberPress('E')
    def btR_click(self):
        self.numberPress('R')
    def btT_click(self):
        self.numberPress('T')
    def btY_click(self):
        self.numberPress('Y')
    def btU_click(self):
        self.numberPress('U')
    def btI_click(self):
        self.numberPress('I')
    def btO_click(self):
        self.numberPress('O')
    def btP_click(self):
        self.numberPress('P')  
    def btA_click(self):
        self.numberPress('A')
    def btS_click(self):
        self.numberPress('S')
    def btD_click(self):
        self.numberPress('D')
    def btF_click(self):
        self.numberPress('F')
    def btG_click(self):
        self.numberPress('G')
    def btH_click(self):
        self.numberPress('H')
    def btJ_click(self):
        self.numberPress('J')
    def btK_click(self):
        self.numberPress('K')
    def btL_click(self):
        self.numberPress('L')
    def btZ_click(self):
        self.numberPress('Z')
    def btX_click(self):
        self.numberPress('X')
    def btC_click(self):
        self.numberPress('C')
    def btV_click(self):
        self.numberPress('V')
    def btB_click(self):
        self.numberPress('B')
    def btN_click(self):
        self.numberPress('N')
    def btM_click(self):
        self.numberPress('M')
    
    def btEnter_click(self):
        self.accept()
    
    def btClear_click(self):
        self.returnValue = self.returnValue[:(len(self.returnValue)-1)]
        self.lbValue.setText(self.returnValue)

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Keyboard = Ui_Keyboard()
    Keyboard.exec_()
    sys.exit(app.exec_())

"""