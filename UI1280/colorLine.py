# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorLine.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 478)
        Form.setStyleSheet("")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 276, 601, 77))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.columnView_5 = QtWidgets.QColumnView(self.horizontalLayoutWidget)
        self.columnView_5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.columnView_5.setObjectName("columnView_5")
        self.horizontalLayout.addWidget(self.columnView_5)
        self.columnView_4 = QtWidgets.QColumnView(self.horizontalLayoutWidget)
        self.columnView_4.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.columnView_4.setObjectName("columnView_4")
        self.horizontalLayout.addWidget(self.columnView_4)
        self.columnView_3 = QtWidgets.QColumnView(self.horizontalLayoutWidget)
        self.columnView_3.setStyleSheet("background-color: rgb(199, 142, 28);")
        self.columnView_3.setObjectName("columnView_3")
        self.horizontalLayout.addWidget(self.columnView_3)
        self.columnView_2 = QtWidgets.QColumnView(self.horizontalLayoutWidget)
        self.columnView_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.columnView_2.setObjectName("columnView_2")
        self.horizontalLayout.addWidget(self.columnView_2)
        self.columnView = QtWidgets.QColumnView(self.horizontalLayoutWidget)
        self.columnView.setEnabled(True)
        self.columnView.setStyleSheet("background-color: rgb(156, 0, 0);")
        self.columnView.setObjectName("columnView")
        self.horizontalLayout.addWidget(self.columnView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

