# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_welcomeForm(object):
    def setupUi(self, welcomeForm):
        welcomeForm.setObjectName("welcomeForm")
        welcomeForm.resize(1280, 800)
        welcomeForm.setStyleSheet("#welcomeForm{background-image: url(:/images/welcome.jpg);}\n"
"#btExit{border: none;background-color: none;}#frame{border: none;background-color: none;}")
        self.frame = QtWidgets.QFrame(welcomeForm)
        self.frame.setGeometry(QtCore.QRect(0, 149, 1280, 631))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btExit = QtWidgets.QPushButton(welcomeForm)
        self.btExit.setGeometry(QtCore.QRect(0, 0, 161, 91))
        self.btExit.setStyleSheet("")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")

        self.retranslateUi(welcomeForm)
        QtCore.QMetaObject.connectSlotsByName(welcomeForm)

    def retranslateUi(self, welcomeForm):
        _translate = QtCore.QCoreApplication.translate
        welcomeForm.setWindowTitle(_translate("welcomeForm", "Form"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcomeForm = QtWidgets.QWidget()
    ui = Ui_welcomeForm()
    ui.setupUi(welcomeForm)
    welcomeForm.show()
    sys.exit(app.exec_())

