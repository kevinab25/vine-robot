# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MainWidget = QWidget(self.centralwidget)
        self.MainWidget.setObjectName(u"MainWidget")
        self.MainWidget.setGeometry(QRect(50, 340, 701, 251))
        self.MainWidget.setMouseTracking(True)
        self.Sensor_lbl = QLabel(self.MainWidget)
        self.Sensor_lbl.setObjectName(u"Sensor_lbl")
        self.Sensor_lbl.setGeometry(QRect(10, 20, 81, 21))
        self.horizontalLayoutWidget = QWidget(self.MainWidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 70, 351, 161))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.temp_label = QLineEdit(self.horizontalLayoutWidget)
        self.temp_label.setObjectName(u"temp_label")
        self.temp_label.setAutoFillBackground(False)
        self.temp_label.setReadOnly(True)

        self.verticalLayout.addWidget(self.temp_label)

        self.humidity_label = QLineEdit(self.horizontalLayoutWidget)
        self.humidity_label.setObjectName(u"humidity_label")
        self.humidity_label.setReadOnly(True)

        self.verticalLayout.addWidget(self.humidity_label)

        self.speed_label = QLineEdit(self.horizontalLayoutWidget)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setReadOnly(True)

        self.verticalLayout.addWidget(self.speed_label)

        self.pressure_label = QLineEdit(self.horizontalLayoutWidget)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setReadOnly(True)

        self.verticalLayout.addWidget(self.pressure_label)

        self.orientation_label = QLineEdit(self.horizontalLayoutWidget)
        self.orientation_label.setObjectName(u"orientation_label")
        self.orientation_label.setReadOnly(True)

        self.verticalLayout.addWidget(self.orientation_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.temp_val_rvcd = QLineEdit(self.horizontalLayoutWidget)
        self.temp_val_rvcd.setObjectName(u"temp_val_rvcd")

        self.verticalLayout_2.addWidget(self.temp_val_rvcd)

        self.humidity_val_rcvd = QLineEdit(self.horizontalLayoutWidget)
        self.humidity_val_rcvd.setObjectName(u"humidity_val_rcvd")

        self.verticalLayout_2.addWidget(self.humidity_val_rcvd)

        self.speed_val_rcvd = QLineEdit(self.horizontalLayoutWidget)
        self.speed_val_rcvd.setObjectName(u"speed_val_rcvd")

        self.verticalLayout_2.addWidget(self.speed_val_rcvd)

        self.pressure_val_rcvd = QLineEdit(self.horizontalLayoutWidget)
        self.pressure_val_rcvd.setObjectName(u"pressure_val_rcvd")

        self.verticalLayout_2.addWidget(self.pressure_val_rcvd)

        self.orient_val_rcvd = QLineEdit(self.horizontalLayoutWidget)
        self.orient_val_rcvd.setObjectName(u"orient_val_rcvd")

        self.verticalLayout_2.addWidget(self.orient_val_rcvd)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayoutWidget_2 = QWidget(self.MainWidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(420, 40, 241, 56))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.obj_ident_label = QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_ident_label.setObjectName(u"obj_ident_label")
        self.obj_ident_label.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.obj_ident_label)

        self.obj_fwing_label = QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_fwing_label.setObjectName(u"obj_fwing_label")
        self.obj_fwing_label.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.obj_fwing_label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.obj_ident_val = QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_ident_val.setObjectName(u"obj_ident_val")

        self.verticalLayout_4.addWidget(self.obj_ident_val)

        self.obj_fwing_val = QLineEdit(self.horizontalLayoutWidget_2)
        self.obj_fwing_val.setObjectName(u"obj_fwing_val")

        self.verticalLayout_4.addWidget(self.obj_fwing_val)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.obj_lbl = QLabel(self.MainWidget)
        self.obj_lbl.setObjectName(u"obj_lbl")
        self.obj_lbl.setGeometry(QRect(420, 20, 58, 16))
        self.mode_group = QGroupBox(self.MainWidget)
        self.mode_group.setObjectName(u"mode_group")
        self.mode_group.setGeometry(QRect(420, 110, 241, 121))
        self.mode_group.setCheckable(False)
        self.auto_mode_radioBtn = QRadioButton(self.mode_group)
        self.auto_mode_radioBtn.setObjectName(u"auto_mode_radioBtn")
        self.auto_mode_radioBtn.setGeometry(QRect(20, 30, 171, 31))
        self.manual_mode_radioBtn = QRadioButton(self.mode_group)
        self.manual_mode_radioBtn.setObjectName(u"manual_mode_radioBtn")
        self.manual_mode_radioBtn.setGeometry(QRect(20, 70, 171, 31))
        self.metric_label = QLabel(self.MainWidget)
        self.metric_label.setObjectName(u"metric_label")
        self.metric_label.setGeometry(QRect(10, 50, 168, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.metric_label.sizePolicy().hasHeightForWidth())
        self.metric_label.setSizePolicy(sizePolicy)
        self.label_3 = QLabel(self.MainWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 50, 167, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Vine Robot", None))
        self.Sensor_lbl.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.temp_label.setText(QCoreApplication.translate("MainWindow", u"Temperature (C)", None))
        self.humidity_label.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.orientation_label.setText(QCoreApplication.translate("MainWindow", u"Orientation", None))
        self.obj_ident_label.setText(QCoreApplication.translate("MainWindow", u"Identified", None))
        self.obj_fwing_label.setText(QCoreApplication.translate("MainWindow", u"Following", None))
        self.obj_lbl.setText(QCoreApplication.translate("MainWindow", u"Object ", None))
        self.mode_group.setTitle(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.auto_mode_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Autonomous", None))
        self.manual_mode_radioBtn.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.metric_label.setText(QCoreApplication.translate("MainWindow", u"Metric", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Value", None))
    # retranslateUi

