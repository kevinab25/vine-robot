# Form implementation generated from reading ui file 'FindPort.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 184)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(20)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.port_val = QtWidgets.QLineEdit(Dialog)
        self.port_val.setGeometry(QtCore.QRect(20, 80, 231, 21))
        self.port_val.setObjectName("port_val")
        self.connectBtn = QtWidgets.QPushButton(Dialog)
        self.connectBtn.setGeometry(QtCore.QRect(230, 121, 121, 41))
        self.connectBtn.setObjectName("connectBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Arduino Port:"))
        self.connectBtn.setText(_translate("Dialog", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())