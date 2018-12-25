# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keybroad.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QLineEdit,QDialog ,QGridLayout, QLabel,QPushButton,QMainWindow,QApplication,QWidget,QHBoxLayout)
import resources

class Ui_KeyboardVN(QDialog):
    def __init__(self):
        super(Ui_KeyboardVN,self).__init__()
        self.returnValue=""
        self.setObjectName("Keyboard")
        self.resize(1280, 800)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/background.png);}.QPushButton:pressed { background-color: #FF6E40} .QPushButton{font: 30pt \"Arial\";background-color: #4e9400;color: #ffffff;border-radius: 20px}.QLabel{font:  30pt \"Arial\";background-color: #ffffff;color: #000000;border: 2px solid gray;border-radius: 10px;padding: 0 8px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt1 = QtWidgets.QPushButton(self.frame)
        self.bt1.setGeometry(QtCore.QRect(155, 340, 100, 75))
        self.bt1.setObjectName("bt1")
        self.bt4 = QtWidgets.QPushButton(self.frame)
        self.bt4.setGeometry(QtCore.QRect(530, 340, 100, 75))
        self.bt4.setObjectName("bt4")
        self.bt7 = QtWidgets.QPushButton(self.frame)
        self.bt7.setGeometry(QtCore.QRect(905, 340, 100, 75))
        self.bt7.setObjectName("bt7")
        self.bt2 = QtWidgets.QPushButton(self.frame)
        self.bt2.setGeometry(QtCore.QRect(280, 340, 100, 75))
        self.bt2.setObjectName("bt2")
        self.bt5 = QtWidgets.QPushButton(self.frame)
        self.bt5.setGeometry(QtCore.QRect(655, 340, 100, 75))
        self.bt5.setObjectName("bt5")
        self.bt8 = QtWidgets.QPushButton(self.frame)
        self.bt8.setGeometry(QtCore.QRect(1030, 340, 100, 75))
        self.bt8.setObjectName("bt8")
        self.bt0 = QtWidgets.QPushButton(self.frame)
        self.bt0.setGeometry(QtCore.QRect(30, 340, 100, 75))
        self.bt0.setObjectName("bt0")
        self.bt6 = QtWidgets.QPushButton(self.frame)
        self.bt6.setGeometry(QtCore.QRect(780, 340, 100, 75))
        self.bt6.setObjectName("bt6")
        self.bt3 = QtWidgets.QPushButton(self.frame)
        self.bt3.setGeometry(QtCore.QRect(405, 340, 100, 75))
        self.bt3.setObjectName("bt3")
        self.bt9 = QtWidgets.QPushButton(self.frame)
        self.bt9.setGeometry(QtCore.QRect(1155, 340, 100, 75))
        self.bt9.setObjectName("bt9")
        self.btEnter = QtWidgets.QPushButton(self.frame)
        self.btEnter.setGeometry(QtCore.QRect(1060, 710, 141, 75))
        self.btEnter.setObjectName("btEnter")
        self.btClear = QtWidgets.QPushButton(self.frame)
        self.btClear.setGeometry(QtCore.QRect(70, 710, 141, 75))
        self.btClear.setObjectName("btClear")
        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(330, 160, 611, 61))
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbValue.setObjectName("lbValue")
        self.btY = QtWidgets.QPushButton(self.frame)
        self.btY.setGeometry(QtCore.QRect(655, 430, 100, 75))
        self.btY.setObjectName("btY")
        self.btR = QtWidgets.QPushButton(self.frame)
        self.btR.setGeometry(QtCore.QRect(405, 430, 100, 75))
        self.btR.setObjectName("btR")
        self.btP = QtWidgets.QPushButton(self.frame)
        self.btP.setGeometry(QtCore.QRect(1155, 430, 100, 75))
        self.btP.setObjectName("btP")
        self.btT = QtWidgets.QPushButton(self.frame)
        self.btT.setGeometry(QtCore.QRect(530, 430, 100, 75))
        self.btT.setObjectName("btT")
        self.btI = QtWidgets.QPushButton(self.frame)
        self.btI.setGeometry(QtCore.QRect(905, 430, 100, 75))
        self.btI.setObjectName("btI")
        self.btU = QtWidgets.QPushButton(self.frame)
        self.btU.setGeometry(QtCore.QRect(780, 430, 100, 75))
        self.btU.setObjectName("btU")
        self.btO = QtWidgets.QPushButton(self.frame)
        self.btO.setGeometry(QtCore.QRect(1030, 430, 100, 75))
        self.btO.setObjectName("btO")
        self.btQ = QtWidgets.QPushButton(self.frame)
        self.btQ.setGeometry(QtCore.QRect(30, 430, 100, 75))
        self.btQ.setObjectName("btQ")
        self.btE = QtWidgets.QPushButton(self.frame)
        self.btE.setGeometry(QtCore.QRect(280, 430, 100, 75))
        self.btE.setObjectName("btE")
        self.btW = QtWidgets.QPushButton(self.frame)
        self.btW.setGeometry(QtCore.QRect(155, 430, 100, 75))
        self.btW.setObjectName("btW")
        self.btS = QtWidgets.QPushButton(self.frame)
        self.btS.setGeometry(QtCore.QRect(215, 520, 100, 75))
        self.btS.setObjectName("btS")
        self.btD = QtWidgets.QPushButton(self.frame)
        self.btD.setGeometry(QtCore.QRect(340, 520, 100, 75))
        self.btD.setObjectName("btD")
        self.btK = QtWidgets.QPushButton(self.frame)
        self.btK.setGeometry(QtCore.QRect(965, 520, 100, 75))
        self.btK.setObjectName("btK")
        self.btL = QtWidgets.QPushButton(self.frame)
        self.btL.setGeometry(QtCore.QRect(1090, 520, 100, 75))
        self.btL.setObjectName("btL")
        self.btA = QtWidgets.QPushButton(self.frame)
        self.btA.setGeometry(QtCore.QRect(90, 520, 100, 75))
        self.btA.setObjectName("btA")
        self.btF = QtWidgets.QPushButton(self.frame)
        self.btF.setGeometry(QtCore.QRect(465, 520, 100, 75))
        self.btF.setObjectName("btF")
        self.btH = QtWidgets.QPushButton(self.frame)
        self.btH.setGeometry(QtCore.QRect(715, 520, 100, 75))
        self.btH.setObjectName("btH")
        self.btJ = QtWidgets.QPushButton(self.frame)
        self.btJ.setGeometry(QtCore.QRect(840, 520, 100, 75))
        self.btJ.setObjectName("btJ")
        self.btG = QtWidgets.QPushButton(self.frame)
        self.btG.setGeometry(QtCore.QRect(590, 520, 100, 75))
        self.btG.setObjectName("btG")
        self.btX = QtWidgets.QPushButton(self.frame)
        self.btX.setGeometry(QtCore.QRect(340, 610, 100, 75))
        self.btX.setObjectName("btX")
        self.btC = QtWidgets.QPushButton(self.frame)
        self.btC.setGeometry(QtCore.QRect(465, 610, 100, 75))
        self.btC.setObjectName("btC")
        self.btZ = QtWidgets.QPushButton(self.frame)
        self.btZ.setGeometry(QtCore.QRect(215, 610, 100, 75))
        self.btZ.setObjectName("btZ")
        self.btV = QtWidgets.QPushButton(self.frame)
        self.btV.setGeometry(QtCore.QRect(590, 610, 100, 75))
        self.btV.setObjectName("btV")
        self.btN = QtWidgets.QPushButton(self.frame)
        self.btN.setGeometry(QtCore.QRect(840, 610, 100, 75))
        self.btN.setObjectName("btN")
        self.btM = QtWidgets.QPushButton(self.frame)
        self.btM.setGeometry(QtCore.QRect(965, 610, 100, 75))
        self.btM.setObjectName("btM")
        self.btB = QtWidgets.QPushButton(self.frame)
        self.btB.setGeometry(QtCore.QRect(715, 610, 100, 75))
        self.btB.setObjectName("btB")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 240, 1271, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btH1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH1.setObjectName("btH1")
        self.horizontalLayout.addWidget(self.btH1)
        self.btH2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH2.setObjectName("btH2")
        self.horizontalLayout.addWidget(self.btH2)
        self.btH3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH3.setObjectName("btH3")
        self.horizontalLayout.addWidget(self.btH3)
        self.btH4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH4.setObjectName("btH4")
        self.horizontalLayout.addWidget(self.btH4)
        self.btH5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH5.setObjectName("btH5")
        self.horizontalLayout.addWidget(self.btH5)
        self.btH6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH6.setObjectName("btH6")
        self.horizontalLayout.addWidget(self.btH6)
        self.btH7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH7.setObjectName("btH7")
        self.horizontalLayout.addWidget(self.btH7)
        self.btH8 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH8.setObjectName("btH8")
        self.horizontalLayout.addWidget(self.btH8)
        self.btH9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH9.setObjectName("btH9")
        self.horizontalLayout.addWidget(self.btH9)
        self.btH10 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH10.setObjectName("btH10")
        self.horizontalLayout.addWidget(self.btH10)
        self.btH11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH11.setObjectName("btH11")
        self.horizontalLayout.addWidget(self.btH11)
        self.btH12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH12.setObjectName("btH12")
        self.horizontalLayout.addWidget(self.btH12)
        self.btH13 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH13.setObjectName("btH13")
        self.horizontalLayout.addWidget(self.btH13)
        self.btH14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH14.setObjectName("btH14")
        self.horizontalLayout.addWidget(self.btH14)
        self.btH15 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH15.setObjectName("btH15")
        self.horizontalLayout.addWidget(self.btH15)
        self.btH16 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btH16.setFont(font)
        self.btH16.setAutoRepeat(False)
        self.btH16.setObjectName("btH16")
        self.horizontalLayout.addWidget(self.btH16)
        self.btH17 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH17.setObjectName("btH17")
        self.horizontalLayout.addWidget(self.btH17)
        self.btH18 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btH18.setObjectName("btH18")
        self.horizontalLayout.addWidget(self.btH18)
        self.btSpace = QtWidgets.QPushButton(self.frame)
        self.btSpace.setGeometry(QtCore.QRect(290, 710, 411, 75))
        self.btSpace.setObjectName("btSpace")
        self.btTab = QtWidgets.QPushButton(self.frame)
        self.btTab.setGeometry(QtCore.QRect(730, 710, 281, 75))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
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
        self.lbValue.setText(_translate("Keyboard", "123"))
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
        
        self.btSpace.setText(_translate("Keyboard", "Space"))
        self.btTab.setText(_translate("Keyboard", "Tab"))


        self.setEvent()
    
    def setEvent(self):
        #set event for button click
        if True :
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
            self.btTab.clicked.connect(self.btTab_click)
            self.btSpace.clicked.connect(self.btSpace_click)

            self.btH1.clicked.connect(self.btH1_click)
            self.btH2.clicked.connect(self.btH2_click)
            self.btH3.clicked.connect(self.btH3_click)
            self.btH4.clicked.connect(self.btH4_click)
            self.btH5.clicked.connect(self.btH5_click)
            self.btH6.clicked.connect(self.btH6_click)

            self.btH7.clicked.connect(self.btH7_click)
            self.btH8.clicked.connect(self.btH8_click)
            self.btH9.clicked.connect(self.btH9_click)
            self.btH10.clicked.connect(self.btH10_click)
            self.btH11.clicked.connect(self.btH11_click)
            self.btH12.clicked.connect(self.btH12_click)

            self.btH13.clicked.connect(self.btH13_click)
            self.btH14.clicked.connect(self.btH14_click)
            self.btH15.clicked.connect(self.btH15_click)
            self.btH16.clicked.connect(self.btH16_click)
            self.btH17.clicked.connect(self.btH17_click)
            self.btH18.clicked.connect(self.btH18_click)


        self.stTab = False
        self.allBtn =[self.btA,self.btB,self.btC,self.btD,self.btE,self.btF,self.btG,self.btH
            ,self.btI,self.btJ,self.btK,self.btL,self.btM,self.btN,self.btO,self.btP,self.btQ
            ,self.btR,self.btS,self.btT,self.btU,self.btV,self.btW,self.btX,self.btZ,self.btY]

        self.List_a = ['a','ă','â','à','á','ã','ả','ạ','ằ','ắ','ẵ','ẳ','ặ','ầ','ấ','ẫ','ẩ','ậ']
        self.List_u = ['u','ư','ù','ú', 'ũ', 'ủ', 'ụ' , 'ừ','ứ','ữ', 'ử' , 'ự']
        self.List_o = ['o','ô','ơ','ò','ó','õ','ỏ','ọ','ồ','ố','ổ','ỗ','ộ','ờ','ớ','ở','ỡ','ợ']
        self.List_i = ['i','ì','í','ĩ','ỉ','ị']
        self.List_y = ['y','ý','ỳ','ỹ','ỷ','ỵ']
        self.List_e = ['e','ê','è','é','ẻ','ẽ','ẹ','ề','ế','ể','ễ','ệ']
        self.List_d = ['d','đ']
        self.op = [self.btH1,self.btH2,self.btH3,self.btH4,self.btH5,self.btH6,self.btH7,self.btH8,self.btH9,
            self.btH10,self.btH11,self.btH12,self.btH13,self.btH14,self.btH15,self.btH16,self.btH17,self.btH18]
        self.btSetVisible(False)

    def btSetVisible(self,isShow):
        for bt in self.op:
            bt.setVisible(isShow)

    def exec_(self):
        super(Ui_KeyboardVN,self).exec_()
        return self.returnValue
    
    def btTab_click(self):
        self.stTab = not self.stTab
        for bt in self.allBtn :
            string = str(bt.text()).lower() if self.stTab else str(bt.text()).upper()
            bt.setText(string)
    
    def btH1_click(self):
        self.numberPress(self.btH1.text())
    def btH2_click(self):
        self.numberPress(self.btH2.text())
    def btH3_click(self):
        self.numberPress(self.btH3.text())
    def btH4_click(self):
        self.numberPress(self.btH4.text())
    def btH5_click(self):
        self.numberPress(self.btH5.text())
    def btH6_click(self):
        self.numberPress(self.btH6.text())
    
    def btH7_click(self):
        self.numberPress(self.btH7.text())
    def btH8_click(self):
        self.numberPress(self.btH8.text())
    def btH9_click(self):
        self.numberPress(self.btH9.text())
    def btH10_click(self):
        self.numberPress(self.btH10.text())
    def btH11_click(self):
        self.numberPress(self.btH11.text())
    def btH12_click(self):
        self.numberPress(self.btH12.text())

    def btH13_click(self):
        self.numberPress(self.btH13.text())
    def btH14_click(self):
        self.numberPress(self.btH14.text())
    def btH15_click(self):
        self.numberPress(self.btH15.text())
    def btH16_click(self):
        self.numberPress(self.btH16.text())
    def btH17_click(self):
        self.numberPress(self.btH17.text())
    def btH18_click(self):
        self.numberPress(self.btH18.text())
        
    def numberPress(self, charIn):
        self.returnValue += charIn
        self.lbValue.setText(self.returnValue)
    def btSpace_click(self):
        self.btSetVisible(False)
        self.numberPress(' ')
    def bt0_click(self):
        self.btSetVisible(False)
        self.numberPress('0')
    def bt1_click(self):
        self.btSetVisible(False)
        self.numberPress('1')
    def bt2_click(self):
        self.btSetVisible(False)
        self.numberPress('2')
    def bt3_click(self):
        self.btSetVisible(False)
        self.numberPress('3')
    def bt4_click(self):
        self.btSetVisible(False)
        self.numberPress('4')
    def bt5_click(self):
        self.btSetVisible(False)
        self.numberPress('5')
        self.btSetVisible(False)
    def bt6_click(self):
        self.btSetVisible(False)
        self.numberPress('6')
    def bt7_click(self):
        self.btSetVisible(False)
        self.numberPress('7')
    def bt8_click(self):
        self.btSetVisible(False)
        self.numberPress('8')
    def bt9_click(self):
        self.btSetVisible(False)
        self.numberPress('9')  
    def btQ_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btQ.text())
    def btW_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btW.text())
    def btR_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btR.text())
    def btT_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btT.text())
    def btP_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btP.text())
    def btS_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btS.text())
    def btF_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btF.text())
    def btG_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btG.text())
    def btH_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btH.text())
    def btJ_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btJ.text())
    def btK_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btK.text())
    def btL_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btL.text())
    def btZ_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btZ.text())
    def btX_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btX.text())
    def btC_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btC.text())
    def btV_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btV.text())
    def btB_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btB.text())
    def btN_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btN.text())
    def btM_click(self):
        self.btSetVisible(False)
        self.numberPress(self.btM.text())
    def btEnter_click(self):
        self.accept()
    
    def btClear_click(self):
        self.returnValue = self.returnValue[:(len(self.returnValue)-1)]
        self.lbValue.setText(self.returnValue)
    
    def btD_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_d)):
            self.op[i].setVisible(True)
            string = str(self.List_d[i]).lower() if self.stTab else str(self.List_d[i]).upper()
            self.op[i].setText(string)
    def btA_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_a)):
            self.op[i].setVisible(True)
            string = str(self.List_a[i]).lower() if self.stTab else str(self.List_a[i]).upper()
            self.op[i].setText(string)
    def btU_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_u)):
            self.op[i].setVisible(True)
            string = str(self.List_u[i]).lower() if self.stTab else str(self.List_u[i]).upper()
            self.op[i].setText(string)
    def btI_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_i)):
            self.op[i].setVisible(True)
            string = str(self.List_i[i]).lower() if self.stTab else str(self.List_i[i]).upper()
            self.op[i].setText(string)
    def btO_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_o)):
            self.op[i].setVisible(True)
            string = str(self.List_o[i]).lower() if self.stTab else str(self.List_o[i]).upper()
            self.op[i].setText(string)
    def btE_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_e)):
            self.op[i].setVisible(True)
            string = str(self.List_e[i]).lower() if self.stTab else str(self.List_e[i]).upper()
            self.op[i].setText(string)
    def btY_click(self):
        self.btSetVisible(False)
        for i in range(0, len(self.List_y)):
            self.op[i].setVisible(True)
            string = str(self.List_y[i]).lower() if self.stTab else str(self.List_y[i]).upper()
            self.op[i].setText(string)

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Keyboard = Ui_KeyboardVN()
    Keyboard.exec_()
    sys.exit(app.exec_())

"""