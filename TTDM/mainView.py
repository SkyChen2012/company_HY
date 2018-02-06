# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PruductType = QtWidgets.QLineEdit(self.centralwidget)
        self.PruductType.setEnabled(True)
        self.PruductType.setGeometry(QtCore.QRect(140, 30, 171, 21))
        self.PruductType.setObjectName("PruductType")
        self.DataTime = QtWidgets.QLineEdit(self.centralwidget)
        self.DataTime.setGeometry(QtCore.QRect(420, 30, 161, 21))
        self.DataTime.setObjectName("DataTime")
        self.SN = QtWidgets.QLineEdit(self.centralwidget)
        self.SN.setGeometry(QtCore.QRect(140, 60, 171, 21))
        self.SN.setObjectName("SN")
        self.YZM = QtWidgets.QLineEdit(self.centralwidget)
        self.YZM.setGeometry(QtCore.QRect(420, 60, 161, 21))
        self.YZM.setObjectName("YZM")
        self.Datalist = QtWidgets.QTableWidget(self.centralwidget)
        self.Datalist.setGeometry(QtCore.QRect(10, 100, 601, 391))
        self.Datalist.setObjectName("Datalist")
        self.Datalist.setColumnCount(6)
        self.Datalist.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Datalist.setHorizontalHeaderItem(5, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 60, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 30, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 60, 60, 16))
        self.label_4.setObjectName("label_4")
        self.getYZM = QtWidgets.QPushButton(self.centralwidget)
        self.getYZM.setGeometry(QtCore.QRect(630, 30, 113, 32))
        self.getYZM.setObjectName("getYZM")
        self.saveData = QtWidgets.QPushButton(self.centralwidget)
        self.saveData.setGeometry(QtCore.QRect(630, 60, 113, 32))
        self.saveData.setObjectName("saveData")
        self.addSNFile = QtWidgets.QPushButton(self.centralwidget)
        self.addSNFile.setGeometry(QtCore.QRect(630, 110, 113, 32))
        self.addSNFile.setObjectName("addSNFile")
        self.getYZMAll = QtWidgets.QPushButton(self.centralwidget)
        self.getYZMAll.setGeometry(QtCore.QRect(630, 150, 113, 32))
        self.getYZMAll.setObjectName("getYZMAll")
        self.saveDataAll = QtWidgets.QPushButton(self.centralwidget)
        self.saveDataAll.setGeometry(QtCore.QRect(630, 190, 113, 32))
        self.saveDataAll.setObjectName("saveDataAll")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.saveData.clicked.connect(MainWindow.SaveData)
        self.getYZM.clicked.connect(MainWindow.GetYZM)
        self.addSNFile.clicked.connect(MainWindow.AddSNFile)
        self.getYZMAll.clicked.connect(MainWindow.GetYZMAll)
        self.saveDataAll.clicked.connect(MainWindow.SaveDataAll)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PruductType.setText(_translate("MainWindow", "Product typt"))
        self.DataTime.setText(_translate("MainWindow", "datatime "))
        self.SN.setText(_translate("MainWindow", "SN"))
        self.YZM.setText(_translate("MainWindow", "验证码"))
        item = self.Datalist.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序列号"))
        item = self.Datalist.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "产品型号"))
        item = self.Datalist.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "时间"))
        item = self.Datalist.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "SN"))
        item = self.Datalist.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "验证码"))
        item = self.Datalist.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "存档"))
        self.label.setText(_translate("MainWindow", "产品型号"))
        self.label_3.setText(_translate("MainWindow", "SN码"))
        self.label_2.setText(_translate("MainWindow", "时间"))
        self.label_4.setText(_translate("MainWindow", "验证码"))
        self.getYZM.setText(_translate("MainWindow", "获取验证码"))
        self.saveData.setText(_translate("MainWindow", "存档"))
        self.addSNFile.setText(_translate("MainWindow", "批量添加SN"))
        self.getYZMAll.setText(_translate("MainWindow", "批量获取验证码"))
        self.saveDataAll.setText(_translate("MainWindow", "批量存储"))

