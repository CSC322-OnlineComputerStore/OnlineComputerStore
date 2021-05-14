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

class UI_LoginRegister (QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR,"LoginRegister.ui")

    def __init__(self):
        super(UI_LoginRegister,self).__init__()
        uic.loadUi(self.UI_FILE,self)

class loginRegister():

    def __init__(self):
        self.ui = UI_LoginRegister()
        self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.LoginRegisterPage)
        
        self.ui.LoginPage_pushButton.clicked.connect(self.openUserTypeLoginPage)
        self.ui.RegisterPage_pushButton.clicked.connect(self.openUserTypeRegisterPage)

        self.ui.ContinueRegister_pushButton.clicked.connect(lambda: self.openRegisterPage(self.ui.UsersRegister_comboBox))
        self.ui.ContinueLogin_pushButton.clicked.connect(lambda: self.openLoginPage())

        # Super User Register
        self.ui.superUserRegister_pushButton.clicked.connect(lambda: self.registerSuperUser(self.ui.UsersRegister_comboBox))

        # Customer Register
        self.ui.ContinueRegister_pushButton.clicked.connect(lambda: self.registerCustomer())

        # User Login
        self.ui.userLogin_pushButton.clicked.connect(lambda: self.loginUser(self.ui.UsersLogin_comboBox))

        # self.ui.customerLogin_pushButton.clicked.connect()
        self.ui.RegisterBack_pushButton_2.clicked.connect(lambda: self.openPage(self.ui.LoginRegisterPage))
        self.ui.RegisterBack_pushButton.clicked.connect(lambda: self.openPage(self.ui.LoginRegisterPage))
        self.ui.RegisterBack_pushButton_4.clicked.connect(lambda: self.openPage(self.ui.LoginRegisterPage))
    
    def openPage(self, page):
        try:
            self.ui.LoginRegister_stackedWidget.setCurrentWidget(page)
        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)

    def registerBackButton(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginRegisterPage)

    def openUserTypeLoginPage(self):
        self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.comboBoxLoginPage)

    def openUserTypeRegisterPage(self):
        self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.comboBoxRegisterPage)
        
    def openRegisterPage(self, comboxBox):
        comboxBoxUser = comboxBox.currentText()
        try:
            if(comboxBoxUser == "Customer"):
                self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.customerRegisterPage)

            elif(comboxBoxUser == "Store Clerk" or comboxBoxUser == "Manager" or comboxBoxUser == "Delivery Company"):
                self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.SuperUserRegisterPage)

        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)

    def openLoginPage(self):
        try:
            self.ui.LoginRegister_stackedWidget.setCurrentWidget(self.ui.LoginPage)
        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)

    def openVisitorPage(self):
        return None
    
    def openCustomerPage(self):
        return None

    def openManagerPage(self):
        return None

    def openStoreClerkPage(self):
        return None

    def openDeliveryPage(self):
        return None
    
    def registerSuperUser(self, comboxBox):
        try:
            comboxBoxUser = comboxBox.currentText()
            userEmail = self.ui.SuperUserEmail_lineEdit.text()
            userPass = self.ui.SuperUserPassword_lineEdit.text()
            userCPass = self.ui.SuperUserConfirmPassword_lineEdit.text()
            userAC = self.ui.SuperUserAccessCode_lineEdit.text()
            userId = ""
            allowLogin = False
            userFile = ""
            if(comboxBoxUser == "Store Clerk"):
                for line in fileinput.input("../Resources/Data/Login/storeClerks.txt", inplace=1):
                    if str(userAC) in line: 
                        allowLogin = True
                        userFile = "../Resources/Data/Login/storeClerks.txt"
                        userId = line.split(",")[1]
                    sys.stdout.write(line)

            elif(comboxBoxUser == "Manager"):
                for line in fileinput.input("../Resources/Data/Login/deliveryCompanies.txt", inplace=1):
                    if str(userAC) in line: 
                        allowLogin = True
                        userFile = "../Resources/Data/Login/deliveryCompanies.txt"
                        userId = line.split(",")[1]
                    sys.stdout.write(line)

            elif(comboxBoxUser == "Delivery Company"):
                for line in fileinput.input("../Resources/Data/manager.txt", inplace=1):
                    if str(userAC) in line: 
                        allowLogin = True
                        userFile = "../Resources/Data/Login/manager.txt"
                        userId = line.split(",")[1]
                    sys.stdout.write(line)

            else:
                print("No Access")

            userInfo = userAC + ", " + userId + ", " + userEmail + ", " + userPass

            if(userPass == userCPass and allowLogin == True):
                print("Succesfully Registered")
                with open(userFile, "a") as a_file:
                    a_file.write("\n")
                    a_file.write(userInfo)

            else:
                print("Confirm password and Password don't match")

        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)
        
    def registerCustomer(self):
        try: 
            userEmail = self.ui.customerEmail_lineEdit.text()
            userPass = self.ui.CustomerPassword_lineEdit.text()
            userCPass = self.ui.CustomerConfirmPassword_lineEdit.text()

            userId = "C0"
            userFile = "../Resources/Data/Login/customer.txt"

            userInfo = userId + ", " + userEmail + ", " + userPass

            if(userPass == userCPass):
                print("Succesfully Registered")
                with open(userFile, "a") as a_file:
                    a_file.write("\n")
                    a_file.write(userInfo)

            else:
                print("Confirm password and Password don't match")
        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)

    def loginUser(self, comboxBox):
        try:
            comboxBoxUser = comboxBox.currentText()
            userEmail = self.ui.userLoginEmail_lineEdit.text()
            userPass = self.ui.userLoginPassword_lineEdit.text()

            allowLogin = False

            if(comboxBoxUser == "Customer"):
                for line in fileinput.input("../Resources/Data/Login/customer.txt", inplace=1):
                    if str(userEmail) in line:
                        if str(userPass) in line: 
                            allowLogin = True
                    sys.stdout.write(line)

                if(allowLogin == True):
                    print("Login sucessfully")
                    self.openCustomerPage()
                else:
                    print("Email or password is wrong")

            elif(comboxBoxUser == "Store Clerk"):
                for line in fileinput.input("../Resources/Data/Login/storeClerks.txt", inplace=1):
                    if str(userEmail) in line:
                        if str(userPass) in line: 
                            allowLogin = True
                    sys.stdout.write(line)

                if(allowLogin == True):
                    print("Login sucessfully")
                    self.openStoreClerkPage()
                else:
                    print("Email or password is wrong")

            elif(comboxBoxUser == "Manager"):
                for line in fileinput.input("../Resources/Data/Login/deliveryCompanies.txt", inplace=1):
                    if str(userEmail) in line:
                        if str(userPass) in line: 
                            allowLogin = True
                    sys.stdout.write(line)

                if(allowLogin == True):
                    print("Login sucessfully")
                    self.openManagerPage()
                else:
                    print("Email or password is wrong")

            elif(comboxBoxUser == "Delivery Company"):
                for line in fileinput.input("../Resources/Data/manager.txt", inplace=1):
                    if str(userEmail) in line:
                        if str(userPass) in line: 
                            allowLogin = True
                    sys.stdout.write(line)

                if(allowLogin == True):
                    print("Login sucessfully")
                    self.openDeliveryPage()
                else:
                    print("Email or password is wrong")
        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = loginRegister()
        window.ui.show()

        sys.exit(app.exec_())