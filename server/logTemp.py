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
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from time import strftime

from kbNumber import Ui_Dialog
import server


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
        
        ax.plot( dtIn, 'r-',color='skyblue',label='Trong tủ')
        ax.plot( dtOut, 'r-',color='red',label='Ngoài tủ')
        
        labels = [item.get_text() for item in ax.get_xticklabels()]
        numStep = int(len(dtX) / len(labels)) + 1
        j=0
        if numStep > 1 :
            for i in range(0, len(dtX),numStep):
                labels[j] = dtX[i]
                j+=1
        else:
            dtxT,runT = 0,1 
            dtxP,runP = len(dtX) -1 , len(labels)-2
            while dtxT <= dtxP and runT <= runP:
                labels[runP] = dtX[dtxP]
                labels[runT] = dtX[dtxT]
                runP -= 1
                runT += 1
                dtxP -= 1
                dtxT += 1
  
        ax.legend(loc=1)
        ax.set_xticklabels(labels,rotation=45)

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
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/background.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{font: 26pt \"Arial\";background-color: #4e9400;color: #ffffff;border-radius: 20px}.QLabel{color:#000000;font: 32pt \"Arial\";}.MyQLineEdit{font:  30pt \"Arial\";background-color: #ffffff;color: #000000;border: 2px solid gray;border-radius: 10px;padding: 0 8px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(50, 610, 160, 80))
        self.btBack.setObjectName("btBack")
        self.btTemHumi = QtWidgets.QPushButton(self.frame)
        self.btTemHumi.setGeometry(QtCore.QRect(50, 490, 160, 80))
        self.btTemHumi.setObjectName("btTemHumi")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 111, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 420, 141, 50))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tbYear = MyQLineEdit(self.frame)
        self.tbYear.setGeometry(QtCore.QRect(140, 410, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tbYear.setFont(font)
        self.tbYear.setObjectName("tbYear")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 330, 131, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tbDay = MyQLineEdit(self.frame)
        self.tbDay.setGeometry(QtCore.QRect(140, 240, 121, 61))
        
        self.tbDay.setFont(font)
        self.tbDay.setObjectName("tbDay")
        self.tbMonth = MyQLineEdit(self.frame)
        self.tbMonth.setGeometry(QtCore.QRect(140, 320, 121, 61))
       
        self.tbMonth.setFont(font)
        self.tbMonth.setObjectName("tbMonth")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 111, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tbNumTu = MyQLineEdit(self.frame)
        self.tbNumTu.setGeometry(QtCore.QRect(140, 160, 121, 61))
        
        self.tbNumTu.setFont(font)
        self.tbNumTu.setObjectName("tbNumTu")

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
                
        self.btBack.clicked.connect(SV_Login.close)
        self.setEvent()

    def setEvent(self):
        self.seeTemp = True
        self.tbNumTu.setText(str(server.myNumberTu))
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
        numMaxLeft = server.numClientLeft + server.numClientRight + 1
        
        dialogKey= Ui_Dialog(numMaxLeft)
        
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
        # 22:05 1 23 22 24 24
        dtIn = []
        dtOut = []
        dtX = []
        nameTu = str(self.tbNumTu.text())
        monthText = str(self.tbMonth.text())
        if len(monthText) == 1 :
            monthText = '0' + monthText
        dayText = str(self.tbDay.text())
        if len(dayText) == 1:
            dayText = '0' + dayText
        nameFile = str(self.tbYear.text())+monthText+dayText+'.txt'
        try :
            fileR = open('/home/pi/backup/temp/'+nameFile,"r")
            while True:
                line = fileR.readline()
                if not line: 
                    break
                else:
                    dt = line.split(' ')
                    if dt[1] == nameTu :
                        if float(dt[2]) < 100 and  float(dt[3]) < 100 and float(dt[4])<100 and float(dt[5]) < 100 :
                            if self.seeTemp :
                                dtIn.append(float(dt[2]))
                                dtOut.append(float(dt[4]))
                            else :
                                dtIn.append(float(dt[3]))
                                dtOut.append(float(dt[5]))
                            dtX.append(dt[0])
        except Exception as e:
            print('Exeption in readFile',e.__doc__)
        return dtIn, dtOut , dtX

import resources


'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_Login = QtWidgets.QWidget()
    ui = Ui_SV_LogTemp()
    ui.setupUi(SV_Login)
    SV_Login.show()
    sys.exit(app.exec_())
'''