# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1049, 831)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.exerciseList = QListWidget(self.centralwidget)
        self.exerciseList.setObjectName(u"exerciseList")

        self.horizontalLayout_7.addWidget(self.exerciseList)

        self.gymList = QListWidget(self.centralwidget)
        self.gymList.setObjectName(u"gymList")

        self.horizontalLayout_7.addWidget(self.gymList)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.clientList = QListWidget(self.centralwidget)
        self.clientList.setObjectName(u"clientList")

        self.horizontalLayout_9.addWidget(self.clientList)

        self.trainerList = QListWidget(self.centralwidget)
        self.trainerList.setObjectName(u"trainerList")

        self.horizontalLayout_9.addWidget(self.trainerList)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.time = QSpinBox(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.time)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.distance = QSpinBox(self.centralwidget)
        self.distance.setObjectName(u"distance")
        self.distance.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_3.addWidget(self.distance)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.repetitionsNumber = QSpinBox(self.centralwidget)
        self.repetitionsNumber.setObjectName(u"repetitionsNumber")
        self.repetitionsNumber.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_2.addWidget(self.repetitionsNumber)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.weight = QSpinBox(self.centralwidget)
        self.weight.setObjectName(u"weight")
        self.weight.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_4.addWidget(self.weight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.calories = QSpinBox(self.centralwidget)
        self.calories.setObjectName(u"calories")
        self.calories.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_6.addWidget(self.calories)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.hight = QSpinBox(self.centralwidget)
        self.hight.setObjectName(u"hight")
        self.hight.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_5.addWidget(self.hight)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1049, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Czas trwania<br/>w s:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Dystans<br/>w m:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Liczba powt\u00f3rze\u0144:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Obci\u0105\u017cenie<br/>w kg:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Kalorie:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Wysoko\u015b\u0107<br/>w cm:</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Prze\u015blij dane do bazy", None))
    # retranslateUi

