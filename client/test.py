# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
import sys


class MyQFrame(QtWidgets.QFrame):
    #
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QFrame.mousePressEvent(self, event)

class Ui_welcomeForm(object):
    def setupUi(self, welcomeForm):
        welcomeForm.setObjectName("welcomeForm")
        welcomeForm.setWindowTitle("welcomeClient")
        welcomeForm.resize(1024, 600)
        self.welcomeForm = welcomeForm
        self.frame = MyQFrame(welcomeForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet(".MyQFrame{background-image: url(:/images/welcome.jpg);}")
        self.frame.clicked.connect(self.frame_click)

        #endUI
        self.setEvent()

    def setEvent(self):
        self.isOpenForm =False
        ctimer = QTimer(self.frame)
        ctimer.timeout.connect(self.checkServerActive)
        ctimer.start(200)

    def checkServerActive(self):
        pass

    def frame_click(self):
        pass

import resources

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    welcomeForm = QtWidgets.QWidget()
    ui = Ui_welcomeForm()
    ui.setupUi(welcomeForm)
    welcomeForm.show()
    pass
    sys.exit(app.exec_())

