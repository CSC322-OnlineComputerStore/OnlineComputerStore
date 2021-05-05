import sys
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QScrollArea
from PyQt5.QtWidgets import QMainWindow

from shopPage import Ui_Homepage


class search_test:
    def __init__(self):
        self.filepath = os.getcwd()  # give filepath
        self.retrieveText = ""
        self.main_win = QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.main_win)
        self.abc = self.filepath + "/productList.txt"

        self.ui.StackedWidget.setCurrentWidget(self.ui.shopPage)  # current is the shopPage now

        self.ui.searchButton.clicked.connect(self.set_abc)  # connect search to filter function

        # home button
        self.ui.HomeButton.clicked.connect(self.showHomepage)
        # shop button
        self.ui.ShopButton.clicked.connect(self.showShopStackedWidget)
        # cart Button
        self.ui.CartButton.clicked.connect(self.showCartPage)

        # add to cart push buttons by order
        self.ui.CartPushButton1.clicked.connect(self.showCartPage)  # how can i make this item to reflect in the cart?
        self.ui.CartPushButton2.clicked.connect(self.showCartPage)
        self.ui.CartPushButton3.clicked.connect(self.showCartPage)
        self.ui.CartPushButton4.clicked.connect(self.showCartPage)
        self.ui.CartPushButton5.clicked.connect(self.showCartPage)
        self.ui.CartPushButton6.clicked.connect(self.showCartPage)
        self.ui.CartPushButton7.clicked.connect(self.showCartPage)
        self.ui.CartPushButton8.clicked.connect(self.showCartPage)

        # product_names = ["Surface Windows", "Apple Mac OS", "HP Chrome", "Hard Disk", "CPU Core i7"]
        # for name in product_names:
        #     item = self.displayProduct(name)

        #  frames



    def show(self):
        self.main_win.show()

    def set_abc(self):
        self.get_product_list(self.abc)

    def get_product_list(self, filename):
        lst = []
        with open(filename, "r") as myfile:
            lines = myfile.readlines()
            lst.append(lines)
        for i in range(len(lst[0])):
            lst[0][i] = lst[0][i].replace('\n', '')
        self.retrieveText = self.ui.searchLineEdit.text()

        # for i in range(len(l[0])):
        #     if (l[0][i] == self.retrieveText):
        #         self.ui.display_message.setText("Found Item")
        #         break;
        #     else:
        #         self.ui.display_message.setText("Item not found")

    # Changing pages on UI
    def showShopStackedWidget(self):
        self.ui.StackedWidget.setCurrentWidget(self.ui.shopPage)

    def showCartPage(self):
        self.ui.StackedWidget.setCurrentWidget(self.ui.cartpage)

    def showHomepage(self):
        self.ui.StackedWidget.setCurrentWidget(self.ui.profilepage)

    def displayProduct(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = search_test()
    main_win.show()
    sys.exit(app.exec_())
