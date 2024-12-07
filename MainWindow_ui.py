# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
        MainWindow.resize(411, 496)
        font = QFont()
        font.setFamily(u"SimSong")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background:#BDBDBD;")
        self.SingerPlayer = QPushButton(MainWindow)
        self.SingerPlayer.setObjectName(u"SingerPlayer")
        self.SingerPlayer.setEnabled(True)
        self.SingerPlayer.setGeometry(QRect(50, 250, 311, 51))
        font1 = QFont()
        font1.setFamily(u"FZQingKeBenYueSongS-R-GB")
        self.SingerPlayer.setFont(font1)
        self.SingerPlayer.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid #252121;\n"
"background-color:#464242;\n"
"color:#CFFEAE;")
        self.SingerPlayer.setCheckable(False)
        self.AI = QPushButton(MainWindow)
        self.AI.setObjectName(u"AI")
        self.AI.setGeometry(QRect(50, 350, 311, 51))
        self.AI.setFont(font1)
        self.AI.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid #252121;\n"
"background-color:#464242;\n"
"color:#CFFEAE;")
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 100, 251, 81))
        font2 = QFont()
        font2.setFamily(u"FZQingKeBenYueSongS-R-GB")
        font2.setPointSize(48)
        self.label.setFont(font2)
        self.RuleButton = QPushButton(MainWindow)
        self.RuleButton.setObjectName(u"RuleButton")
        self.RuleButton.setGeometry(QRect(20, 20, 31, 31))
        font3 = QFont()
        font3.setFamily(u"FZQingKeBenYueSongS-R-GB")
        font3.setPointSize(14)
        self.RuleButton.setFont(font3)
        self.RuleButton.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid #252121;\n"
"background-color:#464242;\n"
"color:#CFFEAE;")

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8b66\u5bdf\u6293\u5c0f\u5077", None))
        self.SingerPlayer.setText(QCoreApplication.translate("MainWindow", u"\u5355\u673a\u6e38\u620f", None))
        self.AI.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u673a\u5bf9\u6218", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8b66\u5bdf\u6293\u5c0f\u5077", None))
        self.RuleButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

