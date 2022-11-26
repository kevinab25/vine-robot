# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 1000)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainWidget = QtWidgets.QWidget(self.centralwidget)
        self.MainWidget.setGeometry(QtCore.QRect(20, 340, 831, 251))
        self.MainWidget.setMouseTracking(True)
        self.MainWidget.setObjectName("MainWidget")
        self.Sensor_lbl = QtWidgets.QLabel(self.MainWidget)
        self.Sensor_lbl.setGeometry(QtCore.QRect(10, 20, 81, 21))
        self.Sensor_lbl.setObjectName("Sensor_lbl")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.MainWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 351, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pressure_val_rcvd = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.pressure_val_rcvd.setReadOnly(True)
        self.pressure_val_rcvd.setObjectName("pressure_val_rcvd")
        self.gridLayout.addWidget(self.pressure_val_rcvd, 2, 1, 1, 1)
        self.pressure_val_rcvd_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.pressure_val_rcvd_2.setReadOnly(True)
        self.pressure_val_rcvd_2.setObjectName("pressure_val_rcvd_2")
        self.gridLayout.addWidget(self.pressure_val_rcvd_2, 2, 2, 1, 1)
        self.temp_val_rvcd = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.temp_val_rvcd.setEnabled(True)
        self.temp_val_rvcd.setReadOnly(True)
        self.temp_val_rvcd.setObjectName("temp_val_rvcd")
        self.gridLayout.addWidget(self.temp_val_rvcd, 0, 1, 1, 1)
        self.speed_val_rcvd = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.speed_val_rcvd.setReadOnly(True)
        self.speed_val_rcvd.setObjectName("speed_val_rcvd")
        self.gridLayout.addWidget(self.speed_val_rcvd, 1, 1, 1, 1)
        self.pressure_val_rcvd_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.pressure_val_rcvd_3.setReadOnly(True)
        self.pressure_val_rcvd_3.setObjectName("pressure_val_rcvd_3")
        self.gridLayout.addWidget(self.pressure_val_rcvd_3, 3, 1, 1, 1)
        self.pressure_val_rcvd_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.pressure_val_rcvd_4.setReadOnly(True)
        self.pressure_val_rcvd_4.setObjectName("pressure_val_rcvd_4")
        self.gridLayout.addWidget(self.pressure_val_rcvd_4, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.MainWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(420, 40, 241, 56))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.obj_ident_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.obj_ident_lbl.setObjectName("obj_ident_lbl")
        self.verticalLayout_3.addWidget(self.obj_ident_lbl)
        self.obj_fwing_lbl = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.obj_fwing_lbl.setObjectName("obj_fwing_lbl")
        self.verticalLayout_3.addWidget(self.obj_fwing_lbl)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.obj_ident_val = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_ident_val.setReadOnly(True)
        self.obj_ident_val.setObjectName("obj_ident_val")
        self.verticalLayout_4.addWidget(self.obj_ident_val)
        self.obj_fwing_val = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_fwing_val.setReadOnly(True)
        self.obj_fwing_val.setObjectName("obj_fwing_val")
        self.verticalLayout_4.addWidget(self.obj_fwing_val)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.obj_lbl = QtWidgets.QLabel(self.MainWidget)
        self.obj_lbl.setGeometry(QtCore.QRect(420, 20, 58, 16))
        self.obj_lbl.setObjectName("obj_lbl")
        self.mode_group = QtWidgets.QGroupBox(self.MainWidget)
        self.mode_group.setGeometry(QtCore.QRect(420, 120, 241, 111))
        self.mode_group.setCheckable(False)
        self.mode_group.setObjectName("mode_group")
        self.auto_mode_radioBtn = QtWidgets.QRadioButton(self.mode_group)
        self.auto_mode_radioBtn.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.auto_mode_radioBtn.setCheckable(True)
        self.auto_mode_radioBtn.setChecked(False)
        self.auto_mode_radioBtn.setObjectName("auto_mode_radioBtn")
        self.manual_mode_radioBtn = QtWidgets.QRadioButton(self.mode_group)
        self.manual_mode_radioBtn.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.manual_mode_radioBtn.setChecked(True)
        self.manual_mode_radioBtn.setObjectName("manual_mode_radioBtn")
        self.metric_label = QtWidgets.QLabel(self.MainWidget)
        self.metric_label.setGeometry(QtCore.QRect(10, 50, 168, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metric_label.sizePolicy().hasHeightForWidth())
        self.metric_label.setSizePolicy(sizePolicy)
        self.metric_label.setObjectName("metric_label")
        self.label_3 = QtWidgets.QLabel(self.MainWidget)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 167, 21))
        self.label_3.setObjectName("label_3")
        self.ConnectBtn = QtWidgets.QPushButton(self.MainWidget)
        self.ConnectBtn.setGeometry(QtCore.QRect(700, 160, 100, 32))
        self.ConnectBtn.setObjectName("ConnectBtn")
        self.port_line = QtWidgets.QLineEdit(self.MainWidget)
        self.port_line.setGeometry(QtCore.QRect(680, 80, 141, 61))
        self.port_line.setObjectName("port_line")
        self.port_label = QtWidgets.QLabel(self.MainWidget)
        self.port_label.setGeometry(QtCore.QRect(730, 50, 58, 16))
        self.port_label.setObjectName("port_label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 600, 311, 191))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 22))
        self.menubar.setObjectName("menubar")
        self.menuTest = QtWidgets.QMenu(self.menubar)
        self.menuTest.setObjectName("menuTest")
        self.menuControls = QtWidgets.QMenu(self.menubar)
        self.menuControls.setObjectName("menuControls")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.debugAction = QtGui.QAction(MainWindow)
        self.debugAction.setObjectName("debugAction")
        self.Main_Controller_action = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("camera-video")
        self.Main_Controller_action.setIcon(icon)
        self.Main_Controller_action.setObjectName("Main_Controller_action")
        self.menuTest.addAction(self.debugAction)
        self.menuControls.addAction(self.Main_Controller_action)
        self.menubar.addAction(self.menuTest.menuAction())
        self.menubar.addAction(self.menuControls.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vine Robot"))
        self.Sensor_lbl.setText(_translate("MainWindow", "Sensors"))
        self.label.setText(_translate("MainWindow", "Temperature (C)"))
        self.label_2.setText(_translate("MainWindow", "Acceleration"))
        self.label_4.setText(_translate("MainWindow", "Pressure"))
        self.label_5.setText(_translate("MainWindow", "Pressure"))
        self.obj_ident_lbl.setText(_translate("MainWindow", "Identified"))
        self.obj_fwing_lbl.setText(_translate("MainWindow", "Following"))
        self.obj_lbl.setText(_translate("MainWindow", "Object "))
        self.mode_group.setTitle(_translate("MainWindow", "Mode"))
        self.auto_mode_radioBtn.setText(_translate("MainWindow", "Autonomous"))
        self.manual_mode_radioBtn.setText(_translate("MainWindow", "Manual"))
        self.metric_label.setText(_translate("MainWindow", "Metric"))
        self.label_3.setText(_translate("MainWindow", "Value"))
        self.ConnectBtn.setText(_translate("MainWindow", "Connect"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Reference Keys:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">w -&gt; start going forward</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">d -&gt; steer right</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a -&gt; steer left</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">s -&gt; retract</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">h -&gt; halt/stop</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">z -&gt; emergency stop</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">x -&gt; quick inflate</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">c -&gt; close all valves</p></body></html>"))
        self.menuTest.setTitle(_translate("MainWindow", "Test"))
        self.menuControls.setTitle(_translate("MainWindow", "Controls"))
        self.debugAction.setText(_translate("MainWindow", "Debug Window"))
        self.debugAction.setStatusTip(_translate("MainWindow", "Test the pneumatic valves"))
        self.Main_Controller_action.setText(_translate("MainWindow", "Main Controller"))
        self.Main_Controller_action.setStatusTip(_translate("MainWindow", "Open controller for the vine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
