# CSC 322 Project Team X
# registered customer pages
# Chelsea Lantigua

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from customerHome import Ui_Homepage


class registered:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
#to generate user information like their name
        self.generateUserName()
        self.generateTopOSHomepage()
        self.generateTopSellersHomepage()
    

#-----homepage navigation bar, home, profile, cart, help
        self.ui.homebutton.clicked.connect(self.show_home_page)
        self.ui.profilebutton.clicked.connect(self.show_profile_page)
        self.ui.helpButton.clicked.connect(self.show_help_page)
        self.ui.cartbutton.clicked.connect(self.show_cart_page)

#-----homepage top seller button leads to cart page
        self.ui.topsellerbutton1.clicked.connect(self.show_cart_page)
        self.ui.topsellerbutton2.clicked.connect(self.show_cart_page)
        self.ui.topsellerbutton3.clicked.connect(self.show_cart_page)
        
#-----homepage top seller image button leads to item page
        self.ui.topSellerImage1.clicked.connect(self.show_item_page)
        self.ui.topSellerImage2.clicked.connect(self.show_item_page)
        self.ui.topSellerImage3.clicked.connect(self.show_item_page)

#----users can go onto the item page and add to their cart
        self.ui.productCartButton.clicked.connect(self.add_to_cart)
        
#----users can go onto the item page and buy the item
        self.ui.productBuyButton.clicked.connect(self.buy_item)
        
        

#-------------profilepage relationships using stackedWidget2 -------------

#-----navigation bar on profile page
        self.ui.profileOrdersButton.clicked.connect(self.show_profile_orders_page)
        self.ui.profilePaymentButton.clicked.connect(self.show_profile_payment_page)
        self.ui.profileComplaintsButton.clicked.connect(self.show_profile_complaints_page)
        self.ui.profileWarningsButton.clicked.connect(self.show_profile_warnings_page)
        self.ui.profileMyAccountButton.clicked.connect(self.show_myAccount_page)
    
 
 #-----profilepage relationships customer can use complain buttons on orders page to connect to make complain page about clerk

        self.ui.profilePageStoreClerk1ComplainButton.clicked.connect(self.make_complaints_page)
        self.ui.profilePageStoreClerk2ComplainButton.clicked.connect(self.make_complaints_page)
       
 #-----profilepage relationships customer can use complain buttons on orders page to connect to make complain page about delivery companies
 
        self.ui.profilePageDeliveryCompany1ComplainButton.clicked.connect(self.make_complaints_page)
        self.ui.profilePageDeliveryCompany2ComplainButton.clicked.connect(self.make_complaints_page)
        
#----users can respond to complaints they have made
        self.ui.userComplaintLeaveMessageButton.clicked.connect(self.respond_complaints_page)

#----users can respond to complaints made against them
        self.ui.theComplaintLeaveMessageButton.clicked.connect(self.respond_complaints_page)

#--users will have to finalize order when they press buy, this button will lead them to their order page
        self.ui.submitFinalizeOrderbutton.clicked.connect(self.show_profile_page)

#--users will have to finalize order when they press place order on their cart page or buy on an item page
        self.ui.placeorderbutton.clicked.connect(self.show_finalize_order_page)
        self.ui.productBuyButton.clicked.connect(self.show_finalize_order_page)



    def show(self):
        self.main_win.show()
        
    def show_home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
            
    def show_profile_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.profilepage)

    def show_help_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chatpage)

    def show_cart_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage)
    
    def show_OS1_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.shoppage)

    def show_OS2_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.windowspage)
   
    def show_OS3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chromepage)
        
    def show_topSeller_image1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
    def show_topSeller_image2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
    def show_topSeller_image3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
    def show_item_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
    
    def add_to_cart(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage)
    
    def buy_item(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage)

    def show_finalize_order_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.finalizeOrderpage)

    def show_profile_orders_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.orderspage)
    
    def show_profile_payment_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.paymentpage)
    
    def show_profile_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.complaintspage)
    
    def show_profile_warnings_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.warningspage)

    def make_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.makeComplaintpage)
    
    def show_myAccount_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.myAccountPage)
        
    def respond_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.respondToComplaintpage)
        
    def show_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.complaintspage)
    
   
        

#-----will generate the customer my account page based on a users email
    def generateUserName(self):
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
        myfile = open("topOperatingSystems.txt", "r")
        
        osImageButtons = [self.ui.OSimagbutton1, self.ui.OSimagbutton2, self.ui.OSimagbutton3]
        osTitles = [self.ui.OStitle1, self.ui.OStitle2, self.ui.OStitle3]
        osButton = [self.ui.seeProductsButton1, self.ui.seeProductsButton2, self.ui.seeProductsButton3]

        lines = myfile.readlines() #list of lines
        index = 0
        for singleLine in lines: #breaks the list down to lines
            newline = singleLine.strip() #strips the "\n" from the strings line
            userList = newline.split(", ") #strips strings by the ", " deliminter 2 elements per line now added to new list
            
            osTitle = userList[0] #refers to the OS Name
            osTitles[index].setText(osTitle)  #sets the OS Name on the homepage

            osImage = userList[1]  #refers to the OS Image
            osImageButtons[index].setIcon(QtGui.QIcon(osImage))  #sets the OS Image on the homepage
            
            self.generateTopOSPages(osTitle, index) #repeats 3 times for each OS, will find items asscociated to OS to write onto OS page
            index = index + 1
        myfile.close()
    
   
        
    # function will take in one OS i value from 0 to 2 and determine from the items in inventory if they match to the OS
    def generateTopOSPages(self, osTitle, i):
    
        osImageButtons = [self.ui.OSimagbutton1, self.ui.OSimagbutton2, self.ui.OSimagbutton3] #array of OS image buttons
        seeProductsButtons = [self.ui.seeProductsButton1, self.ui.seeProductsButton2, self.ui.seeProductsButton3] #array of see products  buttons
        showOSpageFunctions = [self.show_OS1_page, self.show_OS2_page, self.show_OS3_page] #array OS pages
        osPageTitles =  [self.ui.OS1Title, self.ui.OS2Title, self.ui.OS3Title] # array for the titles of the OS pages
      
        osImageButtons[i].clicked.connect(showOSpageFunctions[i]) #connects the operating system image to it's page
        seeProductsButtons[i].clicked.connect(showOSpageFunctions[i]) #connects the operating system see products button to it's page
        itemsArray = [] # will store the items matched to an OS
        position = [] # will store the index value of the matched items contained in itemsArray
        
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        index = 0
        for singleLine in lines: #breaks the list down to lines
            newline = singleLine.strip() #strips the "\n" from the strings line
            item = newline.split(", ") #strips strings by the ", " delimiter 6 elements per line now added to new list
            os = item[5].lower() #refers to OS Type of the product to see if we can find a subset with the name of the operating system file
            if (os == osTitle.lower()): #items are found with the OS type attribute of the item
                itemsArray.append(item[1]) # add the items ID number to a list
                position.append(index)
            index = index + 1

        if i == 0:
            self.generateTopOS1Page(itemsArray, position, index)
        elif i == 1:
            self.generateTopOS2Page(itemsArray, position, index)
        else:
            self.generateTopOS3Page(itemsArray, position, index)

        osPageTitles[i].setText(osTitle) #sets the title of the page based on the tile of the OS selected
        myfile.close()
        return position

    #generates top OS 1 page
    def generateTopOS1Page(self, matchedItems, matchedPosition, totalItems):

        os1PageImageButton = [self.ui.OS1Image1, self.ui.OS1Image2, self.ui.OS1Image3, self.ui.OS1Image4, self.ui.OS1Image5, self.ui.OS1Image6]  #ui objects for top OS products images
        os1ItemNames = [self.ui.OS1name1, self.ui.OS1name2, self.ui.OS1name3, self.ui.OS1name4, self.ui.OS1name5, self.ui.OS1name6] #ui objects for top OS products names
        os1ItemPrice = [self.ui.OS1price1, self.ui.OS1price2, self.ui.OS1price3, self.ui.OS1price4, self.ui.OS1price5, self.ui.OS1price6] #ui objects for top OS products prices

        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        count = 0 # to repeat the for loop
        # will traverse through the lines in the textfile and store the matched items to the associated Operating system
        while count <= len(matchedItems) -1:
            index = matchedPosition[count]
            newline = lines[index].strip()
            item = newline.split(", ")
            
            itemName = item[0] #refers to the name
            os1ItemNames[count].setText(itemName)
            os1ItemNames[count].setStyleSheet("font-size: 25pt;")


            itemPrice = item[2] #refers to the price
            os1ItemPrice[count].setText(itemPrice)
            os1ItemPrice[count].setStyleSheet("font-size: 25pt;")


            itemImage= item[4] #refers to the image
            os1PageImageButton[count].setIcon(QtGui.QIcon(itemImage))
            os1PageImageButton[count].setIconSize(QtCore.QSize(300, 200))

            count = count + 1

        myfile.close()
    
    
    #generates top OS 2 page
    def generateTopOS2Page(self, matchedItems, matchedPosition, totalItems):
            
        os2PageImageButton = [self.ui.OS2Image1, self.ui.OS2Image2, self.ui.OS2Image3, self.ui.OS2Image4, self.ui.OS2Image5, self.ui.OS2Image6]  #ui objects for top OS products images
        os2ItemNames = [self.ui.OS2name1, self.ui.OS2name2, self.ui.OS2name3, self.ui.OS2name4, self.ui.OS2name5, self.ui.OS2name6] #ui objects for top OS products names
        os2ItemPrice = [self.ui.OS2price1, self.ui.OS2price2, self.ui.OS2price3, self.ui.OS2price4, self.ui.OS2price5, self.ui.OS2price6] #ui objects for top OS products prices

        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        count = 0 # to repeat the for loop
        # will traverse throught the lines in the textfile and store the matched items to the associated Operating system
        while count <= len(matchedItems) -1:
            index = matchedPosition[count]
            newline = lines[index].strip()
            item = newline.split(", ")
            
            itemName = item[0] #refers to the name
            os2ItemNames[count].setText(itemName)
            os2ItemNames[count].setStyleSheet("font-size: 25pt;")

            itemPrice = item[2] #refers to the price
            os2ItemPrice[count].setText(itemPrice) #refers to the price
            os2ItemPrice[count].setStyleSheet("font-size: 25pt;")

            itemImage= item[4] #refers to the image
            os2PageImageButton[count].setIcon(QtGui.QIcon(itemImage))
            os2PageImageButton[count].setIconSize(QtCore.QSize(300, 200))

            count = count + 1

        myfile.close()
        
    #generates top OS 3 page
    def generateTopOS3Page(self, matchedItems, matchedPosition, totalItems):
          
        os3PageImageButton = [self.ui.OS3Image1, self.ui.OS3Image2, self.ui.OS3Image3, self.ui.OS3Image4, self.ui.OS3Image5, self.ui.OS3Image6]  #ui objects for top OS products images
        os3ItemNames = [self.ui.OS3name1, self.ui.OS3name2, self.ui.OS3name3, self.ui.OS3name4, self.ui.OS3name5, self.ui.OS3name6]  #ui objects for top OS products names
        os3ItemPrice = [self.ui.OS3price1, self.ui.OS3price2, self.ui.OS3price3, self.ui.OS3price4, self.ui.OS3price5, self.ui.OS3price6]  #ui objects for top OS products prices

        # will traverse throught the lines in the textfile and store the matched items to the associated Operating system
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        count = 0 # to repeat the for loop
        while count <= len(matchedItems) -1:
            index = matchedPosition[count]
            newline = lines[index].strip()
            item = newline.split(", ")
            
            itemName = item[0] #refers to the name
            os3ItemNames[count].setText(itemName)
            os3ItemNames[count].setStyleSheet("font-size: 25pt;")


            itemPrice = item[2] #refers to the price
            os3ItemPrice[count].setText(itemPrice)
            os3ItemPrice[count].setStyleSheet("font-size: 25pt;")


            itemImage= item[4] #refers to the image
            os3PageImageButton[count].setIcon(QtGui.QIcon(itemImage))
            os3PageImageButton[count].setIconSize(QtCore.QSize(300, 200))

            count = count + 1

        myfile.close()


    #will generate the top sellers on the homepage by looking into the topSeller.txt
    def generateTopSellersHomepage(self):
        myfile = open("topSeller.txt", "r")
        lines = myfile.readlines() #list of lines
        index = 0
        for singleLine in lines: #breaks the list down to lines should just be one line of 3 product IDs seperated by commas
            newline = singleLine.strip() #strips the "\n" from the strings line
            topSellerItems = newline.split(", ") #strips strings by the ", " delimoiter 2 elements per line now added to new list
            
            self.generateTopSellersItems(topSellerItems[0], 0) #the first top seller ID sent to function generateTopSellersItems
            self.generateTopSellersItems(topSellerItems[1], 1) #the second top seller ID sent to function generateTopSellersItems
            self.generateTopSellersItems(topSellerItems[2], 2) #the third top seller ID sent to function generateTopSellersItems
            
        myfile.close()

    #will read the first top sellers information from the inventory.txt textfile to write on the homepage
    def generateTopSellersItems(self, itemID, i):
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        index = 0
        for singleLine in lines: #breaks the list down to lines
            newline = singleLine.strip() #strips the "\n" from the strings line
            item = newline.split(", ") #strips strings by the ", " delimiter 6 elements per line now added to new list
           
            if (item[1] == itemID): #2nd attribute in inventory.txt is product ID
                if i == 0:
                    self.generateTopSeller1Page(index) #takes in the parameter index to determine which row to look at within the inventory text file
                elif i == 1:
                    self.generateTopSeller2Page(index)
                else:
                    self.generateTopSeller3Page(index)
                    
                break;
                        
            index = index + 1
        myfile.close()
               
    #will read the first top seller product information from the inventory.txt textfile to write on the homepage
    def generateTopSeller1Page(self, index):
    
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        elements =  lines[index].strip().split(", ") #refers to specific line of the textfile with the product information

        itemName = elements[0] #refers to product name
        self.ui.topsellername1.setText(itemName)
        self.ui.topsellername1.setStyleSheet("font-size: 25pt;")


        itemPrice = elements[2] #refers to product price
        self.ui.topSellerPrice1.setText(itemPrice)
        self.ui.topSellerPrice1.setStyleSheet("font-size: 25pt;")


        itemImage= elements[4] #refers to product image
        self.ui.topSellerImage1.setIcon(QtGui.QIcon(itemImage))

        myfile.close()

    #will read the second top seller product information from the inventory.txt textfile to write on the homepage
    def generateTopSeller2Page(self, index):
    
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        elements =  lines[index].strip().split(", ") #refers to specific line of the textfile with the product information, elements in the row placed in list called elements

        itemName = elements[0] #refers to product name
        self.ui.topsellername2.setText(itemName)
        self.ui.topsellername2.setStyleSheet("font-size: 25pt;")


        itemPrice = elements[2]  #refers to product price
        self.ui.topSellerPrice2.setText(itemPrice)
        self.ui.topSellerPrice2.setStyleSheet("font-size: 25pt;")


        itemImage= elements[4]  #refers to product image
        self.ui.topSellerImage2.setIcon(QtGui.QIcon(itemImage))

        myfile.close()

   
    #will read the third top seller product information from the inventory.txt textfile to write on the homepage
    def generateTopSeller3Page(self, index):
        myfile = open("inventory.txt", "r")
        lines = myfile.readlines() #list of lines
        elements =  lines[index].strip().split(", ") ##refers to specific line of the textfile with the product information, elements in the row placed in list called elements

        itemName = elements[0] #refers to product name
        self.ui.topsellername3.setText(itemName)
        self.ui.topsellername3.setStyleSheet("font-size: 25pt;")

        itemPrice = elements[2] #refers to product price
        self.ui.topSellerPrice3.setText(itemPrice)
        self.ui.topSellerPrice3.setStyleSheet("font-size: 25pt;")

        itemImage= elements[4] #refers to product image
        self.ui.topSellerImage3.setIcon(QtGui.QIcon(itemImage))
        myfile.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = registered()
    main_win.show()

    sys.exit(app.exec_())
    
