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

        # set all products
        self.allStoreProducts = self.setAllProducts()

        # set all complaints
        self.allUsersComplaints = self.setAllComplaints()

        # set all store clerks
        self.allStoreClerks = self.setAllStoreClerks()

        # set all delivery companies
        self.allDeliveryCompanies = self.setAllDeliveryCompanies()

        # set all customers
        self.allCustomers = self.setAllCustomers()

        # set avoid list
        self.allAvoidList = self.setAvoidList()

        self.displayTopOS()

        self.displayAllProducts()

        self.displayAllComplaints()

        self.menu_buttons = [self.ui.Products_pushButton, self.ui.Orders_pushButton,
                             self.ui.Complaints_pushButton,self.ui.StoreClerks_pushButton, self.ui.DeliveryCompanies_pushButton,
                             self.ui.Customers_pushButton, self.ui.AvoidList_pushButton, self.ui.TabooList_pushButton]

        # Open Pages
        self.ui.Products_pushButton.clicked.connect(lambda: self.openPage(self.ui.Products_Page, self.ui.Products_pushButton))
        self.ui.Orders_pushButton.clicked.connect(lambda: self.openPage(self.ui.Orders_Page, self.ui.Orders_pushButton))
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

        # Set Product Image
        self.ui.product_Image1_pushButton.clicked.connect(lambda: self.addProductImage(self.ui.product_Image1_pushButton,"1"))
        self.ui.product_Image2_pushButton.clicked.connect(lambda: self.addProductImage(self.ui.product_Image2_pushButton,"2"))
        self.ui.product_Image3_pushButton.clicked.connect(lambda: self.addProductImage(self.ui.product_Image3_pushButton,"3"))
        self.ui.product_Image4_pushButton.clicked.connect(lambda: self.addProductImage(self.ui.product_Image4_pushButton,"4"))
        self.ui.product_Image5_pushButton.clicked.connect(lambda: self.addProductImage(self.ui.product_Image5_pushButton,"5"))

        # Save Product
        self.ui.saveProduct_pushButton.clicked.connect(self.saveProduct)

        # Remove Product
        self.ui.removeProduct_pushButton.clicked.connect(self.removeProduct)

        # Add New Product
        self.ui.addNewProduct_pushButton.clicked.connect(self.addNewProduct)

        # Display Product Info
        self.ui.Products_tableWidget.selectionModel().selectionChanged.connect(self.displayProductInfo)

        # Display Complaints Info
        self.ui.Complaints_tableWidget.selectionModel().selectionChanged.connect(self.displayComplaintInfo)

        # Add Complaint Warning
        self.ui.Complaint_AddWarning_pushButton.clicked.connect(self.addWarningToUser)

        # Remove Complaint
        self.ui.Complaint_Remove_pushButton.clicked.connect(self.removeComplaint)

        # Display all Store Clerks
        self.ui.StoreClerks_pushButton.clicked.connect(self.displayAllStoreClerks)

        # Add Store Clerk
        self.ui.StoreClerk_Add_pushButton.clicked.connect(self.addStoreClerk)

        # Block Store Clerk
        self.ui.StoreClerk_Block_pushButton.clicked.connect(self.blockStoreClerk)

        # Activate Store Clerk 
        self.ui.StoreClerk_Activate_pushButton.clicked.connect(self.activateStoreClerk)

        # Display all Delivery Companies
        self.ui.DeliveryCompanies_pushButton.clicked.connect(self.displayAllDeliveryCompanies)

        # Add Delivery Company
        self.ui.DeliveryCompanies_Add_pushButton.clicked.connect(self.addDeliveryCompany)

        # Block Delivery Company
        self.ui.DeliveryCompanies_Block_pushButton.clicked.connect(self.blockDeliveryCompany)

        # Activate Delivery Company
        self.ui.DeliveryCompanies_Activate_pushButton.clicked.connect(self.activateDeliveryCompany)

        # Display Customers
        self.ui.Customers_pushButton.clicked.connect(self.displayAllCustomers)

        # Block Customer
        self.ui.Customer_Block_pushButton.clicked.connect(self.blockCustomer)

        # Activate Customer
        self.ui.Customer_Activate_pushButton.clicked.connect(self.activateCustomer)

        # Display Avoid List
        self.ui.AvoidList_pushButton.clicked.connect(self.displayAvoidList)

        # Activate User
        self.ui.AvoidList_Activate_pushButton.clicked.connect(self.activateUser)

    def openPage(self, page, button):
        try:
            self.ui.MenuContent_stackedWidget.setCurrentWidget(page)
            for b in self.menu_buttons:
                if b == button:
                    button.setStyleSheet("QPushButton{color:rgb(60, 161, 255);} QPushButton:hover {color:rgb(60, 161, 255);}")
                else:
                    b.setStyleSheet("QPushButton{color:rgb(112, 112, 112);} QPushButton:hover {color:rgb(60, 161, 255);}")
        except Exception as e:
            print('openPage(): Cannot proceed, something went wrong.\n', e)


#-------------Products Page Functions-------------#
                
    def displayTopOS(self):
        # Display on screen
        # save all topOS1/2/3_ComboBox.currentText() value on text File
        try:
            myfile = open("../Resources/Data/topOperatingSystems.txt", "r")
            next(myfile)
            lines = myfile.readlines()

            print(lines)

            if(len(lines) > 0):
                if(len(lines) == 1):
                    OS1 = lines[0].strip()

                    index1 = self.ui.topOS_comboBox_1.findText(OS1)
                    self.ui.topOS_comboBox_1.setCurrentIndex(index1)
                    self.setTopOS(self.ui.topOS_comboBox_1, self.ui.FirstOS_Image)

                elif(len(lines) == 2):
                    OS1 = lines[0].strip()

                    OS2 = lines[1].strip()

                    index1 = self.ui.topOS_comboBox_1.findText(OS1)
                    self.ui.topOS_comboBox_1.setCurrentIndex(index1)
                    self.setTopOS(self.ui.topOS_comboBox_1, self.ui.FirstOS_Image)

                    index2 = self.ui.topOS_comboBox_2.findText(OS2)
                    self.ui.topOS_comboBox_2.setCurrentIndex(index2)
                    self.setTopOS(self.ui.topOS_comboBox_2, self.ui.SecondOS_Image)

                elif(len(lines) == 3):

                    OS1 = lines[0].strip()

                    OS2 = lines[1].strip()

                    OS3 = lines[2].strip()

                    index1 = self.ui.topOS_comboBox_1.findText(OS1)
                    self.ui.topOS_comboBox_1.setCurrentIndex(index1)
                    self.setTopOS(self.ui.topOS_comboBox_1, self.ui.FirstOS_Image)

                    index2 = self.ui.topOS_comboBox_2.findText(OS2)
                    self.ui.topOS_comboBox_2.setCurrentIndex(index2)
                    self.setTopOS(self.ui.topOS_comboBox_2, self.ui.SecondOS_Image)

                    index3 = self.ui.topOS_comboBox_3.findText(OS3)
                    self.ui.topOS_comboBox_3.setCurrentIndex(index3)
                    self.setTopOS(self.ui.topOS_comboBox_3, self.ui.ThirdOS_Image)

            print(self.ui.topOS_comboBox_3.currentText())

        except Exception as e:
            print('displayTopOS(): Cannot proceed, something went wrong.\n', e)

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

            toSaveOS = []
            toSaveOS.append("TopOS\n")
            if(self.ui.topOS_comboBox_1.currentText() != "" and self.ui.topOS_comboBox_1.currentText() != "Select"):
                toSaveOS.append(self.ui.topOS_comboBox_1.currentText()+"\n")

            if(self.ui.topOS_comboBox_2.currentText() != "" and self.ui.topOS_comboBox_2.currentText() != "Select"):
                toSaveOS.append(self.ui.topOS_comboBox_2.currentText()+"\n")

            if(self.ui.topOS_comboBox_3.currentText() != "" and self.ui.topOS_comboBox_3.currentText() != "Select"):
                toSaveOS.append(self.ui.topOS_comboBox_3.currentText()+"\n")

            osFile = open("../Resources/Data/topOperatingSystems.txt", "w")
            osFile.writelines(toSaveOS)
            osFile.close()

        except Exception as e:
            print('setTopOS(): Cannot proceed, something went wrong.\n', e)
            
    def setAllProducts(self):
        try:
            # ID, name, price, OS, quantity, sold, profit, boughtPrice, weight, rating, images, description
            myfile = open("../Resources/Data/Products/products.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProductsData = []
            allProductsObjects = []

            for singleLine in lines:
                if singleLine != "\n":
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
                if singleLine != "\n":
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
                if singleLine != "\n":
                    newline = singleLine.strip()
                    productDescription = newline.split(", ", 1)
                    del productDescription[0]
                    allProductsDescriptions.append(productDescription)

            if len(allProductsData) > 0:
                i = 0
                for product in allProductsData:
                    product.append(allProductsImages[i])
                    product.append(allProductsDescriptions[i][0])
                    i += 1

                myfile.close()

                for pData in allProductsData:
                    # 0:ID, 1:name, 2:price, 3:OS, 4:quantity, 5:sold, 6:profit, 7:boughtPrice, 8:weight, 9:rating, 10:images, 11:description
                    allProductsObjects.append(storeProduct(pData[0], pData[1], pData[2], pData[3], pData[4], pData[5], pData[6], pData[7], pData[8], pData[9], pData[10], pData[11]))

            return allProductsObjects

        except Exception as e:
            print('getAllProducts(): Cannot proceed, something went wrong.\n', e)

    def displayAllProducts(self):
        try:
            myfile = open("../Resources/Data/Products/products.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allProducts = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    product = newline.split(", ")
                    allProducts.append(product)

            myfile.close()

            row = 0
            column = 0
            for p in allProducts: #rows
                self.ui.Products_tableWidget.insertRow(row)
                for column in range(7):
                    # 0:ID, 1:name, 2:price, 3:OS, 4:quantity, 5:sold, 6:profit, 7:boughtPrice, 8:weight, 9:rating, 10:images, 11:description
                    self.ui.Products_tableWidget.setItem(row, column, QTableWidgetItem(str(p[column])))

                row = row+1
            
        except Exception as e:
            print('displayAllProducts(): Cannot proceed, something went wrong.\n', e)

    def addNewProduct(self):
        try:
            row = self.ui.Products_tableWidget.rowCount()
            self.ui.Products_tableWidget.insertRow(row)

            if(row > 0):
                newId = self.allStoreProducts[-1].getID()
                newId = newId.replace('P', '')
                print("newId:", newId)
                pId = "P"+str(int(newId)+1)
            else:
                pId = "P0"

            self.ui.Products_tableWidget.setItem(row, 0, QTableWidgetItem(pId))
            self.ui.Products_tableWidget.setItem(row, 1, QTableWidgetItem("None"))
            self.ui.Products_tableWidget.setItem(row, 2, QTableWidgetItem("0"))
            self.ui.Products_tableWidget.setItem(row, 3, QTableWidgetItem("None"))
            self.ui.Products_tableWidget.setItem(row, 4, QTableWidgetItem("0"))
            self.ui.Products_tableWidget.setItem(row, 5, QTableWidgetItem("0"))
            self.ui.Products_tableWidget.setItem(row, 6, QTableWidgetItem("0"))

            # 0:ID, 1:name, 2:price, 3:OS, 4:quantity, 5:sold, 6:profit, 7:boughtPrice, 8:weight, 9:rating, 10:images, 11:description
            p = storeProduct(pId, "None", "0", "None", "0", "0", "0", "0", "0", "None", ["None"]*5, "None")
            self.allStoreProducts.append(p)
            
            pInfo = (str(p.getID()) + ", " + str(p.getName()) + ", " + str(p.getPrice()) + ", " + str(p.getOperatingSystem()) + ", " 
                  + str(p.getQuantity()) + ", " + str(p.getQuantitySold()) + ", " + str(p.getProfit()) + ", " 
                  + str(p.getBoughtPrice()) + ", " + str(p.getWeight()) + ", " + str(p.getRating()))

            pImages = (str(p.getID()) + ", " + str(p.getImages()[0]) + ", " + str(p.getImages()[1]) + ", " + str(p.getImages()[2]) + ", " 
                    + str(p.getImages()[3]) + ", " + str(p.getImages()[4]))

            pDescription = str(p.getID()) + ", " + str(p.getDescription())

            with open("../Resources/Data/Products/products.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(pInfo)
            
            with open("../Resources/Data/Products/products_images.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(pImages)

            with open("../Resources/Data/Products/products_descriptions.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(pDescription)
            
            pWeightPrice = str(p.getID()) + ", " + str(p.getName()) + ", " + str(p.getPrice()) + ", " + str(p.getWeight()) 
            with open("../Resources/Data/Products/productsWeightPrice.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(pWeightPrice)

        except Exception as e:
            print('addNewProduct(): Cannot proceed, something went wrong', e)

    def displayProductInfo(self):
        try:
            if(self.ui.Products_tableWidget.rowCount() > 0):
                index = self.ui.Products_tableWidget.currentIndex()
                NewIndex = self.ui.Products_tableWidget.model().index(index.row(), 0)
                pId = self.ui.Products_tableWidget.model().data(NewIndex)
                selectedProduct = None

                for p in self.allStoreProducts:
                    if(p.getID() == pId):
                        selectedProduct = p
                        break
                
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

                self.ui.productRating_Label.setText(selectedProduct.getRating())

                self.ui.ProductWeight_lineEdit.setText(selectedProduct.getWeight())

                imagePath = '../Resources/Data/Products/ProductsImages/' + str(selectedProduct.getID()) + "/"
                self.ui.product_Image1_pushButton.setText("")
                self.ui.product_Image2_pushButton.setText("")
                self.ui.product_Image3_pushButton.setText("")
                self.ui.product_Image4_pushButton.setText("")
                self.ui.product_Image5_pushButton.setText("")
                self.ui.product_Image1_pushButton.setIcon(QIcon(imagePath + selectedProduct.getImages()[0]))
                self.ui.product_Image2_pushButton.setIcon(QIcon(imagePath + selectedProduct.getImages()[1]))
                self.ui.product_Image3_pushButton.setIcon(QIcon(imagePath + selectedProduct.getImages()[2]))
                self.ui.product_Image4_pushButton.setIcon(QIcon(imagePath + selectedProduct.getImages()[3]))
                self.ui.product_Image5_pushButton.setIcon(QIcon(imagePath + selectedProduct.getImages()[4]))

        except Exception as e:
            print('displayProductInfo(): Cannot proceed, something went wrong.\n', e)

    def addProductImage(self, imageButton, imageNumber): # add image to selected product
        try:
            fileName = QFileDialog.getOpenFileName()
            filePath = fileName[0]
            
            imageButton.setText("")
            imageButton.setIcon(QIcon(filePath))

            index = self.ui.Products_tableWidget.currentIndex()
            NewIndex = self.ui.Products_tableWidget.model().index(index.row(), 0)
            pId = self.ui.Products_tableWidget.model().data(NewIndex)
            selectedProduct = None

            for p in self.allStoreProducts:
                if(p.getID() == pId):
                    selectedProduct = p
                    break
            
            fileExt = filePath.split(".")[-1]
            imageName = str(selectedProduct.getID()) + "_Image_" + str(imageNumber)+"."+fileExt

            # Create new directory for product images

            # Directory
            directory = str(selectedProduct.getID())
            
            # Parent Directory path
            parent_dir = '../Resources/Data/Products/ProductsImages/'
            
            # Path
            thePath = os.path.join(parent_dir, directory)

            if not os.path.exists(thePath):
                os.mkdir(thePath)

            fileExt = fileExt.lower()
            if(fileExt == "png" or fileExt == "jpeg" or fileExt == "svg"):
                newPath = shutil.copy(filePath, '../Resources/Data/Products/ProductsImages/' + str(selectedProduct.getID()) + "/" + imageName)

            selectedProduct.setImages((int(imageNumber)-1),imageName)
            # print(selectedProduct.getImages())

            for p in self.allStoreProducts:
                print(p.getImages())

        except Exception as e:
            print('addProductImage(): Cannot proceed, something went wrong.\n', e)

    def saveProduct(self): # take all the inputs and save it
        # set product attributes
        # save product on text file
        try:
            if self.ui.ProductID_Label.text() != "Select Product":
                index = self.ui.Products_tableWidget.currentIndex()
                NewIndex = self.ui.Products_tableWidget.model().index(index.row(), 0)
                pId = self.ui.Products_tableWidget.model().data(NewIndex)
                selectedProduct = None

                for p in self.allStoreProducts:
                    if(p.getID() == pId):
                        selectedProduct = p
                        break

                # Format: ID, name, price, OS, quantity, sold, profit, boughtPrice, images, description
                pName           =   self.ui.productName_lineEdit.text()
                pName           =   pName.replace(',', '')
                pSellingPrice   =   self.ui.ProductSellingPrice_lineEdit.text()
                pOS             =   self.ui.OS_ComboBox.currentText()
                pQuantity       =   self.ui.productQuantityAvailable_LineEdit.text()
                pBoughtPrice    =   self.ui.ProductBoughtPrice_lineEdit.text()
                pWeight         =   self.ui.ProductWeight_lineEdit.text()
                pDescription    =   self.ui.ProductDescription_lineEdit.text()

                selectedProduct.setName(pName)
                selectedProduct.setPrice(pSellingPrice)
                selectedProduct.setOperatingSystem(pOS)
                selectedProduct.setQuantity(pQuantity)
                selectedProduct.setBoughtPrice(pBoughtPrice)
                selectedProduct.setWeight(pWeight)
                selectedProduct.setDescription(pDescription)

                productFileInfo = (str(selectedProduct.getID()) + ", " + str(pName) + ", " + str(pSellingPrice) + ", " + str(pOS) + ", " 
                                + str(pQuantity) + ", " + str(selectedProduct.getQuantitySold()) + ", " + str(selectedProduct.getProfit()) + ", " 
                                + str(pBoughtPrice) + ", " + str(pWeight) + ", " + str(selectedProduct.getRating()) + "\n")
                print(productFileInfo)

                productImagesInfo = (str(selectedProduct.getID()) + ", " + str(selectedProduct.getImages()[0]) + ", " + str(selectedProduct.getImages()[1]) + ", " + str(selectedProduct.getImages()[2]) + ", " 
                                + str(selectedProduct.getImages()[3]) + ", " + str(selectedProduct.getImages()[4]) + "\n")
                print(productImagesInfo)

                productDescriptionInfo = (str(selectedProduct.getID()) + ", " + str(pDescription) + "\n")
                print(productDescriptionInfo)

                for line in fileinput.input("../Resources/Data/Products/products.txt", inplace=1):
                    if str(selectedProduct.getID()) in line:
                        line = productFileInfo
                    sys.stdout.write(line)

                for line in fileinput.input("../Resources/Data/Products/products_images.txt", inplace=1):
                    if str(selectedProduct.getID()) in line:
                        line = productImagesInfo
                    sys.stdout.write(line)
                
                for line in fileinput.input("../Resources/Data/Products/products_descriptions.txt", inplace=1):
                    if str(selectedProduct.getID()) in line:
                        line = productDescriptionInfo
                    sys.stdout.write(line)

                pWeightPrice = str(selectedProduct.getID()) + ", " + str(pName) + ", " + str(pSellingPrice) + ", " + str(pWeight) + "\n"
                for line in fileinput.input("../Resources/Data/Products/productsWeightPrice.txt", inplace=1):
                    if str(selectedProduct.getID()) in line:
                        line = pWeightPrice
                    sys.stdout.write(line)

                self.ui.Products_tableWidget.setRowCount(0)
                self.displayAllProducts()

            else:
                print("Select Product to save.")

        except Exception as e:
            print('saveProduct(): Cannot proceed, something went wrong.\n', e)

    def removeProduct(self): # remove product from file and display first product
        try:
            if self.ui.ProductID_Label.text() != "Select Product":
                index = self.ui.Products_tableWidget.currentIndex()
                NewIndex = self.ui.Products_tableWidget.model().index(index.row(), 0)
                pId = self.ui.Products_tableWidget.model().data(NewIndex)
                selectedProduct = None

                for p in self.allStoreProducts:
                    if(p.getID() == pId):
                        selectedProduct = p
                        break

                self.allStoreProducts.remove(selectedProduct)
                
                selected = self.ui.Products_tableWidget.currentRow()
                self.ui.Products_tableWidget.removeRow(selected)

                pFiles = ["../Resources/Data/Products/products.txt", "../Resources/Data/Products/products_descriptions.txt", 
                          "../Resources/Data/Products/products_images.txt", "../Resources/Data/Products/productsWeightPrice.txt"]

                # remove product line
                for fileName in pFiles:
                    for line in fileinput.input(fileName, inplace=1):
                        if str(selectedProduct.getID()) in line:
                            line = ""
                        sys.stdout.write(line)

                # remove blank spaces
                for fileName in pFiles:  
                    with open(fileName) as filehandle:
                        lines = filehandle.readlines()

                    with open(fileName, 'w') as filehandle:
                        lines = filter(lambda x: x.strip(), lines)
                        filehandle.writelines(lines) 

            else:
                print("Select Product to remove.")

        except Exception as e:
            print('removeProduct(): Cannot proceed, something went wrong.', e)

#-------------Orders Page Functions-------------#

    # def displayAllOrders(self):
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

    # def displaySearchedOrder(self): # show error dialog if there is not match
    #     try:

    #     except:
    #         print('Cannot proceed, something went wrong')

#-------------Complaints Page Functions-------------#

    def displayAllComplaints(self):
        try:
            self.ui.Complaints_tableWidget.setRowCount(0)

            myfile = open("../Resources/Data/UsersComplaints/usersComplaints.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allComplaints = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    c = newline.split(", ")
                    allComplaints.append(c)
            myfile.close()

            # get warnings
            for complaint in allComplaints:
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt", inplace=1):
                    # get ToUserID in warnings
                    if str(complaint[2]) in line: # if user is found get warning
                        complaint.append(line.split(", ")[1])
                    sys.stdout.write(line)
            
            # get status
            for complaint in allComplaints:
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    # get ToUserID status
                    if str(complaint[2]) in line: # if user is found get status
                        complaint.append(line.split(", ")[1])
                    sys.stdout.write(line)

            print(allComplaints)
            row = 0
            column = 0
            for complaint in allComplaints: 
                self.ui.Complaints_tableWidget.insertRow(row)
                for column in range(6):
                    # complaintID, userID, name, userType, warnings, userStatus
                    self.ui.Complaints_tableWidget.setItem(row, column, QTableWidgetItem(str(complaint[column])))

                row = row+1
        except Exception as e:
            print('Cannot proceed, something went wrong.', e)

    def setAllComplaints(self):
        try:
            # complaintID, userID, userName, userType, warnings, userStatus, description, complaintJustification, messageToUser
            myfile = open("../Resources/Data/UsersComplaints/usersComplaints.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allComplaintsData = []
            allObjects = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ")
                    allComplaintsData.append(line)

            myfile.close()

            # ID, description
            myfile = open("../Resources/Data/UsersComplaints/usersComplaintsDescriptions.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allDescriptions = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ", 1)
                    del line[0]
                    allDescriptions.append(line[0])

            myfile.close()

            # ID, justification
            myfile = open("../Resources/Data/UsersComplaints/usersComplaintsJustifications.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allJustification = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ", 1)
                    del line[0]
                    allJustification.append(line[0])

            # ID, messages to user
            myfile = open("../Resources/Data/UsersComplaints/usersComplaintsMessages.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allMessages = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ", 1)
                    del line[0]
                    allMessages.append(line[0])
            
            # add all
            if len(allComplaintsData) > 0:
                i = 0
                for d in allComplaintsData:
                    d.append(allDescriptions[i])
                    d.append(allJustification[i])
                    d.append(allMessages[i])
                    i += 1
                
                myfile.close()

                for pData in allComplaintsData:
                    # 0:complaintID, 1:fromUserID, 2:toUserID, 3:toUserType, 4:toUserStatus, 5:toUserWarnings, 6:description, 7:justification, 8:messageToUser
                    allObjects.append(userComplaint(pData[0], pData[1], pData[2], pData[3], "None", "0000", pData[4], pData[5], pData[6]))

            return allObjects

        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def displayComplaintInfo(self):
        try:
            if(self.ui.Complaints_tableWidget.rowCount() > 0):
                index = self.ui.Complaints_tableWidget.currentIndex()
                NewIndex = self.ui.Complaints_tableWidget.model().index(index.row(), 0)
                ctId = self.ui.Complaints_tableWidget.model().data(NewIndex)
                selected = None

                for ct in self.allUsersComplaints:
                    if(ct.getComplaintID() == ctId):
                        selected = ct
                        break

                if(selected != None):
                    complaintFrom = ""
                    complaintTo = ""

                    storeClerksFile = "../Resources/Data/storeClerks.txt"
                    deliveryCompanyFile = "../Resources/Data/deliveryCompanies.txt"
                    customersFile = "../Resources/Data/customers.txt"
                    
                    for line in fileinput.input(storeClerksFile, inplace=1):
                        if str(selected.getToUserID()) in line:
                            complaintTo = line.split(", ")[2]
                        sys.stdout.write(line)

                    for line in fileinput.input(deliveryCompanyFile, inplace=1):
                        if str(selected.getToUserID()) in line:
                            complaintTo = line.split(", ")[2]
                        sys.stdout.write(line)
                    
                    for line in fileinput.input(customersFile, inplace=1):
                        if str(selected.getFromUserID()) in line:
                            complaintFrom = line.split(", ")[1]
                        sys.stdout.write(line)

                    complaintToUserType = selected.getToUserType()
                    complaintJustification = selected.getJustification()
                    complaintDescription = selected.getDescription()
                    complaintMessage = selected.getMessageToUser()

                    self.ui.Complaint_FromUserName_Label.setText(str(complaintFrom))
                    self.ui.Complaint_ToUserName_Label.setText(str(complaintTo))
                    self.ui.Complaint_ToUserType_Label.setText(str(complaintToUserType))
                    self.ui.Complaint_Description_Label.setText(str(complaintDescription))
                    self.ui.Complaint_UserJustification_Label.setText(str(complaintJustification))
                    self.ui.Complaint_MessageToUser_lineEdit.setText(str(complaintMessage))

                    print(selected.getToUserWarnings())
        
        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def removeComplaint(self):
        try:
            indexes = self.ui.Complaints_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.Complaints_tableWidget.currentIndex()
                NewIndex = self.ui.Complaints_tableWidget.model().index(index.row(), 0)
                ctId = self.ui.Complaints_tableWidget.model().data(NewIndex)
                selected = None

                for ct in self.allUsersComplaints:
                    if(ct.getComplaintID() == ctId):
                        selected = ct
                        break

                if(selected != None):
                    self.allUsersComplaints.remove(selected)
                    
                    selectedRow = self.ui.Complaints_tableWidget.currentRow()
                    self.ui.Complaints_tableWidget.removeRow(selectedRow)

                    pFiles = ["../Resources/Data/UsersComplaints/usersComplaints.txt", "../Resources/Data/UsersComplaints/usersComplaintsDescriptions.txt", 
                              "../Resources/Data/UsersComplaints/usersComplaintsJustifications.txt", "../Resources/Data/UsersComplaints/usersComplaintsMessages.txt"]
                    
                    # remove product line
                    for fileName in pFiles:
                        for line in fileinput.input(fileName, inplace=1):
                            if str(selected.getComplaintID()) in line:
                                line = ""
                            sys.stdout.write(line)

                    # remove blank spaces
                    for fileName in pFiles:  
                        with open(fileName) as filehandle:
                            lines = filehandle.readlines()

                        with open(fileName, 'w') as filehandle:
                            lines = filter(lambda x: x.strip(), lines)
                            filehandle.writelines(lines) 

            else:
                print("Select Complaint to remove.")
        except:
            print('Cannot proceed, something went wrong')

    def addWarningToUser(self):
        try:
            index = self.ui.Complaints_tableWidget.currentIndex()
            NewIndex = self.ui.Complaints_tableWidget.model().index(index.row(), 0)
            ctId = self.ui.Complaints_tableWidget.model().data(NewIndex)
            selected = None
            warnings = 0
            for ct in self.allUsersComplaints:
                if(ct.getComplaintID() == ctId):
                    selected = ct
                    break

            if(selected != None):
                # get warnings
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt", inplace=1):
                    # get ToUserID in warnings
                    if str(selected.getToUserID()) in line: # if user is found add warning
                        warnings = int(line.split(", ")[1])+1
                        line = str(line.split(", ")[0]) + ", " + str(int(warnings))
                    sys.stdout.write(line)

                for line in fileinput.input("../Resources/Data/UsersComplaints/usersComplaintsMessages.txt", inplace=1):
                    # get complaint ID in file
                    if str(selected.getComplaintID()) in line:
                        line = str(line.split(", ")[0]) + ", " + self.ui.Complaint_MessageToUser_lineEdit.text()
                    sys.stdout.write(line)

                if(warnings >= 3):
                    for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                        # get ToUserID in warnings
                        if str(selected.getToUserID()) in line: # if user is found add warning
                            line = str(line.split(", ")[0]) + ", " + "Blocked\n"
                        sys.stdout.write(line)

                self.displayAllComplaints()
                self.allUsersComplaints = self.setAllComplaints()



        except:
            print('Cannot proceed, something went wrong')

#-------------Store Clerks Page Functions-------------#

    def displayAllStoreClerks(self):
        try:
            self.ui.StoreClerks_tableWidget.setRowCount(0)

            self.allStoreClerks = self.setAllStoreClerks()

            row = 0
            for data in self.allStoreClerks: 
                self.ui.StoreClerks_tableWidget.insertRow(row)
                # accessCode, ID, name, status, email
                self.ui.StoreClerks_tableWidget.setItem(row, 0, QTableWidgetItem(str(data.getAccessCode())))
                self.ui.StoreClerks_tableWidget.setItem(row, 1, QTableWidgetItem(str(data.getID())))
                self.ui.StoreClerks_tableWidget.setItem(row, 2, QTableWidgetItem(str(data.getName())))
                self.ui.StoreClerks_tableWidget.setItem(row, 3, QTableWidgetItem(str(data.getStatus())))
                self.ui.StoreClerks_tableWidget.setItem(row, 4, QTableWidgetItem(str(data.getEmail())))
                row = row+1

        except Exception as e:
            print('Cannot proceed, something went wrong.', e)

    def setAllStoreClerks(self):
        try:
            myfile = open("../Resources/Data/storeClerks.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allClerks = []
            allObjects = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ")
                    allClerks.append(line)

            myfile.close()
            
            # add all
            if len(allClerks) > 0:
                for pData in allClerks:
                    # 0:AccessCode, 1:ID, 2:name, 3:status, 4:email
                    allObjects.append(storeClerks(pData[0], pData[1], pData[2], pData[3], pData[4]))

            return allObjects

        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def addStoreClerk(self):
        try:
            row = self.ui.StoreClerks_tableWidget.rowCount()
            self.ui.StoreClerks_tableWidget.insertRow(row)

            if(row > 0):
                newId = self.allStoreClerks[-1].getID()
                newAccessCode = self.allStoreClerks[-1].getAccessCode()
                newAccessCode = newAccessCode.replace('SAC', '')
                newId = newId.replace('S', '')
                pId = "S"+str(int(newId)+1)
                accessCode = "SAC"+str(int(newAccessCode)+1)
            else:
                pId = "S0"
                accessCode = "SAC1000"

            self.ui.StoreClerks_tableWidget.setItem(row, 0, QTableWidgetItem(accessCode))
            self.ui.StoreClerks_tableWidget.setItem(row, 1, QTableWidgetItem(pId))
            self.ui.StoreClerks_tableWidget.setItem(row, 2, QTableWidgetItem("Name"))
            self.ui.StoreClerks_tableWidget.setItem(row, 3, QTableWidgetItem("Active"))
            self.ui.StoreClerks_tableWidget.setItem(row, 4, QTableWidgetItem("Email"))
            
            info = (accessCode + ", " + pId + ", Name, Active, Email")

            userStatus = pId + ", Active"

            with open("../Resources/Data/storeClerks.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(info)
            
            with open("../Resources/Data/UsersComplaints/usersStatus.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(userStatus)

            self.allStoreClerks = self.setAllStoreClerks()

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

    def blockStoreClerk(self):
        try:
            indexes = self.ui.StoreClerks_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.StoreClerks_tableWidget.currentIndex()
                NewIndex = self.ui.StoreClerks_tableWidget.model().index(index.row(), 1)
                pId = self.ui.StoreClerks_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allStoreClerks:
                    if(p.getID() == pId):
                        selected = p
                        break
                print("S", selected.getStatus())

                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Blocked\n"
                    sys.stdout.write(line)
                
                lineInfo  = (str(selected.getAccessCode()) + ", " + str(selected.getID()) + ", " 
                          + str(selected.getName()) + ", Blocked" + ", " + str(selected.getEmail()) + "\n")
                for line in fileinput.input("../Resources/Data/storeClerks.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllStoreClerks()
            else:
                print("Select Store Clerk to block.")
        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

    def activateStoreClerk(self):
        try:
            indexes = self.ui.StoreClerks_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.StoreClerks_tableWidget.currentIndex()
                NewIndex = self.ui.StoreClerks_tableWidget.model().index(index.row(), 1)
                pId = self.ui.StoreClerks_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allStoreClerks:
                    if(p.getID() == pId):
                        selected = p
                        break

                selected.setStatus()
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Active\n"
                    sys.stdout.write(line)

                lineInfo  = (str(selected.getAccessCode()) + ", " + str(selected.getID()) + ", " 
                          + str(selected.getName()) + ", Active" + ", " + str(selected.getEmail()) + "\n")
                for line in fileinput.input("../Resources/Data/storeClerks.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllStoreClerks()
            else:
                print("Select Store Clerk to Activate.")

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

#-------------Delivery Companies Page Functions-------------#

    def setAllDeliveryCompanies(self):
        try:
            myfile = open("../Resources/Data/deliveryCompanies.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allDeliveryCompanies = []
            allObjects = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ")
                    allDeliveryCompanies.append(line)

            myfile.close()
            
            # add all
            if len(allDeliveryCompanies) > 0:
                for pData in allDeliveryCompanies:
                    # 0:AccessCode, 1:ID, 2:name, 3:status, 4:email
                    allObjects.append(deliveryCompanies(pData[0], pData[1], pData[2], pData[3], pData[4]))

            return allObjects

        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def displayAllDeliveryCompanies(self):
        try:
            self.ui.DeliveryCompany_tableWidget.setRowCount(0)

            self.allDeliveryCompanies = self.setAllDeliveryCompanies()

            print(self.allDeliveryCompanies)
            row = 0
            for data in self.allDeliveryCompanies: 
                self.ui.DeliveryCompany_tableWidget.insertRow(row)
                # accessCode, ID, name, status, email
                self.ui.DeliveryCompany_tableWidget.setItem(row, 0, QTableWidgetItem(str(data.getAccessCode())))
                self.ui.DeliveryCompany_tableWidget.setItem(row, 1, QTableWidgetItem(str(data.getID())))
                self.ui.DeliveryCompany_tableWidget.setItem(row, 2, QTableWidgetItem(str(data.getName())))
                self.ui.DeliveryCompany_tableWidget.setItem(row, 3, QTableWidgetItem(str(data.getStatus())))
                self.ui.DeliveryCompany_tableWidget.setItem(row, 4, QTableWidgetItem(str(data.getEmail())))
                row = row+1

        except Exception as e:
            print('Cannot proceed, something went wrong.', e)

    def addDeliveryCompany(self):
        try:
            row = self.ui.StoreClerks_tableWidget.rowCount()
            self.ui.DeliveryCompany_tableWidget.insertRow(row)

            if(row > 0):
                newId = self.allStoreClerks[-1].getID()
                newAccessCode = self.allStoreClerks[-1].getAccessCode()
                newAccessCode = newAccessCode.replace('DAC', '')
                newId = newId.replace('D', '')
                pId = "D"+str(int(newId)+1)
                accessCode = "DAC"+str(int(newAccessCode)+1)
            else:
                pId = "D0"
                accessCode = "DAC1000"

            self.ui.DeliveryCompany_tableWidget.setItem(row, 0, QTableWidgetItem(accessCode))
            self.ui.DeliveryCompany_tableWidget.setItem(row, 1, QTableWidgetItem(pId))
            self.ui.DeliveryCompany_tableWidget.setItem(row, 2, QTableWidgetItem("Name"))
            self.ui.DeliveryCompany_tableWidget.setItem(row, 3, QTableWidgetItem("Active"))
            self.ui.DeliveryCompany_tableWidget.setItem(row, 4, QTableWidgetItem("Email"))
            
            info = (accessCode + ", " + pId + ", Name, Active, Email")

            userStatus = pId + ", Active"

            with open("../Resources/Data/storeClerks.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(info)
            
            with open("../Resources/Data/UsersComplaints/usersStatus.txt", "a") as a_file:
                a_file.write("\n")
                a_file.write(userStatus)

            self.allDeliveryCompanies = self.setAllDeliveryCompanies()

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

    def blockDeliveryCompany(self):
        try:
            indexes = self.ui.DeliveryCompany_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.DeliveryCompany_tableWidget.currentIndex()
                NewIndex = self.ui.DeliveryCompany_tableWidget.model().index(index.row(), 1)
                pId = self.ui.DeliveryCompany_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allDeliveryCompanies:
                    if(p.getID() == pId):
                        selected = p
                        break

                print(selected.getID())
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Blocked\n"
                    sys.stdout.write(line)
                
                lineInfo  = (str(selected.getAccessCode()) + ", " + str(selected.getID()) + ", " 
                          + str(selected.getName()) + ", Blocked" + ", " + str(selected.getEmail()) + "\n")
                print(lineInfo)
                for line in fileinput.input("../Resources/Data/deliveryCompanies.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllDeliveryCompanies()
            else:
                print("Select Delivery Company to block.")
        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

    def activateDeliveryCompany(self):
        try:
            indexes = self.ui.DeliveryCompany_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.DeliveryCompany_tableWidget.currentIndex()
                NewIndex = self.ui.DeliveryCompany_tableWidget.model().index(index.row(), 1)
                pId = self.ui.DeliveryCompany_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allDeliveryCompanies:
                    if(p.getID() == pId):
                        selected = p
                        break

                selected.setStatus()
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Active\n"
                    sys.stdout.write(line)

                lineInfo  = (str(selected.getAccessCode()) + ", " + str(selected.getID()) + ", " 
                          + str(selected.getName()) + ", Active" + ", " + str(selected.getEmail()) + "\n")
                for line in fileinput.input("../Resources/Data/deliveryCompanies.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllDeliveryCompanies()
            else:
                print("Select Delivery Company to Activate.")

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

#-------------Customers Page Functions-------------#
    def setAllCustomers(self):
        try:
            myfile = open("../Resources/Data/customers.txt", "r")
            next(myfile)
            lines = myfile.readlines()
            allCust = []
            allObjects = []

            for singleLine in lines:
                if singleLine != "\n":
                    newline = singleLine.strip()
                    line = newline.split(", ")
                    allCust.append(line)

            myfile.close()
            
            # add all
            if len(allCust) > 0:
                for pData in allCust:
                    # ID, name, status, email
                    allObjects.append(storeCustomers(pData[0], pData[1], pData[2], pData[3]))

            return allObjects

        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def displayAllCustomers(self):
        # try:
            self.ui.Customers_tableWidget.setRowCount(0)

            self.allCustomers = self.setAllCustomers()

            row = 0
            for data in self.allCustomers: 
                self.ui.Customers_tableWidget.insertRow(row)
                # ID, name, status, email
                self.ui.Customers_tableWidget.setItem(row, 0, QTableWidgetItem(str(data.getID())))
                self.ui.Customers_tableWidget.setItem(row, 1, QTableWidgetItem(str(data.getName())))
                self.ui.Customers_tableWidget.setItem(row, 2, QTableWidgetItem(str(data.getStatus())))
                self.ui.Customers_tableWidget.setItem(row, 3, QTableWidgetItem(str(data.getEmail())))
                row = row+1

        # except Exception as e:
        #     print('Cannot proceed, something went wrong.', e)

    def blockCustomer(self):
        # try:
            indexes = self.ui.Customers_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.Customers_tableWidget.currentIndex()
                NewIndex = self.ui.Customers_tableWidget.model().index(index.row(), 0)
                pId = self.ui.Customers_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allCustomers:
                    if(p.getID() == pId):
                        selected = p
                        break

                print(selected.getID())
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Blocked\n"
                    sys.stdout.write(line)
                
                lineInfo  = (str(selected.getID()) + ", " + str(selected.getName()) + ", Blocked" + ", " + str(selected.getEmail()) + "\n")
                print(lineInfo)
                for line in fileinput.input("../Resources/Data/customers.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllCustomers()
            else:
                print("Select Customer to block.")
        # except Exception as e:
        #     print(' Cannot proceed, something went wrong', e)

    def activateCustomer(self):
        try:
            indexes = self.ui.Customers_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.Customers_tableWidget.currentIndex()
                NewIndex = self.ui.Customers_tableWidget.model().index(index.row(), 0)
                pId = self.ui.Customers_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allCustomers:
                    if(p.getID() == pId):
                        selected = p
                        break

                selected.setStatus()
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Active\n"
                    sys.stdout.write(line)

                lineInfo  = (str(selected.getID()) + ", " + str(selected.getName()) + ", Active" + ", " + str(selected.getEmail()) + "\n")
                for line in fileinput.input("../Resources/Data/customers.txt", inplace=1):
                    if str(selected.getID()) in line:
                        line = lineInfo
                    sys.stdout.write(line)

                self.displayAllCustomers()
            else:
                print("Select Customer to Activate.")

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

#-------------Avoid List--------------#
    def setAvoidList(self):
        try:
            filesName = ["../Resources/Data/customers.txt", "../Resources/Data/deliveryCompanies.txt", "../Resources/Data/storeClerks.txt"]
            allAvoidUsers = []
            allObjects = []
            for fileName in filesName:
                for line in fileinput.input(fileName, inplace=1):
                    if str("Blocked") in line: 
                        allAvoidUsers.append(lines.split(", "))
                    sys.stdout.write(line)

            print("B:", allAvoidUsers)
            
            # add all
            if len(allAvoidUsers) > 0:
                for pData in allAvoidUsers:
                    # ID, name, status, email
                    allObjects.append(avoidList(pData[0], pData[1], pData[2], pData[3]))

            print("Classes:", allObjects)
            return allObjects

        except Exception as e:
            print('Cannot proceed, something went wrong.\n', e)

    def displayAvoidList(self):
        # try:
                self.ui.AvoidList_tableWidget.setRowCount(0)

                self.allAvoidList = self.setAvoidList()

                print(self.allAvoidList)
                row = 0
                for data in self.allAvoidList: 
                    self.ui.AvoidList_tableWidget.insertRow(row)
                    # ID, name, status, email
                    self.ui.AvoidList_tableWidget.setItem(row, 0, QTableWidgetItem(str(data.getID())))
                    self.ui.AvoidList_tableWidget.setItem(row, 1, QTableWidgetItem(str(data.getName())))
                    self.ui.AvoidList_tableWidget.setItem(row, 2, QTableWidgetItem(str(data.getStatus())))
                    self.ui.AvoidList_tableWidget.setItem(row, 3, QTableWidgetItem(str(data.getEmail())))
                    row = row+1

            # except Exception as e:
            #     print('Cannot proceed, something went wrong.', e)

    def activateUser(self):
        try:
            indexes = self.ui.AvoidList_tableWidget.selectionModel().selectedRows()
            if(len(indexes) > 0):
                index = self.ui.AvoidList_tableWidget.currentIndex()
                NewIndex = self.ui.AvoidList_tableWidget.model().index(index.row(), 0)
                pId = self.ui.AvoidList_tableWidget.model().data(NewIndex)
                selected = None

                for p in self.allAvoidUsers:
                    if(p.getID() == pId):
                        selected = p
                        break

                selected.setStatus()
                for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
                    if str(selected.getID()) in line: 
                        line = str(line.split(", ")[0]) + ", " + "Active\n"
                    sys.stdout.write(line)

                lineInfo  = (str(selected.getID()) + ", " + str(selected.getName()) + ", Active" + ", " + str(selected.getEmail()) + "\n")
                filesName = ["../Resources/Data/customers.txt", "../Resources/Data/deliveryCompanies.txt", "../Resources/Data/storeClerks.txt"]
                for fileName in filesName:
                    for line in fileinput.input(fileName, inplace=1):
                        if str(selected.getID()) in line: 
                            line = lineInfo
                        sys.stdout.write(line)


                self.allAvoidUsers.remove(selected)
                    
                s = self.ui.AvoidList_tableWidget.currentRow()
                self.ui.AvoidList_tableWidget.removeRow(s)

            else:
                print("Select Customer to Activate.")

        except Exception as e:
            print(' Cannot proceed, something went wrong', e)

class storeProduct():
    def __init__(self, ID, name, price, OS, quantity, sold, profit, boughtPrice, weight, rating, images, description):
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
        self.rating = rating
        self.weight = weight
        
        self.setRating()

    def getID(self):
        return(self.ID)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getOperatingSystem(self):
        return self.OS

    def getQuantity(self):
        return str(int(self.quantity) - int(self.sold))
        
    def getQuantitySold(self):
        return self.sold

    def getProfit(self):
        return self.profit

    def getBoughtPrice(self):
        return self.boughtPrice

    def getWeight(self):
        return self.weight

    def getRating(self):
        return self.rating

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

    def setRating(self):
        # read all ratings from orders with this specific product id (if rating != none)
        # count each rating, add them, and then divide then by the total ratings
        self.rating = "None"

    def setWeight(self, weight):
        self.weight = weight

    def setImages(self, imagesNumber, image):
        self.images[imagesNumber] = image

    def setDescription(self, description):
        self.description = description

class userComplaint():
    def __init__(self, complaintID, fromUserID, toUserID, toUserType, toUserStatus, toUserWarnings, description, justification, messageToUser):
        self.complaintID = complaintID
        self.fromUserID = fromUserID
        self.toUserID = toUserID
        self.toUserType = toUserType
        self.toUserWarnings = toUserWarnings
        self.toUserStatus = toUserStatus
        self.description = description
        self.justification = justification
        self.messageToUser = messageToUser

        self.setToUserWarnings()
        self.setToUserStatus()

    def getComplaintID(self):
        return self.complaintID
    def getFromUserID(self):
        return self.fromUserID
    def getToUserID(self):
        return self.toUserID
    def getToUserType(self):
        return self.toUserType
    def getToUserWarnings(self):
        return self.toUserWarnings
    def getToUserStatus(self):
        return self.toUserStatus
    def getDescription(self):
        return self.description
    def getJustification(self):
        return self.justification
    def getMessageToUser(self):
        return self.messageToUser

    def setComplaintID(self, complaintID):
        self.complaintID = complaintID
    def setFromUserID(self, fromUserID):
        self.fromUserID = fromUserID
    def setToUserID(self, toUserID):
        self.toUserID = toUserID
    def setToUserType(self, toUserType):
        self.toUserType = toUserType

    def setToUserWarnings(self):
        # get warnings
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt", inplace=1):
            # get to user complaint ID
            if str(self.getToUserID()) in line: # if user is found set warnings
                self.toUserWarnings = line.split(", ")[1]
            sys.stdout.write(line)

    def setToUserStatus(self):
        # get status
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
            # get ToUserID status
            if str(self.getToUserID()) in line: # if user is found set status
                self.toUserStatus = line.split(", ")[1]
            sys.stdout.write(line)

    def setDescription(self, description):
        self.description = description
    def setComplaintJustification(self, complaintJustification):
        self.justification = justification
    def setMessageToUser(self, messageToUser):
        self.messageToUser = messageToUser

class storeClerks():
    def __init__(self, accessCode, ID, name, status, email):
        self.accessCode = accessCode
        self.ID = ID
        self.name = name
        self.status = status
        self.email = email

        self.setStatus()

    def getAccessCode(self):
        return self.accessCode
    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getEmail(self):
        return self.email

    def setAccessCode(self, accessCode):
        self.accessCode = accessCode
    def setID(self, ID):
        self.ID = ID
    def setName(self, name):
        self.name = name

    def setStatus(self):
        # get status
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
            # get ToUserID status
            if str(self.getID()) in line: # if user is found set status
                self.status = line.split(", ")[1]
            sys.stdout.write(line)

    def setEmail(self, email):
        self.email = email

class deliveryCompanies():
    def __init__(self, accessCode, ID, name, status, email):
        self.accessCode = accessCode
        self.ID = ID
        self.name = name
        self.status = status
        self.email = email

        self.setStatus()

    def getAccessCode(self):
        return self.accessCode
    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getEmail(self):
        return self.email

    def setAccessCode(self, accessCode):
        self.accessCode = accessCode
    def setID(self, ID):
        self.ID = ID
    def setName(self, name):
        self.name = name

    def setStatus(self):
        # get status
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
            # get ToUserID status
            if str(self.getID()) in line: # if user is found set status
                self.status = line.split(", ")[1]
            sys.stdout.write(line)

    def setEmail(self, email):
        self.email = email

class storeCustomers():
    def __init__(self, ID, name, status, email):
        self.ID = ID
        self.name = name
        self.status = status
        self.email = email

        self.setStatus()

    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getEmail(self):
        return self.email

    def setID(self, ID):
        self.ID = ID
    def setName(self, name):
        self.name = name

    def setStatus(self):
        # get status
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
            # get ToUserID status
            if str(self.getID()) in line: # if user is found set status
                self.status = line.split(", ")[1]
            sys.stdout.write(line)

    def setEmail(self, email):
        self.email = email

class avoidList():
    def __init__(self, ID, name, status, email):
        self.ID = ID
        self.name = name
        self.status = status
        self.email = email

        self.setStatus()

    def getID(self):
        return self.ID
    def getName(self):
        return self.name
    def getStatus(self):
        return self.status
    def getEmail(self):
        return self.email

    def setID(self, ID):
        self.ID = ID
    def setName(self, name):
        self.name = name

    def setStatus(self):
        # get status
        for line in fileinput.input("../Resources/Data/UsersComplaints/usersStatus.txt", inplace=1):
            # get ToUserID status
            if str(self.getID()) in line: # if user is found set status
                self.status = line.split(", ")[1]
            sys.stdout.write(line)

    def setEmail(self, email):
        self.email = email

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        window = manager()
        window.ui.show()

        sys.exit(app.exec_())
