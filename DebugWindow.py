# Form implementation generated from reading ui file 'DebugWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        DebugWindow.setObjectName("DebugWindow")
        DebugWindow.resize(1035, 624)
        self.centralwidget = QtWidgets.QWidget(DebugWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 50, 311, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Valve2On = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve2On.setObjectName("Valve2On")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.Valve2On)
        self.gridLayout.addWidget(self.Valve2On, 1, 1, 1, 1)
        self.Valve3Off = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve3Off.setObjectName("Valve3Off")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.Valve3Off)
        self.gridLayout.addWidget(self.Valve3Off, 2, 2, 1, 1)
        self.Valve4On = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve4On.setObjectName("Valve4On")
        self.buttonGroup_4 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_4.setObjectName("buttonGroup_4")
        self.buttonGroup_4.addButton(self.Valve4On)
        self.gridLayout.addWidget(self.Valve4On, 3, 1, 1, 1)
        self.Valve3On = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve3On.setObjectName("Valve3On")
        self.buttonGroup_3.addButton(self.Valve3On)
        self.gridLayout.addWidget(self.Valve3On, 2, 1, 1, 1)
        self.Valve5Off = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve5Off.setObjectName("Valve5Off")
        self.buttonGroup_5 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_5.setObjectName("buttonGroup_5")
        self.buttonGroup_5.addButton(self.Valve5Off)
        self.gridLayout.addWidget(self.Valve5Off, 4, 2, 1, 1)
        self.Valve5On = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve5On.setObjectName("Valve5On")
        self.buttonGroup_5.addButton(self.Valve5On)
        self.gridLayout.addWidget(self.Valve5On, 4, 1, 1, 1)
        self.Valve4Off = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve4Off.setObjectName("Valve4Off")
        self.buttonGroup_4.addButton(self.Valve4Off)
        self.gridLayout.addWidget(self.Valve4Off, 3, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.Valve2Off = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve2Off.setObjectName("Valve2Off")
        self.buttonGroup_2.addButton(self.Valve2Off)
        self.gridLayout.addWidget(self.Valve2Off, 1, 2, 1, 1)
        self.Valve1On = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve1On.setObjectName("Valve1On")
        self.gridLayout.addWidget(self.Valve1On, 0, 1, 1, 1)
        self.Valve1Off = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.Valve1Off.setObjectName("Valve1Off")
        self.gridLayout.addWidget(self.Valve1Off, 0, 2, 1, 1)
        self.Pneumatics_label = QtWidgets.QLabel(self.centralwidget)
        self.Pneumatics_label.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.Pneumatics_label.setObjectName("Pneumatics_label")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 300, 311, 151))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Ball1OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball1OffRbtn.setObjectName("Ball1OffRbtn")
        self.buttonGroup_9 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_9.setObjectName("buttonGroup_9")
        self.buttonGroup_9.addButton(self.Ball1OffRbtn)
        self.gridLayout_2.addWidget(self.Ball1OffRbtn, 0, 2, 1, 1)
        self.Ball3OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball3OffRbtn.setObjectName("Ball3OffRbtn")
        self.buttonGroup_11 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_11.setObjectName("buttonGroup_11")
        self.buttonGroup_11.addButton(self.Ball3OffRbtn)
        self.gridLayout_2.addWidget(self.Ball3OffRbtn, 2, 2, 1, 1)
        self.BV1lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.BV1lbl.setObjectName("BV1lbl")
        self.gridLayout_2.addWidget(self.BV1lbl, 0, 0, 1, 1)
        self.Ball1OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball1OnRbtn.setObjectName("Ball1OnRbtn")
        self.buttonGroup_9.addButton(self.Ball1OnRbtn)
        self.gridLayout_2.addWidget(self.Ball1OnRbtn, 0, 1, 1, 1)
        self.Ball2OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball2OffRbtn.setObjectName("Ball2OffRbtn")
        self.buttonGroup_10 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_10.setObjectName("buttonGroup_10")
        self.buttonGroup_10.addButton(self.Ball2OffRbtn)
        self.gridLayout_2.addWidget(self.Ball2OffRbtn, 1, 2, 1, 1)
        self.BV4lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.BV4lbl.setObjectName("BV4lbl")
        self.gridLayout_2.addWidget(self.BV4lbl, 3, 0, 1, 1)
        self.BV3lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.BV3lbl.setObjectName("BV3lbl")
        self.gridLayout_2.addWidget(self.BV3lbl, 2, 0, 1, 1)
        self.Ball2OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball2OnRbtn.setObjectName("Ball2OnRbtn")
        self.buttonGroup_10.addButton(self.Ball2OnRbtn)
        self.gridLayout_2.addWidget(self.Ball2OnRbtn, 1, 1, 1, 1)
        self.Ball4OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball4OnRbtn.setObjectName("Ball4OnRbtn")
        self.buttonGroup_12 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_12.setObjectName("buttonGroup_12")
        self.buttonGroup_12.addButton(self.Ball4OnRbtn)
        self.gridLayout_2.addWidget(self.Ball4OnRbtn, 3, 1, 1, 1)
        self.Ball3OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball3OnRbtn.setObjectName("Ball3OnRbtn")
        self.buttonGroup_11.addButton(self.Ball3OnRbtn)
        self.gridLayout_2.addWidget(self.Ball3OnRbtn, 2, 1, 1, 1)
        self.BV2lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.BV2lbl.setObjectName("BV2lbl")
        self.gridLayout_2.addWidget(self.BV2lbl, 1, 0, 1, 1)
        self.Ball4OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.Ball4OffRbtn.setObjectName("Ball4OffRbtn")
        self.buttonGroup_12.addButton(self.Ball4OffRbtn)
        self.gridLayout_2.addWidget(self.Ball4OffRbtn, 3, 2, 1, 1)
        self.BVallPause = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.BVallPause.setObjectName("BVallPause")
        self.buttonGroup_9.addButton(self.BVallPause)
        self.gridLayout_2.addWidget(self.BVallPause, 0, 3, 1, 1)
        self.BVallPause_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.BVallPause_2.setObjectName("BVallPause_2")
        self.buttonGroup_10.addButton(self.BVallPause_2)
        self.gridLayout_2.addWidget(self.BVallPause_2, 1, 3, 1, 1)
        self.BVallPause_3 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.BVallPause_3.setObjectName("BVallPause_3")
        self.buttonGroup_11.addButton(self.BVallPause_3)
        self.gridLayout_2.addWidget(self.BVallPause_3, 2, 3, 1, 1)
        self.BVallPause_4 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.BVallPause_4.setObjectName("BVallPause_4")
        self.buttonGroup_12.addButton(self.BVallPause_4)
        self.gridLayout_2.addWidget(self.BVallPause_4, 3, 3, 1, 1)
        self.Ball_valve_label = QtWidgets.QLabel(self.centralwidget)
        self.Ball_valve_label.setGeometry(QtCore.QRect(40, 280, 71, 16))
        self.Ball_valve_label.setObjectName("Ball_valve_label")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(420, 50, 431, 191))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Motor3_rev = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor3_rev.setObjectName("Motor3_rev")
        self.buttonGroup_8 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_8.setObjectName("buttonGroup_8")
        self.buttonGroup_8.addButton(self.Motor3_rev)
        self.gridLayout_3.addWidget(self.Motor3_rev, 2, 2, 1, 1)
        self.Motor2_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Motor2_label.setObjectName("Motor2_label")
        self.gridLayout_3.addWidget(self.Motor2_label, 1, 0, 1, 1)
        self.Motor1_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Motor1_speed.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Motor1_speed.setReadOnly(False)
        self.Motor1_speed.setObjectName("Motor1_speed")
        self.gridLayout_3.addWidget(self.Motor1_speed, 0, 4, 1, 1)
        self.Motor3_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Motor3_label.setObjectName("Motor3_label")
        self.gridLayout_3.addWidget(self.Motor3_label, 2, 0, 1, 1)
        self.Motor2_rev = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor2_rev.setObjectName("Motor2_rev")
        self.buttonGroup_7 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_7.setObjectName("buttonGroup_7")
        self.buttonGroup_7.addButton(self.Motor2_rev)
        self.gridLayout_3.addWidget(self.Motor2_rev, 1, 2, 1, 1)
        self.send_speed1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.send_speed1.setObjectName("send_speed1")
        self.gridLayout_3.addWidget(self.send_speed1, 0, 5, 1, 1)
        self.Motor2_fwd = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor2_fwd.setObjectName("Motor2_fwd")
        self.buttonGroup_7.addButton(self.Motor2_fwd)
        self.gridLayout_3.addWidget(self.Motor2_fwd, 1, 1, 1, 1)
        self.Motor1_label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.Motor1_label.setObjectName("Motor1_label")
        self.gridLayout_3.addWidget(self.Motor1_label, 0, 0, 1, 1)
        self.Motor3_fwd = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor3_fwd.setObjectName("Motor3_fwd")
        self.buttonGroup_8.addButton(self.Motor3_fwd)
        self.gridLayout_3.addWidget(self.Motor3_fwd, 2, 1, 1, 1)
        self.send_speed3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.send_speed3.setObjectName("send_speed3")
        self.gridLayout_3.addWidget(self.send_speed3, 2, 5, 1, 1)
        self.Motor2_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Motor2_speed.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Motor2_speed.setReadOnly(False)
        self.Motor2_speed.setObjectName("Motor2_speed")
        self.gridLayout_3.addWidget(self.Motor2_speed, 1, 4, 1, 1)
        self.Motor1_fwd = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor1_fwd.setObjectName("Motor1_fwd")
        self.buttonGroup_6 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_6.setObjectName("buttonGroup_6")
        self.buttonGroup_6.addButton(self.Motor1_fwd)
        self.gridLayout_3.addWidget(self.Motor1_fwd, 0, 1, 1, 1)
        self.Motor1_rev = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor1_rev.setObjectName("Motor1_rev")
        self.buttonGroup_6.addButton(self.Motor1_rev)
        self.gridLayout_3.addWidget(self.Motor1_rev, 0, 2, 1, 1)
        self.Motor3_speed = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.Motor3_speed.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.Motor3_speed.setReadOnly(False)
        self.Motor3_speed.setObjectName("Motor3_speed")
        self.gridLayout_3.addWidget(self.Motor3_speed, 2, 4, 1, 1)
        self.send_speed2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.send_speed2.setObjectName("send_speed2")
        self.gridLayout_3.addWidget(self.send_speed2, 1, 5, 1, 1)
        self.Motor1Off = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor1Off.setObjectName("Motor1Off")
        self.buttonGroup_6.addButton(self.Motor1Off)
        self.gridLayout_3.addWidget(self.Motor1Off, 0, 3, 1, 1)
        self.Motor2Off = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor2Off.setObjectName("Motor2Off")
        self.buttonGroup_7.addButton(self.Motor2Off)
        self.gridLayout_3.addWidget(self.Motor2Off, 1, 3, 1, 1)
        self.Motor3Off = QtWidgets.QRadioButton(self.gridLayoutWidget_3)
        self.Motor3Off.setObjectName("Motor3Off")
        self.buttonGroup_8.addButton(self.Motor3Off)
        self.gridLayout_3.addWidget(self.Motor3Off, 2, 3, 1, 1)
        self.Motor_label = QtWidgets.QLabel(self.centralwidget)
        self.Motor_label.setGeometry(QtCore.QRect(420, 30, 58, 16))
        self.Motor_label.setObjectName("Motor_label")
        self.MotorSpeedlbl = QtWidgets.QLabel(self.centralwidget)
        self.MotorSpeedlbl.setGeometry(QtCore.QRect(690, 30, 58, 16))
        self.MotorSpeedlbl.setObjectName("MotorSpeedlbl")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(420, 300, 311, 151))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Ball5OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball5OffRbtn.setObjectName("Ball5OffRbtn")
        self.buttonGroup = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.Ball5OffRbtn)
        self.gridLayout_4.addWidget(self.Ball5OffRbtn, 0, 2, 1, 1)
        self.Ball7OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball7OffRbtn.setObjectName("Ball7OffRbtn")
        self.buttonGroup_14 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_14.setObjectName("buttonGroup_14")
        self.buttonGroup_14.addButton(self.Ball7OffRbtn)
        self.gridLayout_4.addWidget(self.Ball7OffRbtn, 2, 2, 1, 1)
        self.BV5lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BV5lbl.setObjectName("BV5lbl")
        self.gridLayout_4.addWidget(self.BV5lbl, 0, 0, 1, 1)
        self.Ball5OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball5OnRbtn.setObjectName("Ball5OnRbtn")
        self.buttonGroup.addButton(self.Ball5OnRbtn)
        self.gridLayout_4.addWidget(self.Ball5OnRbtn, 0, 1, 1, 1)
        self.Ball6OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball6OffRbtn.setObjectName("Ball6OffRbtn")
        self.buttonGroup_13 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_13.setObjectName("buttonGroup_13")
        self.buttonGroup_13.addButton(self.Ball6OffRbtn)
        self.gridLayout_4.addWidget(self.Ball6OffRbtn, 1, 2, 1, 1)
        self.BV8lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BV8lbl.setObjectName("BV8lbl")
        self.gridLayout_4.addWidget(self.BV8lbl, 3, 0, 1, 1)
        self.BV7lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BV7lbl.setObjectName("BV7lbl")
        self.gridLayout_4.addWidget(self.BV7lbl, 2, 0, 1, 1)
        self.Ball6OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball6OnRbtn.setObjectName("Ball6OnRbtn")
        self.buttonGroup_13.addButton(self.Ball6OnRbtn)
        self.gridLayout_4.addWidget(self.Ball6OnRbtn, 1, 1, 1, 1)
        self.Ball8OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball8OnRbtn.setObjectName("Ball8OnRbtn")
        self.buttonGroup_15 = QtWidgets.QButtonGroup(DebugWindow)
        self.buttonGroup_15.setObjectName("buttonGroup_15")
        self.buttonGroup_15.addButton(self.Ball8OnRbtn)
        self.gridLayout_4.addWidget(self.Ball8OnRbtn, 3, 1, 1, 1)
        self.Ball7OnRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball7OnRbtn.setObjectName("Ball7OnRbtn")
        self.buttonGroup_14.addButton(self.Ball7OnRbtn)
        self.gridLayout_4.addWidget(self.Ball7OnRbtn, 2, 1, 1, 1)
        self.BV6lbl = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.BV6lbl.setObjectName("BV6lbl")
        self.gridLayout_4.addWidget(self.BV6lbl, 1, 0, 1, 1)
        self.Ball8OffRbtn = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.Ball8OffRbtn.setObjectName("Ball8OffRbtn")
        self.buttonGroup_15.addButton(self.Ball8OffRbtn)
        self.gridLayout_4.addWidget(self.Ball8OffRbtn, 3, 2, 1, 1)
        self.BVallPause_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.BVallPause_5.setObjectName("BVallPause_5")
        self.gridLayout_4.addWidget(self.BVallPause_5, 0, 3, 1, 1)
        self.BVallPause_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.BVallPause_6.setObjectName("BVallPause_6")
        self.gridLayout_4.addWidget(self.BVallPause_6, 1, 3, 1, 1)
        self.BVallPause_7 = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.BVallPause_7.setObjectName("BVallPause_7")
        self.gridLayout_4.addWidget(self.BVallPause_7, 2, 3, 1, 1)
        self.BVallPause_8 = QtWidgets.QRadioButton(self.gridLayoutWidget_4)
        self.BVallPause_8.setObjectName("BVallPause_8")
        self.gridLayout_4.addWidget(self.BVallPause_8, 3, 3, 1, 1)
        self.Ball_valve_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Ball_valve_label_2.setGeometry(QtCore.QRect(420, 280, 71, 16))
        self.Ball_valve_label_2.setObjectName("Ball_valve_label_2")
        self.closeAll = QtWidgets.QPushButton(self.centralwidget)
        self.closeAll.setGeometry(QtCore.QRect(40, 480, 100, 32))
        self.closeAll.setObjectName("closeAll")
        DebugWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DebugWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 36))
        self.menubar.setObjectName("menubar")
        DebugWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DebugWindow)
        self.statusbar.setObjectName("statusbar")
        DebugWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DebugWindow)
        QtCore.QMetaObject.connectSlotsByName(DebugWindow)

    def retranslateUi(self, DebugWindow):
        _translate = QtCore.QCoreApplication.translate
        DebugWindow.setWindowTitle(_translate("DebugWindow", "MainWindow"))
        self.Valve2On.setText(_translate("DebugWindow", "On"))
        self.Valve3Off.setText(_translate("DebugWindow", "Off"))
        self.Valve4On.setText(_translate("DebugWindow", "On"))
        self.Valve3On.setText(_translate("DebugWindow", "On"))
        self.Valve5Off.setText(_translate("DebugWindow", "Off"))
        self.Valve5On.setText(_translate("DebugWindow", "On"))
        self.Valve4Off.setText(_translate("DebugWindow", "Off"))
        self.label_1.setText(_translate("DebugWindow", "Valve 1"))
        self.label_2.setText(_translate("DebugWindow", "Valve 2"))
        self.label_3.setText(_translate("DebugWindow", "Valve 3"))
        self.label_4.setText(_translate("DebugWindow", "Valve 4"))
        self.label_5.setText(_translate("DebugWindow", "Valve 5"))
        self.Valve2Off.setText(_translate("DebugWindow", "Off"))
        self.Valve1On.setText(_translate("DebugWindow", "On"))
        self.Valve1Off.setText(_translate("DebugWindow", "Off"))
        self.Pneumatics_label.setText(_translate("DebugWindow", "Pneumatics"))
        self.Ball1OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.Ball3OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BV1lbl.setText(_translate("DebugWindow", "Inflate 1"))
        self.Ball1OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball2OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BV4lbl.setText(_translate("DebugWindow", "Inflate 4"))
        self.BV3lbl.setText(_translate("DebugWindow", "Inflate 3"))
        self.Ball2OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball4OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball3OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.BV2lbl.setText(_translate("DebugWindow", "Inflate 2"))
        self.Ball4OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BVallPause.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_2.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_3.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_4.setText(_translate("DebugWindow", "Pause"))
        self.Ball_valve_label.setText(_translate("DebugWindow", "Ball Valves"))
        self.Motor3_rev.setText(_translate("DebugWindow", "Reverse"))
        self.Motor2_label.setText(_translate("DebugWindow", "Motor 2"))
        self.Motor3_label.setText(_translate("DebugWindow", "Motor 3"))
        self.Motor2_rev.setText(_translate("DebugWindow", "Reverse"))
        self.send_speed1.setText(_translate("DebugWindow", "Ok"))
        self.Motor2_fwd.setText(_translate("DebugWindow", "Forward"))
        self.Motor1_label.setText(_translate("DebugWindow", "Motor 1"))
        self.Motor3_fwd.setText(_translate("DebugWindow", "Forward"))
        self.send_speed3.setText(_translate("DebugWindow", "Ok"))
        self.Motor1_fwd.setText(_translate("DebugWindow", "Forward"))
        self.Motor1_rev.setText(_translate("DebugWindow", "Reverse"))
        self.send_speed2.setText(_translate("DebugWindow", "Ok"))
        self.Motor1Off.setText(_translate("DebugWindow", "Off"))
        self.Motor2Off.setText(_translate("DebugWindow", "Off"))
        self.Motor3Off.setText(_translate("DebugWindow", "Off"))
        self.Motor_label.setText(_translate("DebugWindow", "Motors"))
        self.MotorSpeedlbl.setText(_translate("DebugWindow", "Speed"))
        self.Ball5OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.Ball7OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BV5lbl.setText(_translate("DebugWindow", "Exhaust 1"))
        self.Ball5OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball6OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BV8lbl.setText(_translate("DebugWindow", "Exhaust 4"))
        self.BV7lbl.setText(_translate("DebugWindow", "Exhaust 3"))
        self.Ball6OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball8OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.Ball7OnRbtn.setText(_translate("DebugWindow", "Open"))
        self.BV6lbl.setText(_translate("DebugWindow", "Exhaust 2"))
        self.Ball8OffRbtn.setText(_translate("DebugWindow", "Close"))
        self.BVallPause_5.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_6.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_7.setText(_translate("DebugWindow", "Pause"))
        self.BVallPause_8.setText(_translate("DebugWindow", "Pause"))
        self.Ball_valve_label_2.setText(_translate("DebugWindow", "Ball Valves"))
        self.closeAll.setText(_translate("DebugWindow", "Close All "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DebugWindow = QtWidgets.QMainWindow()
    ui = Ui_DebugWindow()
    ui.setupUi(DebugWindow)
    DebugWindow.show()
    sys.exit(app.exec())
