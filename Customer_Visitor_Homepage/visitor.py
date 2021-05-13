
# CSC 322 Project Team X
# registered customer pages
# Chelsea Lantigua my copy file

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox, QPushButton


from PyQt5 import QtCore, QtGui, QtWidgets
from visitorHome import Ui_Homepage


countOrders = 0

        
class visitor:


    def __init__(self):
        self.filepath = os.getcwd()
        self.main_win = QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
#to generate user information like their name
        
        self.generateTopOSHomepage()
        self.generateTopSellersHomepage()

        
#-----homepage navigation bar, home, profile, cart, help
        self.ui.homebutton.clicked.connect(self.show_home_page)
        #hides the OS1cartbuttons
        self.ui.OS1cartbutton1.setHidden(True)
        self.ui.OS1cartbutton2.setHidden(True)
        self.ui.OS1cartbutton3.setHidden(True)
        self.ui.OS1cartbutton4.setHidden(True)
        self.ui.OS1cartbutton5.setHidden(True)
        self.ui.OS1cartbutton6.setHidden(True)
        #hides the OS2cartbuttons
        self.ui.OS2cartbutton1.setHidden(True)
        self.ui.OS2cartbutton2.setHidden(True)
        self.ui.OS2cartbutton3.setHidden(True)
        self.ui.OS2cartbutton4.setHidden(True)
        self.ui.OS2cartbutton5.setHidden(True)
        self.ui.OS2cartbutton6.setHidden(True)
        #hides the OS3cartbuttons
        self.ui.OS3cartbutton1.setHidden(True)
        self.ui.OS3cartbutton2.setHidden(True)
        self.ui.OS3cartbutton3.setHidden(True)
        self.ui.OS3cartbutton4.setHidden(True)
        self.ui.OS3cartbutton5.setHidden(True)
        self.ui.OS3cartbutton6.setHidden(True)
        
        
#        self.ui.cartTableWidget.selectionModel().selectionChanged.connect(self.set_selectedCartItem_info)

#        self.ui.productBuyButton.clicked.connect(self.show_finalize_order_page)

    def show(self):
        self.main_win.show()
        
    def show_home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
            
    def show_OS1_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.shoppage)

    def show_OS2_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.windowspage)
   
    def show_OS3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chromepage)
        
    def show_item_page(self, product):
        self.generateItem(product)
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
       

    # will take the info from the 3 OS pages, search for it and then add it to the cart
    def generateItemInfo4(self, nameUI, priceUI):
        name = nameUI.text()
        price = priceUI.text()
        item = self.searchItem(name, price)
        self.add_to_cart(item)
        
    #generates item on item page
    def generateItem(self, product):
        self.ui.productImage.setIcon(QtGui.QIcon(product.getImage()))
        self.ui.productImage.setIconSize(QtCore.QSize(500, 600))
        self.ui.productName.setText(product.getName())
        self.ui.productName.setStyleSheet("font-size: 50pt;")
        self.ui.productPrice.setText(product.getPrice())
        self.ui.productPrice.setStyleSheet("font-size: 35pt;")
        self.ui.productDescription.setText(product.getDescription())
        self.ui.productDescription.setStyleSheet("font-size: 30pt;")
        self.ui.productRating.setText(str(product.getRate())) #need to add ui objects to just change numerator
        self.ui.productRating.setStyleSheet("font-size: 35pt;")
    
    # will take the first top seller item's name, price, search for it and then add it to the cart
    def generateItemInfo1(self):
        name = self.ui.topsellername1.text()
        price = self.ui.topSellerPrice1.text()
        item = self.searchItem(name, price)
        self.add_to_cart(item)
    # will take the second top seller item's name, price, search for it and then add it to the cart
    def generateItemInfo2(self):
        name = self.ui.topsellername2.text()
        price = self.ui.topSellerPrice2.text()
        item = self.searchItem(name, price)
        self.add_to_cart(item)
    # will take the third top seller item's name, price, search for it and then add it to the cart
    def generateItemInfo3(self):
        name = self.ui.topsellername3.text()
        price = self.ui.topSellerPrice3.text()
        item = self.searchItem(name, price)
        self.add_to_cart(item)
 
 
        
    def showPopUpMessage(self, title, message):
        output = QMessageBox()
        output.setWindowTitle(title)
        output.setText(message)
        x = output.exec_()
    
 
            


#-----will generate the customer my account page based on a users email
    def generateProfileInfo(self):
        search = "al001@gmail.com"
        myfile = open("userInfo.txt", "r")
        lines = myfile.readlines()
        
        for singleLine in lines:
            newline = singleLine.strip()
            userList = newline.split(", ")
            if(userList[0] == search): #if the user is found based on their email then their info will  be displayed on their profile
            
                userEmail = userList[0]
                userName = userList[1]
                userID = userList[2]
                userPaymenCardNumber = userList[3]
                userPaymentBillingAddress = userList[4]
                
                self.ui.myAccountName.setText(userName)
                self.ui.myAccountUserEmail.setText(userEmail)
                self.ui.myAccountUserID.setText(userID)
                self.ui.myAccountUserCardInfo.setText(userPaymenCardNumber)
                self.ui.myAccountUserBillingInfo.setText(userPaymentBillingAddress)
        myfile.close()
   
    #will generate the top os on the homepage
    def generateTopOSHomepage(self):
        osImageButtons = [self.ui.OSimagbutton1, self.ui.OSimagbutton2, self.ui.OSimagbutton3]
        osTitles = [self.ui.OStitle1, self.ui.OStitle2, self.ui.OStitle3]
        osButton = [self.ui.seeProductsButton1, self.ui.seeProductsButton2, self.ui.seeProductsButton3]

        osArray = self.readTopOS()
        index = 0
        for os in osArray: #breaks the list down to lines
            osTitle = os.getName() #refers to the OS Name
            osTitles[index].setText(osTitle)  #sets the OS Name on the homepage

            osImage = os.getImage()  #refers to the OS Image
            osImageButtons[index].setIcon(QtGui.QIcon(osImage))  #sets the OS Image on the homepage
            
            self.generateTopOSPages(osTitle, index) #repeats 3 times for each OS, will find items asscociated to OS to write onto OS page
            index = index + 1
        self.ui.topOSLabel.setStyleSheet("font-size: 30pt; text-align: center;")
        self.ui.topSelleLabel.setStyleSheet("font-size: 30pt; text-align: center;")
    
    #reads from the top OS file and creates OS objects from the attributes
    def readTopOS(self):
        myfile = open("topOperatingSystems.txt", "r")
        osArray = []
        lines = myfile.readlines() #list of lines
        index = 0
        for singleLine in lines: #breaks the list down to lines
            newline = singleLine.strip() #strips the "\n" from the strings line
            os = newline.split(", ") #strips strings by the ", " delimiter 2 elements per line now added to new list
            osArray.append(topOS(os[0], os[1])) #array of item objects #adds the item objects to an array
        return osArray

    def generateTopOSPages(self, osTitle, i): # will take in one OS i value from 0 to 2 and determine from the items in inventory if they match to the OS
    
        osImageButtons = [self.ui.OSimagbutton1, self.ui.OSimagbutton2, self.ui.OSimagbutton3] #array of OS image buttons
        seeProductsButtons = [self.ui.seeProductsButton1, self.ui.seeProductsButton2, self.ui.seeProductsButton3] #array of see products  buttons
        showOSpageFunctions = [self.show_OS1_page, self.show_OS2_page, self.show_OS3_page] #array OS pages
        osPageTitles =  [self.ui.OS1Title, self.ui.OS2Title, self.ui.OS3Title] # array for the titles of the OS pages
        osImageButtons[i].clicked.connect(showOSpageFunctions[i]) #connects the operating system image to it's page
        seeProductsButtons[i].clicked.connect(showOSpageFunctions[i]) #connects the operating system see products button to it's page
        
        
        seeProductsButtons[i].setStyleSheet("QPushButton{\n"
        "    border-radius:15px;\n"
        "    border-top:2px solid #4a89c7;\n"
        "    border-bottom:2px solid #4a89c7;\n"
        "    border-right:2px solid #4a89c7;\n"
        "    border-left:2px solid #4a89c7;\n"
        "    background-color:#4A7FC7;\n"
        "    color:#ffffff;\n"
        "    padding: 5px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    color:#ffffff;\n"
        "    background-color:#84afd9;\n"
        "    border-top:2px solid #84afd9;\n"
        "    border-bottom:2px solid #84afd9;\n"
        "    border-right:2px solid #84afd9;\n"
        "    border-left:2px solid#84afd9;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    color:ffffff;\n"
        "    background-color:#84afd9;\n"
        "    color:#ffffff;\n"
        "    border:none;\n"
        "    border-top:3px solid rgb(178, 84, 84);\n"
        "    border-right:1px solid rgb(178, 84, 84);\n"
        "    border-left:2px solid rgb(178, 84, 84);\n"
        "}")

        
        items = [] #store the items that match to the OS system we are looking at
        position = [] #store the position of the items that match to the OS system we are looking at

        index = 0
        itemsArray = self.readInventoryTextFile()
        index = 0
        for item in itemsArray: #breaks the list down to seperate product objects
            os = item.getOperatingSystem().lower() #refers to OS Type of the product to see if we can find a subset with the name of the operating system file
            if (os == osTitle.lower()): #items are found with the OS type attribute of the item
                items.append(item.getID()) # add the items ID number to a list
                position.append(index)  # add the position of the item to a list
            
            index = index + 1
 
        if i == 0:
            self.generateTopOS1Page(items, position)
        elif i == 1:
            self.generateTopOS2Page(items, position)
        else:
            self.generateTopOS3Page(items, position)
 
        osPageTitles[i].setText(osTitle) #sets the title of the page based on the tile of the OS selected

        return position
 
    #generates top OS 1 page
    def generateTopOS1Page(self, matchedItems, matchedPosition):
        #top OS page ui components
        os1PageImageButton = [self.ui.OS1Image1, self.ui.OS1Image2, self.ui.OS1Image3, self.ui.OS1Image4, self.ui.OS1Image5, self.ui.OS1Image6]  #ui objects for top OS products images
        os1ItemNames = [self.ui.OS1name1, self.ui.OS1name2, self.ui.OS1name3, self.ui.OS1name4, self.ui.OS1name5, self.ui.OS1name6] #ui objects for top OS products names
        os1ItemPrice = [self.ui.OS1price1, self.ui.OS1price2, self.ui.OS1price3, self.ui.OS1price4, self.ui.OS1price5, self.ui.OS1price6] #ui objects for top OS products prices
        addCartButtons = [self.ui.OS1cartbutton1, self.ui.OS1cartbutton2, self.ui.OS1cartbutton3, self.ui.OS1cartbutton4, self.ui.OS1cartbutton5, self.ui.OS1cartbutton6] # add to cart buttons
        self.matchOS(os1ItemNames, os1ItemPrice, os1PageImageButton, matchedItems, matchedPosition, addCartButtons)
        
        
    #generates top OS 2 page
    def generateTopOS2Page(self, matchedItems, matchedPosition):
        
        #top OS page ui components
        os2PageImageButton = [self.ui.OS2Image1, self.ui.OS2Image2, self.ui.OS2Image3, self.ui.OS2Image4, self.ui.OS2Image5, self.ui.OS2Image6]  #ui objects for top OS products images
        os2ItemNames = [self.ui.OS2name1, self.ui.OS2name2, self.ui.OS2name3, self.ui.OS2name4, self.ui.OS2name5, self.ui.OS2name6] #ui objects for top OS products names
        os2ItemPrice = [self.ui.OS2price1, self.ui.OS2price2, self.ui.OS2price3, self.ui.OS2price4, self.ui.OS2price5, self.ui.OS2price6] #ui objects for top OS products prices
        addCartButtons = [self.ui.OS2cartbutton1, self.ui.OS2cartbutton2, self.ui.OS2cartbutton3, self.ui.OS2cartbutton4, self.ui.OS2cartbutton5, self.ui.OS2cartbutton6]
        self.matchOS(os2ItemNames, os2ItemPrice, os2PageImageButton, matchedItems, matchedPosition, addCartButtons)
    

    #generates top OS 3 page
    def generateTopOS3Page(self, matchedItems, matchedPosition):
        #top OS page ui components
        os3PageImageButton = [self.ui.OS3Image1, self.ui.OS3Image2, self.ui.OS3Image3, self.ui.OS3Image4, self.ui.OS3Image5, self.ui.OS3Image6]  #ui objects for top OS products images
        os3ItemNames = [self.ui.OS3name1, self.ui.OS3name2, self.ui.OS3name3, self.ui.OS3name4, self.ui.OS3name5, self.ui.OS3name6]  #ui objects for top OS products names
        os3ItemPrice = [self.ui.OS3price1, self.ui.OS3price2, self.ui.OS3price3, self.ui.OS3price4, self.ui.OS3price5, self.ui.OS3price6]  #ui objects for top OS products prices
        addCartButtons = [self.ui.OS3cartbutton1, self.ui.OS3cartbutton2, self.ui.OS3cartbutton3, self.ui.OS3cartbutton4, self.ui.OS3cartbutton5, self.ui.OS3cartbutton6]
        self.matchOS(os3ItemNames, os3ItemPrice, os3PageImageButton, matchedItems, matchedPosition, addCartButtons)
        


    #will structure the different products based on their OS. Matches the product attributes to the ui components
    def matchOS(self, uiNameArray, uiPriceArray, uiImageArray, matchedItems, matchedPosition, addCartButtons):
           
        itemsArray = self.readInventoryTextFile()
        count = 0 # to repeat the for loop
        #will traverse throught the lines in the array and store the matched items to the associated Operating system
        while count <= len(matchedItems) -1:
            index = matchedPosition[count]
            itemObject = itemsArray[index]

            itemName = itemObject.getName() #refers to the name
            uiNameArray[count].setText(itemName)
            uiNameArray[count].setStyleSheet("font-size: 25pt;")

            itemPrice = itemObject.getPrice() #refers to the price
            uiPriceArray[count].setText(itemPrice) #refers to the price
            uiPriceArray[count].setStyleSheet("font-size: 25pt;")

            itemImage= itemObject.getImage() #refers to the image
            uiImageArray[count].setIcon(QtGui.QIcon(itemImage))
            uiImageArray[count].setIconSize(QtCore.QSize(300, 200))
            
            uiImageArray[count].clicked.connect(lambda x: self.show_item_page(itemObject))
            
            addCartButtons[count].setText("ADD TO CART")
            addCartButtons[count].setStyleSheet("font-size: 13pt;")
            addCartButtons
            
            
            addCartButtons[count].setStyleSheet("QPushButton{\n"
        "    border-radius:15px;\n"
        "    border-top:2px solid #4a89c7;\n"
        "    border-bottom:2px solid #4a89c7;\n"
        "    border-right:2px solid #4a89c7;\n"
        "    border-left:2px solid #4a89c7;\n"
        "    background-color:#4A7FC7;\n"
        "    color:#ffffff;\n"
        "    padding: 5px;\n"
        "}\n"
        "QPushButton:hover{\n"
        "    color:#ffffff;\n"
        "    background-color:#84afd9;\n"
        "    border-top:2px solid #84afd9;\n"
        "    border-bottom:2px solid #84afd9;\n"
        "    border-right:2px solid #84afd9;\n"
        "    border-left:2px solid#84afd9;\n"
        "}\n"
        "QPushButton:pressed{\n"
        "    color:ffffff;\n"
        "    background-color:#84afd9;\n"
        "    color:#ffffff;\n"
        "    border:none;\n"
        "    border-top:3px solid rgb(178, 84, 84);\n"
        "    border-right:1px solid rgb(178, 84, 84);\n"
        "    border-left:2px solid rgb(178, 84, 84);\n"
        "}")
                    
            count = count + 1

    #will generate the top sellers on the homepage by looking into the topSeller.txt, creates objects of the items
    def readTopSellers(self):
        myfile = open("topSeller.txt", "r")
        topSellerArray = []
        lines = myfile.readlines() #list of lines
        
        for singleLine in lines: #breaks the list down to lines should just be one line of 3 product IDs seperated by commas
            newline = singleLine.strip() #strips the "\n" from the strings line
            topSellerItems = newline.split(", ") #strips strings by the ", " delimoiter 2 elements per line now added to new list
            
            topSellerArray.append(topSeller(topSellerItems[0])) #adds first top seller to array of top seller objects
            topSellerArray.append(topSeller(topSellerItems[1])) #adds second top seller to array of top seller objects
            topSellerArray.append(topSeller(topSellerItems[2])) #adds third top seller to array of top seller objects
            
        return topSellerArray
        
    #will generate the top sellers information
    def generateTopSellersHomepage(self):
        topSellerArray = self.readTopSellers()
        i = 0
        for item in topSellerArray:
            self.generateTopSellersItems(item.getID(), i) #the first top seller ID sent to function generateTopSellersItems
            i += 1

    # will generate the pages of the top sellers based on their position on the textfile determined by value of i
    def generateTopSellersItems(self, itemID, i):

        itemsArray = self.readInventoryTextFile()
        index = 0
        for item in itemsArray: #breaks the list down to seperate product objects
            if (item.getID() == itemID): #checks if the product object we are looking at is a top sellers item
                if i == 0:
                    self.generateTopSeller1Page(item)
                elif i == 1:
                    self.generateTopSeller2Page(item)
                else:
                    self.generateTopSeller3Page(item)
                    
                break;
                        
            index = index + 1
               
    #will record the first top seller product information to write on the homepage
    def generateTopSeller1Page(self, item):
        self.matchTopSeller(item, self.ui.topsellername1,  self.ui.topSellerPrice1, self.ui.topSellerImage1)
        ##-----homepage top seller button leads to cart page through the generateItemInfo1 function
        self.ui.topsellerbutton1.setHidden(True)
                


    #will record the second top seller product information to write on the homepage
    def generateTopSeller2Page(self, item):
        self.matchTopSeller(item, self.ui.topsellername2, self.ui.topSellerPrice2, self.ui.topSellerImage2)
        ##-----homepage top seller button leads to cart page through the generateItemInfo2 function
        self.ui.topsellerbutton2.setHidden(True)
        
                


    #will record the third top seller product information to write on the homepage
    def generateTopSeller3Page(self, item):
        self.matchTopSeller(item, self.ui.topsellername3, self.ui.topSellerPrice3, self.ui.topSellerImage3)
        ##-----homepage top seller button leads to cart page through the generateItemInfo3 function
        self.ui.topsellerbutton3.setHidden(True)

      
                

        
    def matchTopSeller(self, item, uiName, uiPrice, uiImage):
        itemName = item.getName() #refers to product name
        uiName.setText(itemName)
        uiName.setStyleSheet("font-size: 25pt;")


        itemPrice = item.getPrice() #refers to product price
        uiPrice.setText(itemPrice)
        uiPrice.setStyleSheet("font-size: 25pt;")


        itemImage= item.getImage() #refers to product image
        uiImage.setIcon(QtGui.QIcon(itemImage))

        #-----homepage top seller image button leads to item page
        uiImage.clicked.connect(lambda x: self.show_item_page(item))
        
        
#will read the inventory textfile and create an array of product objects
    def readInventoryTextFile(self):
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        index = 0
        itemArray = [] #to store the item objects
        for singleLine in lines: #breaks the list down to lines
            newline = singleLine.strip() #strips the "\n" from the strings line
            item = newline.split(", ") #strips strings by the ", " deliminter 6 elements per line now added to new list
#            del item[0]
            itemArray.append(product(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])) #array of item objects #adds the item objects to an array
            index = index + 1
        myfile.close()
        return itemArray


        
#    def writeToInventoryTexfile(self, product, userID):
#        file = userID + "cart.txt"
#        itemsArray = self.readInventoryTextFile()
#
#        #opens the cart file to read
#        myfile = open(file, "r+")
#        lines = myfile.readlines()
#        i = 0
#        count = 0
#        index = -1
#        for singleLine in lines:
#            newline = singleLine.strip()
#            userList = newline.split(", ")
#
#            ID = userList[1]
#            quantity = userList[2]
#
#            #checks if the item is already in the file
#            if ID == product.getID():
#                count += 1
#                index = i
#            i += 1
#        myfile.close()
#
#        #opens the cart file to write attributes seperated by a comma
#        myfile = open(file, "a+")
#        myfile.write(product.getName())
#        myfile.write(", ")
#        myfile.write(product.getID())
#        myfile.write(", ")
#        myfile.write(str(1)) #quantity will equal 1
#        myfile.write(", ")
#        num = int(product.getPrice().replace("$", ""))
#        total = num * (1) #stores the total
#        myfile.write(str(total))
#        myfile.write("\n")
#
#        myfile.close()
#        return file
        
        
        
        
class product:
    def __init__(self, name, ID, price, description, image, OS, itemsSold, quantity):
        self.name = name
        self.ID = ID
        self.price = price
        self.description = description
        self.image = image
        self.OS = OS
        self.itemsSold = itemsSold
        self.quantity = quantity
        self.rate = 0
        self.totalRatingSum = 0
    
    def getName(self):
        return self.name
    def getID(self):
        return(self.ID)
    def getPrice(self):
        return self.price
    def getDescription(self):
        return self.description
    def getImage(self):
        return self.image
    def getOperatingSystem(self):
        return self.OS
    def getItemSold(self):
        return self.itemsSold
    def getQuantity(self):
        return self.quantity
    def getRate(self):
        return self.rate
    def getTotalRatingSum(self):
        return self.totalRatingSum
        
    def setName(self, name):
        self.name = name
    def setID(self, ID):
        self.ID = ID
    def setPrice(self, price):
        self.price = price
    def setDescription(self, description):
        self.description = description
    def setImage(self, image):
        self.image = image
    def setOS(self, OS):
        self.OS = OS
    def setItemSold(self, itemsSold):
        self.itemsSold = itemsSold
    def setQuantity(self, quantity):
        self.quantity = quantity
    def setRate(self, totalRatingSum, itemsSold):
        self.rate = totalRatingSum/itemsSold
    def setTotalRatingSum(self, totalRatingSum):
        self.totalRatingSum = totalRatingSum
      
class topSeller:
    def __init__(self, ID):
        self.ID = ID
        
    def getID(self):
        return(self.ID)
        
class topOS:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def getName(self):
        return(self.name)
    def getImage(self):
        return self.image

    def setName(self, name):
        self.name = name
    def setImage(self, image):
        self.image = image

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = visitor()
    main_win.show()

    sys.exit(app.exec_())
    
