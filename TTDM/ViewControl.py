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

import mainView

class MyWindow(QtWidgets.QMainWindow,mainView.Ui_MainWindow):
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
        self.Datalist

    def SaveData(self):
        print("Save Data ~~")

    def AddSNFile(self):
        print("Add SN File ~~")

    def GetYZMAll(self):
        print("Get YZM All ~~")

    def SaveDataAll(self):
        print("Save Data All ~~")
