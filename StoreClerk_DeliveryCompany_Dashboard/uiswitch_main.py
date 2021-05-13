import sys
import os
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


from uiswitch import Ui_MainWindow
from clerk_main import clerk_main

class uiswitch_main:
    def __init__(self):
        self.filepath = os.getcwd()
        self.selectedOrderno, self.selectedCustomerno, self.selectedProductno = 0,0,0
        self.main_win = QMainWindow() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.clerk_win = clerk_main()

        self.ui.clerk_button.clicked.connect(self.show_clerk_ui)

    def show_clerk_ui(self):
        self.main_win.close()
        self.clerk_win.show()

    def show(self):
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = uiswitch_main()
    main_win.show()
    sys.exit(app.exec_()) 
