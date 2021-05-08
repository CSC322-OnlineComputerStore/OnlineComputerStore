import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap


import os.path

class UI_ManagerDashboard (QtWidgets.QMainWindow):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    UI_FILE = os.path.join(BASE_DIR,"ManagerDashboard.ui")

    def __init__(self):
        super(UI_ManagerDashboard,self).__init__()
        uic.loadUi(self.UI_FILE,self)

class manager():

    def __init__(self):
        self.ui = UI_ManagerDashboard()
        self.ui.MenuContent_stackedWidget.setCurrentWidget(self.ui.Products_Page)

        self.allStoreProducts = self.getAllProducts()

        self.OS_1 = "Windows";
        self.OS_2 = "macOS";
        self.OS_3 = "Chrome";
        self.OS_4 = "Linux";

        self.displayTopOS(self.OS_1, self.ui.topOS_comboBox_1, self.ui.FirstOS_Image)
        self.displayTopOS(self.OS_2, self.ui.topOS_comboBox_2, self.ui.SecondOS_Image)
        self.displayTopOS(self.OS_3, self.ui.topOS_comboBox_3, self.ui.ThirdOS_Image)
        self.displayAllProducts()

        self.menu_buttons = [self.ui.Products_pushButton, self.ui.Orders_pushButton, self.ui.Funds_pushButton,
                             self.ui.Complaints_pushButton,self.ui.StoreClerks_pushButton, self.ui.DeliveryCompanies_pushButton,
                             self.ui.Customers_pushButton, self.ui.AvoidList_pushButton, self.ui.TabooList_pushButton]

        # Open Pages
        self.ui.Products_pushButton.clicked.connect(lambda: self.openPage(self.ui.Products_Page, self.ui.Products_pushButton))
        self.ui.Orders_pushButton.clicked.connect(lambda: self.openPage(self.ui.Orders_Page, self.ui.Orders_pushButton))
        self.ui.Funds_pushButton.clicked.connect(lambda: self.openPage(self.ui.Funds_Page, self.ui.Funds_pushButton))
        self.ui.Complaints_pushButton.clicked.connect(lambda: self.openPage(self.ui.Complaints_Page, self.ui.Complaints_pushButton))
        self.ui.StoreClerks_pushButton.clicked.connect(lambda: self.openPage(self.ui.StoreClerks_Page, self.ui.StoreClerks_pushButton))
        self.ui.DeliveryCompanies_pushButton.clicked.connect(lambda: self.openPage(self.ui.DeliveryCompanies_Page, self.ui.DeliveryCompanies_pushButton))
        self.ui.Customers_pushButton.clicked.connect(lambda: self.openPage(self.ui.Customers_Page, self.ui.Customers_pushButton))
        self.ui.AvoidList_pushButton.clicked.connect(lambda: self.openPage(self.ui.AvoidList_Page, self.ui.AvoidList_pushButton))
        self.ui.TabooList_pushButton.clicked.connect(lambda: self.openPage(self.ui.TabooList_Page, self.ui.TabooList_pushButton))
        self.ui.managerProfile_pushButton.clicked.connect(lambda: self.ui.MenuContent_stackedWidget.setCurrentWidget(self.ui.Profile_Page))

        # Set Top Operating Systems
        self.ui.topOS_comboBox_1.activated.connect(lambda: self.setTopOS(self.ui.topOS_comboBox_1, self.ui.FirstOS_Image))
        self.ui.topOS_comboBox_2.activated.connect(lambda: self.setTopOS(self.ui.topOS_comboBox_2, self.ui.SecondOS_Image))
        self.ui.topOS_comboBox_3.activated.connect(lambda: self.setTopOS(self.ui.topOS_comboBox_3, self.ui.ThirdOS_Image))

        # Save Product
        
        # Display Product Info
        self.ui.Products_tableWidget.selectionModel().selectionChanged.connect(self.displayProductInfo)


    def openPage(self, page, button):
        self.ui.MenuContent_stackedWidget.setCurrentWidget(page)
        for b in self.menu_buttons:
            if b == button:
                button.setStyleSheet("QPushButton{color:rgb(60, 161, 255);} QPushButton:hover {color:rgb(60, 161, 255);}")
            else:
                b.setStyleSheet("QPushButton{color:rgb(112, 112, 112);} QPushButton:hover {color:rgb(60, 161, 255);}")


    #-------------Products Page Functions-------------#
                
    def displayTopOS(self, OS, OS_ComboBox, OS_Label):
        print("Y")
        # Display on screen
        # save all topOS1/2/3_ComboBox.currentText() value on text File
        try:
            index = OS_ComboBox.findText(OS)
            OS_ComboBox.setCurrentIndex(index)

            self.setTopOS(OS_ComboBox, OS_Label)
        except:
            print('Cannot proceed, something went wrong')

    def getAllProducts(self):
        try:
            # ID, name, price, OS, quantity, sold, profit, boughtPrice, images, description
            myfile = open("../Resources/Data/Products/products.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProductsData = []

            for singleLine in lines:
                newline = singleLine.strip()
                product = newline.split(", ")
                allProductsData.append(product)

            myfile.close()

            # ID, images
            myfile = open("../Resources/Data/Products/products_images.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProductsImages = []

            for singleLine in lines:
                newline = singleLine.strip()
                productImages = newline.split(", ")
                del productImages[0]
                allProductsImages.append(productImages)

            myfile.close()

            # ID, description
            myfile = open("../Resources/Data/Products/products_descriptions.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProductsDescriptions = []

            for singleLine in lines:
                newline = singleLine.strip()
                productDescription = newline.split(", ", 1)
                del productDescription[0]
                allProductsDescriptions.append(productDescription)

            i = 0
            for product in allProductsData:
                product.append(allProductsImages[i])
                product.append(allProductsDescriptions[i][0])
                i += 1

            myfile.close()

            allProducts = []
            for pData in allProductsData:
                #ID, name, price, OS, quantity, sold, profit, boughtPrice, images, description
                allProducts.append(storeProduct(pData[0], pData[1], pData[2], pData[3], pData[4], pData[5], pData[6], pData[7], pData[8], pData[9]))

            print(allProducts)

            return allProducts

        except:
            print('Cannot proceed, something went wrong')

    def setTopOS(self, OS_ComboBox, OS_Label):
        # Display on screen
        # save all topOS1/2/3_ComboBox.currentText() value on text File
        try:

            OS = OS_ComboBox.currentText().lower()

            windows_Pixmap  =   QPixmap('../Resources/Icons/windowsOS.png')
            macOS_Pixmap    =   QPixmap('../Resources/Icons/macOS.png')
            chrome_Pixmap   =   QPixmap('../Resources/Icons/chromeOS.png')
            linux_Pixmap    =   QPixmap('../Resources/Icons/linuxOS.png')

            if(OS == "windows"):
                OS_Label.setPixmap(windows_Pixmap);

            elif(OS =="macos"):
                OS_Label.setPixmap(macOS_Pixmap)

            elif(OS =="chrome"):
                OS_Label.setPixmap(chrome_Pixmap)

            elif(OS =="linux"):
                OS_Label.setPixmap(linux_Pixmap)

            elif(OS =="select"):
                OS_Label.clear()

            OS_Label.setMargin(25);
 
        except:
            print('Cannot proceed, something went wrong')


    def displayAllProducts(self):
        try:
            myfile = open("../Resources/Data/Products/products.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProducts = []

            for singleLine in lines:
                newline = singleLine.strip()
                product = newline.split(", ")
                allProducts.append(product)

            myfile.close()

            row = 0
            column = 0
            for p in allProducts: #rows
                self.ui.Products_tableWidget.insertRow(row)
                for column in range(7):
                    #0:productID, 1:name, 2:sellingPrice, 3:OS, 4:quantity, 5:sold, 6:profit, 7:boughtPrice, 8:quantityRated
                    self.ui.Products_tableWidget.setItem(row, column, QTableWidgetItem(str(p[column])))
                    column = column + 1

                row = row+1

        except:
            print('Cannot proceed, something went wrong')

    def addNewProduct(self):
        try:
            print("")
        except:
            print('Cannot proceed, something went wrong')

    def displayProductInfo(self, selected, deselected):
        try:
            index = self.ui.Products_tableWidget.currentIndex()
            NewIndex = self.ui.Products_tableWidget.model().index(index.row(), 0)
            pId = self.ui.Products_tableWidget.model().data(NewIndex)
            selectedProduct = None

            for p in self.allStoreProducts:
                if(p.getID() == pId):
                    selectedProduct = p
                    break

            print(pId, selectedProduct)
            
            self.ui.ProductID_Label.setText(selectedProduct.getID())

            self.ui.productName_lineEdit.setText(selectedProduct.getName())

            self.ui.productQuantityAvailable_LineEdit.setText(selectedProduct.getQuantity())

            self.ui.ProductBoughtPrice_lineEdit.setText(selectedProduct.getBoughtPrice())

            self.ui.ProductSellingPrice_lineEdit.setText(selectedProduct.getPrice())

            self.ui.ProductDescription_lineEdit.setText(selectedProduct.getDescription())

            index = self.ui.OS_ComboBox.findText(selectedProduct.getOperatingSystem())
            self.ui.OS_ComboBox.setCurrentIndex(index)

            self.ui.productQuantitySold_Label.setText(selectedProduct.getQuantitySold())

            self.ui.productProfit_Label.setText(selectedProduct.getProfit())

            self.ui.productRating_Label.setText("0")

        except:
            print('Cannot proceed, something went wrong')

    # def addProductImage(self): # add image to selected product
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def saveProduct(self): # take all the inputs and save it
    #     # set product attributes
    #     # save product on text file
    #     try:
    #         print("")
    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeProduct(self): # remove product from file and display first product
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Orders Page Functions-------------#

    # def displayAllOrders(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def displaySearchedOrder(self): # show error dialog if there is not match
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Funds Page Functions-------------#

    # def displayAvailableFunds(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def displayAllBankAccounts(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def addBankAccount(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeBankAccount(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def proceedWithdrawal(self):
    #     # show dialog with comboBox to select bank account
    #     # if there is not a bank account show a dialog message saying "Add a bank account to proceed"
    #     # If a bank account, then select one, the amount to withdraw, then proceed to withdrawal (circle loading icon) and show a dialog message
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Complaints Page Functions-------------#

    # def displayAllComplaints(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def displayComplaintInfo(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeComplaint(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def addWarningToUser(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Store Clerks Page Functions-------------#

    # def displayAllStoreClerks(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def addStoreClerk(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeStoreClerk(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def activateStoreClerk(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Delivery Companies Page Functions-------------#
    # def displayAllDeliveryCompanies(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def addDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def activateDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # #-------------Customers Page Functions-------------#
    # def displayAllCustomers(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def addDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def removeDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def activateDeliveryCompany(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

class storeProduct():
    def __init__(self, ID, name, price, OS, quantity, sold, profit, boughtPrice, images, description):
        self.ID = ID
        self.name = name
        self.price = price
        self.OS = OS
        self.quantity = quantity
        self.sold = sold
        self.profit = profit
        self.boughtPrice = boughtPrice
        self.images = images
        self.description = description

        self.ratedQuantity = 0
        self.totalRatingSum = 0


        
    def getID(self):
        return(self.ID)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getOperatingSystem(self):
        return self.OS

    def getQuantity(self):
        return self.quantity
        
    def getQuantitySold(self):
        return self.sold

    def getProfit(self):
        return self.profit

    def getBoughtPrice(self):
        return self.boughtPrice

    def getImages(self):
        return self.images

    def getDescription(self):
        return self.description
    


    def setID(self, ID):
        self.ID = ID

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setOperatingSystem(self, OS):
        self.OS = OS

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setQuantitySold(self, sold):
        self.sold = sold

    def setProfit(self, profit):
        self.profit = profit

    def setBoughtPrice(self, boughtPrice):
        self.boughtPrice = boughtPrice

    def setImages(self, images):
        self.images = images

    def setDescription(self, description):
        self.description = description


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = manager()
        window.ui.show()

        sys.exit(app.exec_())
