import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, \
    QMessageBox

from qtwidgets import PasswordEdit

from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont, QIcon

font = QFont("Times", 12)

from PyQt5.QtWidgets import QMainWindow

from loginRegister import Ui_Login


class UserLogIn:
    def __init__(self):
        super(UserLogIn, self).__init__()
        self.filepath = os.getcwd()  # give filepath
        self.main_win = QMainWindow()
        self.ui = Ui_Login()
        self.ui.setupUi(self.main_win)

        """ Hide Password"""
        # password1 = self.ui.CustomerLoginPassword_lineEdit()
        # password1 = PasswordEdit(show_visibility=False)


        """registration main page"""
        # continue without login button
        # self.ui.notLoginPage_pushButton.clicked.connect(self.goToHomePage)

        self.ui.comboBoxUsers.activated.connect(lambda: self.selectComboBox)

        # Login main button
        self.ui.LoginPage_pushButton.clicked.connect(self.loginStackAccess)
        self.ui.RegisterPage_pushButton.clicked.connect(self.registerStackAccess)

        # continue button from comboOptionPage
        self.ui.ContinuepushButton.clicked.connect(self.customerStackRegistration1)
        self.ui.customerContinueRegister_pushButton.clicked.connect(self.customerStackRegistration2)

        # back button
        self.ui.RegisterBack_pushButton.clicked.connect(self.registerBackButton)
        self.ui.RegisterBack_pushButton_2.clicked.connect(self.registerBackButton)

        # This bottom takes the user to first page of customer registration
        self.ui.RegisterBack_pushButton_3.clicked.connect(self.customerStackRegistration1)

        self.ui.RegisterBack_pushButton_4.clicked.connect(self.registerBackButton)
        self.ui.RegisterBack_pushButton_5.clicked.connect(self.registerBackButton)

        # Superuser register button
        self.ui.superUserRegister_pushButton.clicked.connect(self.loginStackAccess)

        # Customer register continue button
        self.ui.customerRegister_pushButton.clicked.connect(self.registrationCustomer)

        # User login button --> redirect this to go to home page
        self.ui.customerLogin_pushButton.clicked.connect(self.customerLogin)
        self.main_win.show()

    def selectComboBox(self, i):

        # print("item available are here: ")
        # self.ui.stackedWidget.setCurrentWidget(self.ui.comboBoxOptionsPage)
        # for count in range(self.comboBoxUsers.count()):
        #     print(self.comboBoxUsers.itemText(count))
        # print("Current index", i, "selection changed ", self.ui.comboBoxUsers.currentText())
        pass




    def loginStackAccess(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    def comboStackAccess(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.comboBoxOptionsPage)

    # this function should print the completion of registration if information is correct
    def registrationCustomer(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.customerCardInfopage)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Registration Completed! Do you want to login?")
        msgBox.setWindowTitle("Registration Page")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

        elif returnValue == QMessageBox.No:
            self.ui.stackedWidget.setCurrentWidget(self.ui.LoginRegisterPage)

    # def loginStackAccess(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    def registerStackAccess(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.comboBoxOptionsPage)

    """ Customer Register StackWidget """

    def customerStackRegistration1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.customerRegisterPage)

    def customerStackRegistration2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.customerCardInfopage)

    def registerBackButton(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginRegisterPage)

    def mainRegistrationPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginRegisterPage)

    # will take user to login page after registration
    # def registerToLogin(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # Super User Registration
    def superUserRegister(self):
        # needs authentication here
        super_user_email = self.ui.SuperUserEmail_lineEdit.text()
        # make sure that both passwords are the same
        super_user_password = self.ui.SuperUserPassword_lineEdit.text()
        super_user_confirm_password = self.ui.SuperUserConfirmPassword_lineEdit.text()

        super_user_access_code = self.ui.SuperUserAccessCode_lineEdit.text()

        print("Successfully registered with", super_user_email)
        print("Password: ", super_user_password)
        print("Confirm Password: ", super_user_confirm_password)
        print("Access code: ", super_user_access_code)
        # check for correct values

        if super_user_email != "yasirisortiz24@gmail.com" and self.ui.superUserRegister_pushButton == self.ui.superUserRegister_pushButton.clicked():
            print("This is an invalid user")

    # Customer Registration
    def customerRegister(self):
        customer_email = self.ui.customerEmail_lineEdit.text()
        customer_password = self.ui.CustomerPassword_lineEdit.text()
        customer_confirm_password = self.ui.CustomerConfirmPassword_lineEdit.text()
        customer_card_name = self.ui.customerNameOnCard_lineEdit.text()
        customer_card_number = self.ui.customerCardNumber_lineEdit.text()
        customer_security_code = self.ui.customerCardSCode_lineEdit.text()
        customer_zip_code = self.ui.zipCode_lineEdit.text()

        # array to append/register data to text file
        userInfo = [customer_email, customer_password, customer_confirm_password, customer_card_name,
                    customer_card_number, customer_security_code, customer_zip_code]

        # save this information in the customerRegister.txt file
        with open("customerRegister.txt", "a+") as fileObject:
            appendEOL = False
            fileObject.seek(0)
            # Check if file is not empty
            data = fileObject.read(100)
            if len(data) > 0:
                appendEOL = True
            for line in userInfo:
                if appendEOL:
                    fileObject.write("\n")
                else:
                    appendEOL = True
                    # Append element at the end of file
                fileObject.write(line)
        print()

    def customerLogin(self):

        # If login is clicked without any information, then
        # print out QMessage (with a warning)

        user_email = self.ui.customerLoginEmail_lineEdit.text()
        user_password = self.ui.CustomerLoginPassword_lineEdit.text()



        # read from one of the login text files
        try:
            allUsersData = []
            with open("customerLogin.txt", "r") as myFile:
                lines = myFile.readlines()
                allUsersData.append(lines)
                for i in range(len(allUsersData[0])):
                    allUsersData[0][i] = allUsersData[0][i].replace('\n', '')
                print(allUsersData)
                # if user_email == user and user_password == password:
                #     print("User: ", user_email + " is a valid user")
                # else:
                #     print("this is wrong user")

                # # first check if the email and password are registered, if not them print box message
                # found = False
                # for line in myFile:
                #     if user_email in myFile and user_password in myFile:
                #         print("Account Found")
                #         found = True
                # if not found:
                #     mbox = QMessageBox.question(self, "This account does not exist", "Do you want to create an account?", QMessageBox.Yes | QMessageBox.No)

                # compare if the entered email and password are registered
            myFile.close()
        except:
            print('Cannot proceed, something went wrong')

    # def superUserLogin(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = UserLogIn()
    sys.exit(app.exec_())
