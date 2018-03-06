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
from PyQt5.QtWidgets import *

import mainView
from DataModel.labelinfo import *
from SQLData.sqlHelper import *
from XXNet.channel.xxClient import *
from Config.config import *
from Tools import JsonTool

class MyWindow(QtWidgets.QMainWindow,mainView.Ui_MainWindow,QtWidgets.QTableWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

    def GetYZM(self):
        ticks = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        PTtext = self.PruductType.text()
        self.PruductType.setText("XXXXXXXXXXXXXX")
        self.DataTime.setText(ticks)
        print("Get YZM ~~")
        Client = XXClient("Client");
        Client.test()
        config = Config();
        print(config.GetUrl())
        postdata = chr(2)+'{"Command":"Dispatch","FrameNumber":"00","Type":"DevList","Data":[{"DeviceId":"0000000000000000","Key":"deviceList"}]}' +chr(3)
        # arr = []
        # for t in postdata:
        #     arr.append(ord(t))
        # print(arr)
        # postdatasend = ''.join(str(hex(i)) for i in arr)
        # r = Client.post(config.GetUrl(),postdata)
        r = Client.TCP(postdata)
        # print(r.text)

        # JsonTool.JsonToPythonDir(r.text)
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
        results  = sql.sqlHelper_test()
        for row in results:
            sData = row[0] + row[1] + row[2]
            self.ShowData.setText(sData);
            print (row[0],row[1],row[2])

    def SaveDataAll(self):
        print("Save Data All ~~")
        sql = sqlHelper()
        results = sql.Query_Database()
        for row in results:
            print(row[0], row[1], row[2])
            row_count = self.Datalist.rowCount()
            self.Datalist.insertRow(row_count)

            newItem = QTableWidgetItem(row[0])
            self.Datalist.setItem(row_count, 0, newItem)

            newItem = QTableWidgetItem(row[1])
            self.Datalist.setItem(row_count, 1, newItem)

            newItem = QTableWidgetItem(row[2])
            self.Datalist.setItem(row_count, 2, newItem)

            newItem = QTableWidgetItem(row[3])
            self.Datalist.setItem(row_count, 3, newItem)

            newItem = QTableWidgetItem(row[4])
            self.Datalist.setItem(row_count, 4, newItem)


    def clicked(self, QModelIndex):
        print("QModelIndex->",QModelIndex)
