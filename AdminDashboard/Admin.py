import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
# from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QLabel, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QPixmap
from pathlib import Path
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import shutil
import fileinput


import os.path

class UI_Admin (QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR,"AdminDashboard.ui")

    def __init__(self):
        super(UI_Admin,self).__init__()
        uic.loadUi(self.UI_FILE,self)

class Admin():

    def __init__(self):
        self.ui = UI_Admin()

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = Admin()
        window.ui.show()

        sys.exit(app.exec_())