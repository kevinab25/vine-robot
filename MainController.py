# Form implementation generated from reading ui file 'MainController.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainController(object):
    def setupUi(self, MainController):
        MainController.setObjectName("MainController")
        MainController.resize(957, 593)
        self.centralwidget = QtWidgets.QWidget(MainController)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 110, 100, 32))
        icon = QtGui.QIcon.fromTheme("application-x-executable")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        MainController.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainController)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 22))
        self.menubar.setObjectName("menubar")
        MainController.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainController)
        self.statusbar.setObjectName("statusbar")
        MainController.setStatusBar(self.statusbar)

        self.retranslateUi(MainController)
        QtCore.QMetaObject.connectSlotsByName(MainController)

    def retranslateUi(self, MainController):
        _translate = QtCore.QCoreApplication.translate
        MainController.setWindowTitle(_translate("MainController", "MainWindow"))
        self.pushButton.setText(_translate("MainController", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainController = QtWidgets.QMainWindow()
    ui = Ui_MainController()
    ui.setupUi(MainController)
    MainController.show()
    sys.exit(app.exec())
