# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_ChonClient.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
import server

from SV_CaiDatNangCao import Ui_SVCaiDatNangCao

class Ui_SVChonClientV2(object):
    def setupUi(self, SVChonClient):
        SVChonClient.setObjectName("SVChonClient")
        SVChonClient.resize(1280, 800)
        self.SVChonClient = SVChonClient
        self.frame = QtWidgets.QFrame(SVChonClient)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}.QLabel{color:#F44336 ;font: 75  30pt \"Arial\";}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}#btBack{color:white;border-image: url(:/images/back.png);}QCheckBox{font: 75 30pt \"Arial\";color: white;background-color: #55007f;}.QCheckBox::indicator{width: 35px;height: 30px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(370, 140, 600, 81))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(150, 550, 211, 111))
        self.btBack.setObjectName("btBack")

        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(210, 260, 901, 261))
        self.grcdControl.setStyleSheet(".QRadioButton{font: 75 26pt \"Arial\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.cbTu02 = QtWidgets.QRadioButton(self.grcdControl)
        self.cbTu02.setGeometry(QtCore.QRect(570, 70, 171, 100))
        self.cbTu02.setObjectName("cbTu02")

        self.cbTu01 = QtWidgets.QRadioButton(self.grcdControl)
        self.cbTu01.setGeometry(QtCore.QRect(190, 70, 161, 100))
        self.cbTu01.setChecked(True)
        self.cbTu01.setObjectName("cbTu01")

        self.btCaiDat = QtWidgets.QPushButton(self.frame)
        self.btCaiDat.setGeometry(QtCore.QRect(940, 550, 211, 111))
        self.btCaiDat.setObjectName("btCaiDat")
        

        self.retranslateUi(SVChonClient)
        QtCore.QMetaObject.connectSlotsByName(SVChonClient)

    def retranslateUi(self, SVChonClient):
        _translate = QtCore.QCoreApplication.translate
        SVChonClient.setWindowTitle(_translate("SVChonClient", "Form"))
        self.lbtitle.setText(_translate("SVChonClient", "Chọn tủ cài đặt"))
        self.btBack.setText(_translate("SVChonClient", "Quay lại"))
        self.cbTu01.setText(_translate("SVChonClient", "Tủ trái"))

        self.cbTu02.setText(_translate("SVChonClient", "Tủ phải"))
        self.btCaiDat.setText(_translate("SVChonClient", "Cài đặt"))
        
        self.setEvent()
    
    def setEvent(self):
       
        self.btBack.clicked.connect(self.btBack_click)
        self.btCaiDat.clicked.connect(self.btCaiDat_click)
        
    def btBack_click(self):
        self.SVChonClient.close()
    def btCaiDat_click(self):
        #ko phia nao duoc check
        if self.checkTuIsChoose() == False:
            return
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SVCaiDatNangCao()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen :
            self.window.showFullScreen()
        #self.window.showFullScreen() 
        self.SVChonClient.close()
    
    # check box change state
    def checkTuIsChoose(self):
        if self.cbTu01.isChecked() or self.cbTu02.isChecked():
            return True
        return False


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVChonClient = QtWidgets.QWidget()
    ui = Ui_SVChonClient()
    ui.setupUi(SVChonClient)
    SVChonClient.show()
    sys.exit(app.exec_())
"""