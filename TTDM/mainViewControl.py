#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: ViewControl.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-05 13:31:10
# Last Modified: 2018-02-06 09:18:18
#***********************************************

import sys
import time

from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import mainView
from DataModel.labelinfo import *
from SQLData.sqlHelper import *

class MyWindow(QtWidgets.QMainWindow,mainView.Ui_MainWindow,QtWidgets.QTableWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(
            self
        )

    def GetYZM(self):
        ticks = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        PTtext = self.PruductType.text()
        self.PruductType.setText("XXXXXXXXXXXXXX")
        self.DataTime.setText(ticks)
        print("Get YZM ~~")
        print(PTtext)

    def SaveData(self):
        print("Save Data ~~")
        ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        row_count = self.Datalist.rowCount()
        self.Datalist.insertRow(row_count)

        newItem = QTableWidgetItem("1")
        self.Datalist.setItem(row_count,0,newItem)

        newItem = QTableWidgetItem(ticks)
        self.Datalist.setItem(row_count, 1, newItem)

        newItem = QTableWidgetItem("1")
        self.Datalist.setItem(row_count, 2, newItem)

        newItem = QTableWidgetItem("1")
        self.Datalist.setItem(row_count, 3, newItem)

        newItem = QTableWidgetItem("1")
        self.Datalist.setItem(row_count, 4, newItem)

    def AddSNFile(self):
        print("Add SN File ~~")
        lable = labelInfo()
        lable.SN = "4"
        print(lable.SN)

    def GetYZMAll(self):
        print("Get YZM All ~~")
        sql = sqlHelper()
        sql.sqlHelper_test()


    def SaveDataAll(self):
        print("Save Data All ~~")

    def clicked(self, QModelIndex):
        print("QModelIndex->",QModelIndex)
