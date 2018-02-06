#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: main.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-02 15:41:46
# Last Modified: 2018-02-06 09:18:41
#***********************************************

import sys
import mainView
import ViewControl

from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = ViewControl.MyWindow()
    # ui = mainView.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
