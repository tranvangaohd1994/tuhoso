# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logTemp.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
#install matplotlib befor run
#pip3 install matplotlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
from PyQt5.QtWidgets import (QWidget,QLineEdit,QDialog ,QGridLayout,QSizePolicy, QLabel,QPushButton,QMainWindow,QApplication,QWidget,QHBoxLayout)
from kbNumber import Ui_Dialog
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from time import strftime


class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        #self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
 
    def plot(self,istemp,dtIn,dtOut,dtX):
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(dtX,dtIn, 'r-',color='skyblue',label='Trong tủ')
        ax.plot(dtX,dtOut, 'r-',color='red',label='Ngoài tủ')
        ax.legend(loc=1)

        for tick in ax.get_xticklabels():
            tick.set_rotation(45)

        if istemp:
            ax.set_title("Nhiệt độ")
        else :
            ax.set_title("Độ ẩm")

        self.draw()

class Ui_SV_LogTemp(object):
    def setupUi(self, SV_Login):
        SV_Login.setObjectName("SV_Login")
        SV_Login.resize(1280, 800)
        self.frame = QtWidgets.QFrame(SV_Login)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}")
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
        self.tbYear = MyQLineEdit(self.frame)
        self.tbYear.setGeometry(QtCore.QRect(140, 480, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
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
        self.tbDay = MyQLineEdit(self.frame)
        self.tbDay.setGeometry(QtCore.QRect(140, 310, 121, 61))
        
        self.tbDay.setFont(font)
        self.tbDay.setObjectName("tbDay")
        self.tbMonth = MyQLineEdit(self.frame)
        self.tbMonth.setGeometry(QtCore.QRect(140, 390, 121, 61))
        
        self.tbMonth.setFont(font)
        self.tbMonth.setObjectName("tbMonth")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 240, 111, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tbNumTu = MyQLineEdit(self.frame)
        self.tbNumTu.setGeometry(QtCore.QRect(140, 230, 121, 61))
        
        self.tbNumTu.setFont(font)
        self.tbNumTu.setObjectName("tbNumTu")
        self.grcdControl_2 = QtWidgets.QGroupBox(self.frame)
        self.grcdControl_2.setGeometry(QtCore.QRect(0, 110, 281, 131))
        self.grcdControl_2.setStyleSheet(".QRadioButton{font: 75 26pt \"Arial\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl_2.setTitle("")
        self.grcdControl_2.setObjectName("grcdControl_2")
        self.rbPhai = QtWidgets.QRadioButton(self.grcdControl_2)
        self.rbPhai.setGeometry(QtCore.QRect(140, 39, 111, 71))
        self.rbPhai.setObjectName("rbPhai")
        self.rbTrai = QtWidgets.QRadioButton(self.grcdControl_2)
        self.rbTrai.setGeometry(QtCore.QRect(10, 39, 111, 71))
        self.rbTrai.setChecked(True)
        self.rbTrai.setObjectName("rbTrai")

        self.retranslateUi(SV_Login)
        QtCore.QMetaObject.connectSlotsByName(SV_Login)

    def retranslateUi(self, SV_Login):
        _translate = QtCore.QCoreApplication.translate
        SV_Login.setWindowTitle(_translate("SV_Login", "Form"))
        self.btBack.setText(_translate("SV_Login", "Quay lại"))
        self.btTemHumi.setText(_translate("SV_Login", "Độ ẩm")) #"Nhiệt độ"))
        self.label_7.setText(_translate("SV_Login", "Ngày"))
        self.label_5.setText(_translate("SV_Login", "Năm"))
        self.label_3.setText(_translate("SV_Login", "Tháng"))
        self.label_8.setText(_translate("SV_Login", "Tủ"))
        self.tbNumTu.setText(_translate("SV_Login", "1"))
        self.rbPhai.setText(_translate("SV_Login", "Phải"))
        self.rbTrai.setText(_translate("SV_Login", "Trái"))

        
        self.btBack.clicked.connect(SV_Login.close)
        self.setEvent()

    def setEvent(self):
        self.seeTemp = True

        self.tbYear.setText(str(strftime("%Y")))
        self.tbMonth.setText(str(strftime("%m")))
        self.tbDay.setText(str(strftime("%d")))
        
        self.tbNumTu.clicked.connect(self.tbNumTu_click)
        self.tbYear.clicked.connect(self.tbYear_click)
        self.tbMonth.clicked.connect(self.tbMonth_click)
        self.tbDay.clicked.connect(self.tbDay_click)
        self.btTemHumi.clicked.connect(self.btTemHumi_click)

        self.map = PlotCanvas(self.frame, width=9.5, height=6)
        self.map.move(320,150)
        
        #readData
        dtIn, dtOut , dtX = self.readFile()
        self.map.plot(True,dtIn, dtOut , dtX)
        
        
    def btTemHumi_click(self):
        if self.seeTemp == True :
            self.seeTemp = False
            self.btTemHumi.setText("Nhiệt độ")
        else:
            self.seeTemp = True
            self.btTemHumi.setText("Độ ẩm")

        #readData
        dtIn, dtOut , dtX = self.readFile()
        self.map.plot(self.seeTemp,dtIn, dtOut , dtX)


    def tbNumTu_click(self):
        numMaxLeft = 2
        numMaxRight = 0
        if self.rbTrai.isChecked():
            dialogKey= Ui_Dialog(numMaxLeft)
        else :
            dialogKey= Ui_Dialog(numMaxRight)
        
        value = dialogKey.exec_()
        if value :
            self.tbNumTu.setText(value)

    def tbDay_click(self):
        dialogKey= Ui_Dialog(31)
        value = dialogKey.exec_()
        if value :
            self.tbDay.setText(value)

    def tbMonth_click(self):
        dialogKey= Ui_Dialog(12)
        value = dialogKey.exec_()
        if value :
            self.tbMonth.setText(value)
            
    def tbYear_click(self):
        dialogKey= Ui_Dialog(3000)
        value = dialogKey.exec_()
        if value :
            self.tbYear.setText(value)

    def readFile(self):
        a = open("/home/pi/Desktop/temp.log","r")
        dtIn = []
        dtOut = []
        dtX = []
        nameTu = ""
        if self.rbTrai.isChecked(): #tu trai duoc check
            nameTu = "Left_"
        else :
            nameTu = "Right_"
        nameTu += str(self.tbNumTu.text())

        date = str(self.tbYear.text())+"-"+str(self.tbMonth.text())+"-"+str(self.tbDay.text())

        while True:
            line = a.readline()
            if not line: 
                break
            else:
                dt = line.split(' ')
                if dt[0] == date and dt[3] == nameTu :
                    if self.seeTemp :
                        dtIn.append(dt[4])
                        dtOut.append(dt[6])
                    else :
                        dtIn.append(dt[5])
                        dtOut.append(dt[7])
                    dtx = dt[1].split(':')
                    dtX.append(dtx[0]+":"+dtx[1])
        return dtIn, dtOut , dtX

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_Login = QtWidgets.QWidget()
    ui = Ui_SV_LogTemp()
    ui.setupUi(SV_Login)
    SV_Login.show()
    sys.exit(app.exec_())

"""