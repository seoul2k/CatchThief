# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AI_Choice.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AI_Choice(object):
    def setupUi(self, AI_Choice):
        AI_Choice.setObjectName("AI_Choice")
        AI_Choice.resize(453, 598)
        AI_Choice.setStyleSheet("border-radius:10px;\n"
"\"\n"
"\"border:2px solid #252121;\n"
"\"\n"
"\"background-color:#464242;\n"
"\"\n"
"\"color:#CFFEAE;")
        self.label = QtWidgets.QLabel(AI_Choice)
        self.label.setGeometry(QtCore.QRect(120, 50, 211, 101))
        font = QtGui.QFont()
        font.setFamily("FZQingKeBenYueSongS-R-GB")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AI_Choice)
        self.label_2.setGeometry(QtCore.QRect(50, 210, 91, 41))
        font = QtGui.QFont()
        font.setFamily("FZQingKeBenYueSongS-R-GB")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Police = QtWidgets.QPushButton(AI_Choice)
        self.Police.setGeometry(QtCore.QRect(100, 300, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Police.setFont(font)
        self.Police.setStyleSheet("border-radius:10px;\n"
"border:2px solid #252121;\n"
"background-color:#464242;\n"
"color:#CFFEAE;")
        self.Police.setObjectName("Police")
        self.Thief = QtWidgets.QPushButton(AI_Choice)
        self.Thief.setGeometry(QtCore.QRect(100, 440, 281, 51))
        font = QtGui.QFont()
        font.setFamily("FZQingKeBenYueSongS-R-GB")
        font.setPointSize(18)
        self.Thief.setFont(font)
        self.Thief.setStyleSheet("border-radius:10px;\n"
"border:2px solid #252121;\n"
"background-color:#464242;\n"
"color:#CFFEAE;")
        self.Thief.setObjectName("Thief")
        self.back = QtWidgets.QPushButton(AI_Choice)
        self.back.setGeometry(QtCore.QRect(390, 10, 41, 41))
        self.back.setStyleSheet("border-radius:5px;\n"
"border:1px solid #000000;\n"
"background-color:#9DA5AC;")
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/back/fanhui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setObjectName("back")

        self.retranslateUi(AI_Choice)
        QtCore.QMetaObject.connectSlotsByName(AI_Choice)

    def retranslateUi(self, AI_Choice):
        _translate = QtCore.QCoreApplication.translate
        AI_Choice.setWindowTitle(_translate("AI_Choice", "Form"))
        self.label.setText(_translate("AI_Choice", "人机对战"))
        self.label_2.setText(_translate("AI_Choice", "你是："))
        self.Police.setText(_translate("AI_Choice", "警察"))
        self.Thief.setText(_translate("AI_Choice", "小偷"))
import fanhui
