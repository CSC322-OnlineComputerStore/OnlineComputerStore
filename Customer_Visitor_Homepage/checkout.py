import sys
from decimal import Decimal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

import CardChecking
#from checkoutPages import Ui_HomepageV2
from checkoutPages2 import Ui_HomepageV2
from CardChecking import purchase


class PurchasePage:
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_HomepageV2()
        self.ui.setupUi(self.main_window)
        self.ui.WrongInfo.setHidden(True)
        self.ui.pushButton.clicked.connect(lambda: self.confirm_pressed())

        # self.ui.pushButton.clicked.connect(lambda: self.take_all_user_inputs())

        self.name = None
        self.address = None
        self.city = None
        self.zip = None
        self.state = None

        self.cardNumber = None
        #self.cardCode = None
        self.cardCode = None
        self.nameOnCard = None
        self.expMonth = None
        self.expYear = None
        self.expDate = None

        self.card = None

        self.result = False
        self.total = Decimal("5.00")

    def confirm_pressed(self):
        self.ui.pushButton.clicked.connect(lambda: self.take_all_user_inputs())

        #self.result = True
        #self.result = False
        #self.wrong_info()
        if self.result:
            # If the card is approved then the customer can move forward to the confirmation page
            # else they need to re-enter their info
            print(self.result)
            self.ui.pushButton.clicked.connect(lambda: self.go_to_confirmation_page())
        else:
            print(self.result)
            self.wrong_info()
            self.ui.WrongInfo.setHidden(False)

    def go_to_confirmation_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.purchaseconfirmationpage)

    def wrong_info(self):
        self.clear_card_input()
        self.clear_code_input()
        self.clear_exp_date_input()

    def clear_card_input(self):
        self.ui.lineEdit_2.setText("")

    def clear_exp_date_input(self):
        self.ui.Year.setText("")
        self.ui.Month.setText("")

    def clear_code_input(self):
        self.ui.CVCinput.setText("")

    def set_total(self):
        # ToDo: Totol is going to be determined by the shopping cart page so this should get the total from there
        self.total = "50.00"

    def make_exp_date(self, month_number, year):
        # Need this function to put the expiration date in the form that the payment processing can handle
        self.expDate = (year + "-" + month_number)
        print(self.expDate)

    def get_exp_month(self):
        self.expMonth = self.ui.Month.text()
        print(self.expMonth)

    def get_expYear(self):
        self.expYear = self.ui.Year.text()
        print(self.expYear)

    def read_input_userName(self):
        # self.ui.lineEdit.setText("Enter your name")
        #ToDo: Decide if these should also set the self values or if that should be handled seperately somewhere else
        # Don't think I'll have them return anything, only update the values in self
        self.name = self.ui.lineEdit.text()
        print(self.name)
        # return self.ui.lineEdit.text()

    def read_input_address(self):
        # self.ui.lineEdit_7.setText("Address")
        self.address = self.ui.lineEdit_7.text()
        print(self.address)
        # return self.ui.lineEdit_7.text()

    def read_input_city(self):
        self.city = self.ui.lineEdit_8.text()
        print(self.city)
        # return self.ui.lineEdit_8.text()

    def read_input_zip(self):
        self.zip = self.ui.lineEdit_9.text()
        print(self.zip)
        # return self.ui.lineEdit_9.text()

    def read_input_state(self):
        self.state = self.ui.lineEdit_10.text()
        print(self.state)
        # return self.ui.lineEdit_10.text()

    def read_input_card_number(self):
        self.cardNumber = str(self.ui.lineEdit_2.text())
        print(self.cardNumber)
        # return self.ui.lineEdit_2.text()

    def read_input_card_code(self):
        self.cardCode = str(self.ui.CVCinput.text())
        print(self.cardCode)

    def read_name_on_card(self):
        self.nameOnCard = str(self.ui.lineEdit_4.text())
        print(self.nameOnCard)
        # return self.ui.lineEdit_4.text()

    def take_all_user_inputs(self):
        # This function is here to take all the input at once when the submit button is pressed
        self.read_input_userName()
        self.read_input_address()
        self.read_input_city()
        self.read_input_zip()
        self.read_input_state()
        self.read_input_card_number()
        self.get_exp_month()
        self.get_expYear()
        self.read_input_card_code()

    def create_user_card(self):
        #CardChecking.CreditCard.__init__(self.cardNumber, self.expDate, self.cardCode, "987")
        #new_card = CardChecking.CreditCard
        #new_card.setNumber(new_card, "4007000000027")
        #new_card.setExpDate(new_card, "2050-01")
        #new_card.setCode(new_card, "123")
        #self.card = new_card
        #self.card.showInfo(self.card)
        new_card = CardChecking.CreditCard
        new_card.setNumber(new_card, self.cardNumber)
        new_card.setExpDate(new_card, self.expDate)
        new_card.setCode(new_card, self.cardCode)
        self.card = new_card
        self.card.showInfo(self.card)


    def use_user_card(self):
        response = CardChecking.purchase(self.card, "50.00")
        self.result = response.success
        print("Approval:" + str(response.success))

    def get_user_info(self, textFilePath):
        file = open(textFilePath, "r")
        # ToDo: fill this part in when the details of file management for the system is made
        # read the user info from wherever and however we store it
        file.close()


    def confirm_button_pressed(self):
        # When confirm is pressed the card check is done
        # and the info is stored to be displayed on the next page if the credit part is succesful
        #CardChecking.purchase()
        self.create_user_card()
        self.use_user_card()


    def show(self):
        self.main_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = PurchasePage()
    page.show()
    #print(page.read_input_userName())
    #page.confirm_button_pressed()
    #page.confirm_pressed()
    #page.create_user_card()
    #page.use_user_card()

    sys.exit(app.exec_())