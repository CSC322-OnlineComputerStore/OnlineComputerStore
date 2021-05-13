# CSC 322 Project Team X
# registered customer pages
# Chelsea Lantigua

import sys
import os
import datetime

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox, QPushButton


from PyQt5 import QtCore, QtGui, QtWidgets
from customerHome import Ui_Homepage
        
class registered:
    def __init__(self):
        self.filepath = os.getcwd()
        self.main_win = QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
#to generate user information like their name
        self.generateProfileInfo()
        self.generateTopOSHomepage()
        self.generateTopSellersHomepage()
        self.readInventoryTextFile()
        
#-----homepage navigation bar, home, profile, cart, help
        self.ui.homebutton.clicked.connect(self.show_home_page)
        self.ui.profilebutton.clicked.connect(self.show_profile_page)
        self.ui.helpButton.clicked.connect(self.show_help_page)
        self.ui.cartbutton.clicked.connect(self.show_cart_page)

        
#-------------profilepage relationships using stackedWidget2 -------------

#-----navigation bar on profile page
        self.ui.profileOrdersButton.clicked.connect(self.show_profile_orders_page)
        self.ui.profilePaymentButton.clicked.connect(self.show_profile_payment_page)
        self.ui.profileComplaintsButton.clicked.connect(self.show_profile_complaints_page)
        self.ui.profileWarningsButton.clicked.connect(self.show_profile_warnings_page)
        self.ui.profileMyAccountButton.clicked.connect(self.show_myAccount_page)
    
 #-----profilepage relationships customer can use complain buttons on orders page to connect to make complain page about clerk

        self.ui.profilePageStoreClerk1ComplainButton.clicked.connect(self.make_complaints_page)
       
 #-----profilepage relationships customer can use complain buttons on orders page to connect to make complain page about delivery companies
 
        self.ui.profilePageDeliveryCompany1ComplainButton.clicked.connect(self.make_complaints_page)
#        self.ui.profilePageDeliveryCompany2ComplainButton.clicked.connect(self.make_complaints_page)
        
#----users can respond to complaints they have made
        self.ui.userComplaintLeaveMessageButton.clicked.connect(self.respond_complaints_page)

#----users can respond to complaints made against them
        self.ui.theComplaintLeaveMessageButton.clicked.connect(self.respond_complaints_page)
        self.userID = "12345"
      
        
        self.folderPath = "../StoreClerk_DeliveryCompany_Dashboard/all_users/all_clerks/"
        self.cartTextfile = "../StoreClerk_DeliveryCompany_Dashboard/all_users/all_customers/"
            

#        self.cartTextfile = self.folderPath + 'cart.txt' # the path for the user's cart
        self.messagesNumber = 0 # sets the number of conversations between a user and store clerk
        self.ordersNumber = 0 #sets the number of orders a user has
        self.num = 0 # number of conversations
        #--users will have to finalize order when they press buy, after they finalize they will be taken to the profile page
        self.ui.submitFinalizeOrderbutton.clicked.connect(self.show_profile_page)
    
        self.ui.chatHistoryButton.clicked.connect(self.showMessagesPage)
        
        self.ui.conversationWidgetTable.selectionModel().selectionChanged.connect(self.set_selectedConversation)

        self.ui.chatSendButton.clicked.connect(self.createNewConversation)
        
        #--users will have to finalize order when they press buy, this button will lead them to update their orders page
#        self.ui.submitFinalizeOrderbutton.clicked.connect(lambda x: self.clearCart(self.file))
        
        
        self.ui.submitFinalizeOrderbutton.clicked.connect(self.newOrder)
        self.ui.ordersTableWidget.selectionModel().selectionChanged.connect(self.set_selectedOrder)
       
        # cart table dimensions
        self.ui.cartTableWidget.setColumnWidth(0, 280)
        self.ui.cartTableWidget.setColumnWidth(1, 280)
        self.ui.cartTableWidget.setColumnWidth(2, 280)
        self.ui.cartTableWidget.setColumnWidth(3, 280)
        
        #message table dimensions
        self.ui.messageTableWidget.setColumnWidth(0, 70)
        self.ui.messageTableWidget.setColumnWidth(1, 280)
        self.ui.messageTableWidget.setColumnWidth(2, 70)
        self.ui.messageTableWidget.setColumnWidth(3, 280)
        self.ui.messageTableWidget.setColumnWidth(4, 70)

        #message list dimension
        self.ui.conversationWidgetTable.setColumnWidth(0,200)
        self.ui.conversationWidgetTable.horizontalHeader().setStretchLastSection(True)

        #to send a message
        self.ui.sendButton.clicked.connect(self.newmessage_set)
        
        self.userWarnings = 0
        self.userStatus = "Active"
        self.storeClerkID = 0
        self.complaintNumber = 0

    def show(self):
        self.main_win.show()
        
    def show_home_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
            
    def show_profile_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.profilepage)
   


#------------------------code for the chat box to chat with a store clerk -----------------
# leads a user to the chat box to write the message box
    def show_help_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chatpage)
  
  #will create a new conversation with a different textfile
    def createNewConversation(self):
        usersPathName = self.folderPath + str(self.userID) + "conversation" +str(self.messagesNumber) + "message" + str(self.num)
#        if(os.path.exists(usersPathName) == 0): #if the file does not exists then
#            dir = "conversations/"
#            parent = self.folderPath
#            path = os.path.join(parent, dir)
#            os.mkdir(path)
#        self.userPathName = usersPathName + str(self.messagesNumber) + ".txt"
#
        text = str(self.ui.chatbox.toPlainText())
        
        if len(text) == 0:
            self.showPopUpMessage("Error", "Error, no message has been entered")
        else:
            myfile = open(self.userPathName, "w+")
            myfile.write("customer\n" + text + "\n")
            myfile.close()
      
            self.showPopUpMessage("Your message has been sent to a store clerk", "Your message has been sent to a store clerk, conversation #" + str(self.messagesNumber))
            
            self.messagesNumber += 1 #increment the number of messages every time a customer selects the help button. A new conversation will be made

            #wont automatically go to messages page will have to go to profile page
            self.ui.chatbox.clear()
        
            self.message_set()
            self.ui.chatbox.clear()
            self.ui.stackedWidget.setCurrentWidget(self.ui.profilepage)
        return list

    def showMessagesPage(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.messagesPage) #will direct user to the page which will be updated with the messages

    #when the message page button is pressed display all messages from a specific conversation
    def message_set(self):
        if self.messagesNumber > 0: # if there is at least one conversation already taking place then read the file and set the message and conversation tables
            self.get_messages(self.userPathName) # sets the message on the table
            self.set_messagelist(self.userPathName) # sets the conversation number on the left table
            
    def newmessage_set(self):
        self.set_message(self.userPathName) #will rewrite the message file with the users new message
        self.num += 1
    
            
    #will select a row on the conversations list to view all messages
    def set_selectedConversation(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
            column = 0

        self.selectedConversation= self.ui.conversationWidgetTable.item(row,column).text()
        self.userPathName = self.folderPath + "/conversations/" +self.selectedConversation + ".txt"
        self.folderPath + str(self.userID) + "conversation" +str(self.messagesNumber) + "message" +str(self.num)
        self.get_messages(self.userPathName)
        

    #will set the messages table by reading the textfile
    def get_messages(self,filename):
        l=[]
        k=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
        l=lines
        for i in range(len(l)):
            l[i]=l[i].replace('\n','')
        self.ui.messageTableWidget.setRowCount(int(len(l)/2))
        self.ui.messageTableWidget.setColumnCount(5)
        for i in range(len(l)-1):
            if (l[i]=='clerk'):
                item1 = QtWidgets.QTableWidgetItem('Clerk #00000')
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QtWidgets.QTableWidgetItem(l[i+1])
                item2.setTextAlignment(QtCore.Qt.AlignLeft)
                item2.setTextAlignment(QtCore.Qt.AlignVCenter)
                self.ui.messageTableWidget.setItem(i/2,0,item1)
                self.ui.messageTableWidget.item(i/2, 0).setForeground(QtGui.QColor(177,177,177))
                self.ui.messageTableWidget.setItem(i/2,1,item2)
                self.ui.messageTableWidget.item(i/2, 1).setBackground(QtGui.QColor(233,211,202))
                self.ui.messageTableWidget.item(i/2, 1).setForeground(QtGui.QColor(177,177,177))

            elif (l[i]=='customer'):
                item1 = QtWidgets.QTableWidgetItem('You')
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item2 = QtWidgets.QTableWidgetItem(l[i+1])
                item2.setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
                self.ui.messageTableWidget.setItem(int(i/2),int(3),item2)
                self.ui.messageTableWidget.item(int(i/2), int(3)).setBackground(QtGui.QColor(int(255),int(255),int(255)))
                self.ui.messageTableWidget.item(int(i/2), int(3)).setForeground(QtGui.QColor(177,177,177))
                self.ui.messageTableWidget.setItem(int(i/2),int(4),item1)
                self.ui.messageTableWidget.item(int(i/2), int(4)).setForeground(QtGui.QColor(177,177,177))

    def set_message(self,filename):
        l=[]
        k=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        message = self.ui.messagesInputBox.toPlainText()
        for i in range(len(l)):
            if (i==(len(l)-1)):
                l[i]+='\n'
        l.append('customer\n')
        l.append(message)
        with open(filename,"w") as file:
            file.writelines(l)
            file.close()
        self.ui.messagesInputBox.clear()
        self.get_messages(filename)
        
        return filename


    def set_messagelist(self,filename):
        rowNum = self.ui.conversationWidgetTable.rowCount()
        self.ui.conversationWidgetTable.insertRow(rowNum)
        item1 = QtWidgets.QTableWidgetItem(str(self.messagesNumber -1))
#            item2 = QtWidgets.QTableWidgetItem(l[i][1])
        self.ui.conversationWidgetTable.setItem(rowNum,0,item1)
#            self.ui.message_list.setItem(i,1,item2)



    def return_customer_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        return l
        
#------------------------code to write the users orders and display them in a table--------------------
     
  
    def newOrder(self):
#        orderPath = self.folderPath+ str(self.userID) + str(self.ordersNumber)
#        clerkspathName = self.filepath+'/folders/all_users/all_clerks/00000/chat' + self.userID + '/'
#
#        if(os.path.exists(orderPath) == 0): #if the file does not exists then
#            dir = "orders/"
#            parent = self.folderPath
#            path = os.path.join(parent, dir)
#            os.mkdir(path)
        
        self.orderPath = self.folderPath + str(self.userID) + "Order" + str(self.ordersNumber) + ".txt"
        
        myfile = open(self.orderPath, "w+")
        myfile.write(str(self.ordersNumber) + "\n" + str(self.userID)+ "\n" + str(datetime.datetime.now()) + "\n" + "Pending\nto be set\nShipping Address\nStore Clerks that handled the order\nDelivery Companies that are delivering the items\n")
    
        myfile.close()
        self.clearCart(self.file)
        
        self.ordersNumber += 1 #increment the number of messages every time a customer selects the help button. A new conversation will be made
        lines = self.readOrderInfo(self.orderPath) # writes the order to the table
        self.set_productlist(lines) # sets the order details on the right table
        return self.orderPath
        
        
    #will read the order information from the textfile
    def readOrderInfo(self, file):
        with open(file, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        for i in range(len(l)):
            l[i]=l[i].replace('\n','')
            
        self.ui.ordersTableWidget.setColumnCount(7) # table have 7 columns
        self.ui.ordersTableWidget.setRowCount(self.ordersNumber) # table has rows dependent on number of orders
        rowNum = self.ui.ordersTableWidget.rowCount()
        self.ui.conversationWidgetTable.insertRow(rowNum) # adds a row
    
        item1 = QtWidgets.QTableWidgetItem(str(l[0]))  #order number
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,0,item1)
        
        item1 = QtWidgets.QTableWidgetItem(str(l[3]))  #status
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,2,item1)
        
        item1 = QtWidgets.QTableWidgetItem(str(l[4]))  #tracking number
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,3,item1)
        
        item1 = QtWidgets.QTableWidgetItem(str(l[2]))  #date
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,4,item1)
        
        item1 = QtWidgets.QTableWidgetItem(str(l[6]))  #clerk
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,5,item1)
        
        item1 = QtWidgets.QTableWidgetItem(str(l[7]))  #delivery company
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,6,item1)
        
        totalPrice = 0
        
        for item in l[8:]: # will travers items in l array  at and after index 8 because these will be the products. The product are in the format of lines seperated by commas for their attributes name ID Quantity and price
            newlist = item.split(", ")
            totalPrice += int(newlist[3]) # all the different prices will be added to compute total
            
        item1 = QtWidgets.QTableWidgetItem(str(totalPrice))  #total price
        item1.setTextAlignment(QtCore.Qt.AlignLeft)
        self.ui.ordersTableWidget.setItem(self.ordersNumber-1,1,item1)
        
        return l
        
    def set_productlist(self, lines):
    
        clerk = str(lines[6])
        delivery = str(lines[7])
        count = 0
        for item in lines[8:]: # will traverse items in l array  at and after index 8 because these will be the products. The product are in the format of lines seperated by commas for their attributes name ID Quantity and price
            
            newlist = item.split(", ")
            id = str(newlist[1]) # product ID
            name = str(newlist[0]) # name
            quantity = str(newlist[2]) ##quantity


            rowNum = self.ui.OrderSpecificsTableWidget.rowCount()
            self.ui.OrderSpecificsTableWidget.insertRow(rowNum)
            item1 = QtWidgets.QTableWidgetItem(id)
            self.ui.OrderSpecificsTableWidget.setItem(count,0,item1)
            item2 = QtWidgets.QTableWidgetItem(name)
            self.ui.OrderSpecificsTableWidget.setItem(count,1,item2)
            item3 = QtWidgets.QTableWidgetItem(quantity)
            self.ui.OrderSpecificsTableWidget.setItem(count,2,item3)
            count += 1
            
        self.ui.profilePageStoreClerk1.setText(clerk)
        self.ui.profilePageDeliveryCompany1.setText(delivery)
        
    
    #will select a row on the conversations list to view all messages
    def set_selectedOrder(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
            column = 0
      
        self.selectedOrder= self.ui.ordersTableWidget.item(row,column).text()
                        
        self.orderPath = self.folderPath + str(self.userID) +"Order"+ str(self.selectedOrder) + ".txt"
        self.readOrderInfo(self.orderPath)
        

    def show_cart_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage)
    
    def show_OS1_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.shoppage)

    def show_OS2_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.windowspage)
   
    def show_OS3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chromepage)
        
    def show_item_page(self, product):
        self.generateItem(product)
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
    
    
    
  #  _________________________cart funtions_______________________________
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
 
    #for OS page "add to cart" buttons
    def searchItem(self, name, price):
        itemsArray = self.readInventoryTextFile()

        index = 0
        for item in itemsArray: #breaks the list down to seperate product objects
            if (item.getName() == name and item.getPrice() == price): #checks if the product object in the inventory list
                ID = item.getID()
                break
        
        return item
    
    #for item page
    def searchItem2(self, name, price, description):
        itemsArray = self.readInventoryTextFile()

        index = 0
        for item in itemsArray: #breaks the list down to seperate product objects
            if (item.getName() == name and item.getPrice() == price and item.getDescription() == description): #checks if the product object in the inventory list
                ID = item.getID()
                break
        return item

    #will add the item to the cart
    def add_to_cart(self, product):
        file = self.writeToCartTextfile(product) #cart file will be created and also updated
        self.showCartTable(file) #cart file will be created
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage) # The cart is shown once it is updated
#        comboBox1 = self.ui.cartItem1comboBox # will look at combobox 1
#        comboBox2 = self.ui.cartItem2comboBox # will look at combobox 2
#        self.ui.cartMakeChangesButton.clicked.connect(lambda x: self.readComboBox(comboBox1))

    #will read and write to the cart textfile
    def writeToCartTextfile(self, product):
    
        file = self.cartTextfile + "cart" + str(self.userID) + ".txt"
        f = open(file, "w")
        f.close()
        itemsArray = self.readInventoryTextFile()
 
        #opens the cart file to read
        myfile = open(file, "r+")
        lines = myfile.readlines()
        i = 0
        count = 0
        index = -1
        for singleLine in lines:
            newline = singleLine.strip()
            userList = newline.split(", ")
 
            ID = userList[1]
            quantity = userList[2]

            #checks if the item is already in the file
            if ID == product.getID():
                count += 1
                index = i
            i += 1
        myfile.close()
  
        #opens the cart file to write attributes seperated by a comma
        myfile = open(file, "a+")
        myfile.write(product.getName())
        myfile.write(", ")
        myfile.write(product.getID())
        myfile.write(", ")
        myfile.write(str(1)) #quantity will equal 1
        myfile.write(", ")
        num = int(product.getPrice().replace("$", ""))
        total = num * (1) #stores the total
        myfile.write(str(total))
        myfile.write("\n")

        myfile.close()
        return file
        
         # will check if cart is empty or not, if so will get error else order will be placed
    def checkCart(self, file):
        with open(file, "r") as f:
            length = len(f.readlines())
        if length == 0: #checks if there are no items in the cart
            self.showPopUpMessage("No items in cart", "Your cart is emtpy can not make a purchase")
        else: # if there are items in the cart and therefore the order than the order can be finalized
            self.file = file
            self.showPopUpMessage("Finalize Order", "Please finalize your order")
            self.ui.stackedWidget.setCurrentWidget(self.ui.finalizeOrderpage)
            
    #will read the cart and also write the new order on the order table
    def clearCart(self, file):
        with open(file ,'r') as cartfile, open(self.orderPath ,'a') as orderfile:
            # read content from first file
            for line in cartfile:
                orderfile.write(line)
                
        self.ui.cartTableWidget.setRowCount(0)
        self.ui.cartTotalCostAmount.setText("$0")
        
        file = open(file,"r+")
        file.truncate(0)
        file.close()
        
    
    def show_finalize_order_page(self, file):
        self.checkCart(file)
    
    #___________________end of cart functions __________________
    def showPopUpMessage(self, title, message):
        output = QMessageBox()
        output.setWindowTitle(title)
        output.setText(message)
        x = output.exec_()
    
    def buy_item(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.cartpage)

    def show_profile_orders_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.orderspage)
    
    def show_profile_payment_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.paymentpage)
    
    def show_profile_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.complaintspage)
    
    def show_profile_warnings_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.warningspage)




#________________complaints functions _____________
    def make_complaints_page(self):
        #reads the user type and
        self.ui.stackedWidget2.setCurrentWidget(self.ui.makeComplaintpage)
        self.ui.complainAbourUserSubmitButton.clicked.connect(self.checkComplaint)
        
                
    def checkComplaint(self):
        userType = self.readComboBox(self.ui.complainAbourUserTypeComboBox)
        message = self.ui.complainAbourUserIDDescriptiontextEdit.toPlainText()
        complaintAboutUserID =  self.ui.userIDTextEdit.toPlainText()
        orderID = self.ui.orderNumberTextEdit.toPlainText()
        
        if userType.lower() == "store clerk":
            letter = 'S'
        elif userType.lower() == "delivery company":
            letter = 'D'
        elif userType.lower() == "registered customer":
            letter = 'R'
        else:
            letter = 'O'
        
        if userType.lower() == "order":
        #write to orders txt file
        
            storeClerk = "N/A"
            path = "../Resources/Data/OrdersComplaints/ordersComplaints.txt"
            file = open(path, "a")  # append
            file.write("OC" + str(self.complaintNumber)  + ", OR" + str(orderID) + ", C" + str(complaintAboutUserID) + ", S" + storeClerk + "\n")
            file.close()
            
            path = "../Resources/Data/OrdersComplaints/ordersComplaintsDescriptions.txt"
            file = open(path, "a")  # append
            file.write("OC" + str(self.complaintNumber)  + ", " + message + "\n")
            file.close()
            
            path = "../Resources/Data/OrdersComplaints/ordersComplaintsResponse.txt"
            file = open(path, "a")  # append
            file.write("OC" + str(self.complaintNumber)  + ", "+ "N/A" + "\n")
            file.close()
            
            
        #else the complaint is about another user
        else:
        #write to user txtfile
            path = "../Resources/Data/UsersComplaints/usersComplaints.txt"
            file = open(path, "a")  # append
            file.write("CT" + str(self.complaintNumber)  + ", C" + str(self.userID) +  ", " + letter + str(userType)+ ", " + "N/A"+ "\n")
            file.close()
            
            path = "../Resources/Data/UsersComplaints/usersComplaintsDescriptions.txt"
            file = open(path, "a")  # append
            file.write("CT" + str(self.complaintNumber)  + ", C" + str(self.userID) + ", " + message + "\n")
            file.close()

            managerMessage = "N/A"
            path = "../Resources/Data/UsersComplaints/usersComplaintsJustifications.txt"
            file = open(path, "a")  # append
            file.write("CT" + str(self.complaintNumber) + ", " + "N/A" + "\n")
            file.close()

            #will write into the warnings text
            otherUserResponse = "N/A"
            path = "../Resources/Data/UsersComplaints/usersComplaintsMessages.txt"
            file = open(path, "a")  # append
            file.write("CT" + str(self.complaintNumber) + ", "+ otherUserResponse + "\n")
            file.close()
            
            
            #will write into the warnings text
            path = "../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt"
            file = open(path, "a")  # append
            file.write("CT" + str(self.complaintNumber ) + ", "  + str(self.userWarnings) + "\n")
            file.close()

        self.complaintNumber += 1 #increment the complaint count
        
        self.showPopUpMessage("Complaint Sent", "Your complaint has been sent")
        self.readComplaintsIHaveMade()
        self.readComplaintsAboutMe()
        self.ui.stackedWidget.setCurrentWidget(self.ui.profilepage)


    def readComplaintsIHaveMade(self):
        allComplaints = []
        
        #will start with the order complaints
        with open("../Resources/Data/OrdersComplaints/ordersComplaints.txt", "r") as file:
            lines = file.readlines()
            
        with open("../Resources/Data/OrdersComplaints/ordersComplaintsDescriptions.txt", "r") as file:
            lines2 = file.readlines()
        
        with open("../Resources/Data/OrdersComplaints/ordersComplaintsResponse.txt", "r") as file:
            lines3 = file.readlines()
       
        allLines = []
        storeLine = []
        for singleLine in lines:
            newline = singleLine.strip()
            line = newline.split(", ")
            
            
            if(str(line[2]) == "C" + str(self.userID)): # the customer has made the complaint
                storeLine = [line[0], line[1], line[2],line[3]] # stores complaint ID, ORder ID, customerID, and clerk ID
                #will look for the description from the second file
                for singleLine in lines2:
                    newline = singleLine.strip()
                    line2 = newline.split(", ")
                    if(str(line2[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line2[1]) #appends the description of the order
                        break
                        
                #will look for the response from the second file
                for singleLine in lines3:
                    newline = singleLine.strip()
                    line3 = newline.split(", ")
                    if (str(line3[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line3[1]) #appends the response to the order
                        break
            allLines.append(storeLine)
            
        #will continue with the users complaints
        with open("../Resources/Data/UsersComplaints/usersComplaints.txt", "r") as file:
            lines = file.readlines()
            
        with open("../Resources/Data/UsersComplaints/usersComplaintsDescriptions.txt", "r") as file:
            lines2 = file.readlines()
        
        with open("../Resources/Data/UsersComplaints/usersComplaintsJustifications.txt", "r") as file:
            lines3 = file.readlines()
            
        with open("../Resources/Data/UsersComplaints/usersComplaintsMessages.txt", "r") as file:
            lines4 = file.readlines()
        
        with open("../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt", "r") as file:
            lines5 = file.readlines()
            
        for singleLine in lines:
            newline = singleLine.strip()
            line = newline.split(", ")
            

            if(str(line[2]) == "C" + str(self.userID)): # the customer has made the complaint
     
                storeLine = [line[0], "N/A", line[1], line[2]]# stores complaint ID, customer userID, and otherUserID
                
                #will look for the description from the second file
                for singleLine in lines2:
                    newline = singleLine.strip()
                    line2 = newline.split(", ")
                    if(str(line[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line2[1]) #appends the description of the order
                        break
                    
                #will look for the justification from the third file
                for singleLine in lines3:
                    newline = singleLine.strip()
                    line3 = newline.split(", ")
                    if (str(line[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line3[1]) #appends the response to the order
                        break
                
                #will look for the Messages from the second file
                for singleLine in lines4:
                    newline = singleLine.strip()
                    line4 = newline.split(", ")
                    if(str(line4[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line4[1]) #appends the description of the order
                        break
                    
#                #will look for the warning from the third file
#                for singleLine in lines5:
#                    newline = singleLine.strip()
#                    line5 = newline.split(", ")
#                    if (str(line5[0]) == storeLine[0]): # find the complaint ID
#                        print("warning", line5[1])
#                        storeLine.append(line5[1]) #appends the response to the order
#                        break
            allLines.append(storeLine)
                
        self.writeComplaintsTable(allLines)
        
        
        
    def writeComplaintsTable(self, lines):
        count = 0
        for i in range(len(lines)):
            rowNum = self.ui.userComplaintsTableWidget.rowCount()
            self.ui.userComplaintsTableWidget.insertRow(rowNum)
            #complaint ID, order num, user ID, clerk ID, message, response
            item1 = QtWidgets.QTableWidgetItem(str(lines[rowNum][0])) #complaint number
            self.ui.userComplaintsTableWidget.setItem(rowNum,0,item1)
            
            item2 = QtWidgets.QTableWidgetItem(str(lines[rowNum][1])) #order number
            self.ui.userComplaintsTableWidget.setItem(rowNum,1,item2)
            
            item3 = QtWidgets.QTableWidgetItem(str(lines[rowNum][3])) #clerk responding
            self.ui.userComplaintsTableWidget.setItem(rowNum,2,item3)
            
            item4 = QtWidgets.QTableWidgetItem(str(lines[rowNum][2])) #userID
            self.ui.userComplaintsTableWidget.setItem(rowNum,3,item4)
            
            item5 = QtWidgets.QTableWidgetItem(str(lines[rowNum][4])) # description
            self.ui.userComplaintsTableWidget.setItem(rowNum,4,item5)
            
            item6 = QtWidgets.QTableWidgetItem(str(lines[rowNum][5])) #response
            self.ui.userComplaintsTableWidget.setItem(rowNum,5,item6)
            
            item7 = QtWidgets.QTableWidgetItem(str(lines[rowNum][5])) #resolution
            self.ui.userComplaintsTableWidget.setItem(rowNum,6,item7)
            
            count += 1
            
            
            
    def readComplaintsAboutMe(self):
        allLines = []
            
        #will continue with the users complaints
        with open("../Resources/Data/UsersComplaints/usersComplaints.txt", "r") as file:
            lines = file.readlines()
            
        with open("../Resources/Data/UsersComplaints/usersComplaintsDescriptions.txt", "r") as file:
            lines2 = file.readlines()
        
        with open("../Resources/Data/UsersComplaints/usersComplaintsJustifications.txt", "r") as file:
            lines3 = file.readlines()
            
        with open("../Resources/Data/UsersComplaints/usersComplaintsMessages.txt", "r") as file:
            lines4 = file.readlines()
        
        with open("../Resources/Data/UsersComplaints/usersComplaintsWarnings.txt", "r") as file:
            lines5 = file.readlines()
            
        for singleLine in lines:
            newline = singleLine.strip()
            line = newline.split(", ")
            

            if(str(line[1]) == "C" + str(self.userID)): # the customer has made the complaint
                storeLine = [line[0], line[1], line[2]]# stores complaint ID, customer userID, and otherUserID
                #will look for the description from the second file
                for singleLine in lines2:
                    newline = singleLine.strip()
                    line2 = newline.split(", ")
                    if(str(line[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line2[1]) #appends the description of the order
                        break
                    
                #will look for the justification from the third file
                for singleLine in lines3:
                    newline = singleLine.strip()
                    line3 = newline.split(", ")
                    if (str(line[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line3[1]) #appends the response to the order
                        break
                
                #will look for the Messages from the second file
                for singleLine in lines4:
                    newline = singleLine.strip()
                    line4 = newline.split(", ")
                    if(str(line4[0]) == storeLine[0]): # find the complaint ID
                        storeLine.append(line4[1]) #appends the description of the order
                        break
          
            allLines.append(storeLine)
                            
        self.writeComplaintsAboutMeTable(allLines)
        
    #will write to the complaints about me table
    def writeComplaintsAboutMeTable(self, lines):
        count = 0
        for i in range(len(lines)):
            rowNum = self.ui.ComplaintsAboutUserTableWidget.rowCount()
            self.ui.ComplaintsAboutUserTableWidget.insertRow(rowNum)
            #complaint ID, order num, user ID, clerk ID, message, response
            item1 = QtWidgets.QTableWidgetItem(str(lines[count][0])) #complaint number
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,0,item1)
            
            item3 = QtWidgets.QTableWidgetItem(str(lines[count][2])) #clerk responding
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,1,item3)
            
            item4 = QtWidgets.QTableWidgetItem(str(lines[count][1])) #userID
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,2,item4)
            
            item5 = QtWidgets.QTableWidgetItem(str(lines[count][3])) # description
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,3,item5)
            
            item6 = QtWidgets.QTableWidgetItem(str(lines[count][4])) #response
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,4,item6)
            
            item7 = QtWidgets.QTableWidgetItem(str(lines[count][5])) #resolution
            self.ui.ComplaintsAboutUserTableWidget.setItem(count,5,item7)
            
            count += 1
    
    def respondToComplaints(self):
        complaintID = self.ui.respondToComplaintlineEdit.text()
        response = self.ui.respondToComplaintDescriptionTextEdit.text()
    
    def respond_to_complaints_page(self):
        #reads the user type and
        self.ui.stackedWidget2.setCurrentWidget(self.ui.makeComplaintpage)
        self.ui.respondToComplaintSubmitButton(self.respondToComplaints())
        self.ui.complainAbourUserSubmitButton.clicked.connect(self.checkComplaint)



    def checkResponse(self):
        complaintID = self.ui.respondToComplaintlineEdit.text()
        message = self.ui.respondToComplaintDescriptionTextEdit.toPlainText()
  
        
        self.showPopUpMessage("Complaint Response Sent", "Your complaint response has been sent")
        self.ui.stackedWidget.setCurrentWidget(self.ui.profilepage)



    def respond_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.respondToComplaintpage)
        self.ui.respondToComplaintSubmitButton.clicked.connect(self.checkResponse)
        

    def show_myAccount_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.myAccountPage)
    
    def show_complaints_page(self):
        self.ui.stackedWidget2.setCurrentWidget(self.ui.complaintspage)

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

        #if any of the add to cart buttons on OS page are pressed then the item is displayed is then added to the cart
        self.ui.OS1cartbutton1.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name1, self.ui.OS1price1))
        self.ui.OS1cartbutton2.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name2, self.ui.OS1price2))
        self.ui.OS1cartbutton3.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name3, self.ui.OS1price3))
        self.ui.OS1cartbutton4.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name4, self.ui.OS1price4))
        self.ui.OS1cartbutton5.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name5, self.ui.OS1price5))
        self.ui.OS1cartbutton6.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS1name6, self.ui.OS1price6))
        
        #will match the OS items images to their information
        self.matchOS( self.ui.OS1name1, self.ui.OS1price1, self.ui.OS1Image1, matchedItems[0], matchedPosition[0], self.ui.OS1cartbutton1)
        self.matchOS(self.ui.OS1name2, self.ui.OS1price2, self.ui.OS1Image2, matchedItems[1], matchedPosition[1], self.ui.OS1cartbutton2)
        self.matchOS(self.ui.OS1name3, self.ui.OS1price3, self.ui.OS1Image3, matchedItems[2], matchedPosition[2], self.ui.OS1cartbutton3)
        self.matchOS(self.ui.OS1name4, self.ui.OS1price4, self.ui.OS1Image4, matchedItems[3], matchedPosition[3], self.ui.OS1cartbutton4)
        self.matchOS(self.ui.OS1name5, self.ui.OS1price5, self.ui.OS1Image5, matchedItems[4], matchedPosition[4], self.ui.OS1cartbutton5)
        self.matchOS(self.ui.OS1name6, self.ui.OS1price6, self.ui.OS1Image6, matchedItems[5], matchedPosition[5], self.ui.OS1cartbutton6)
        
        
    
    #generates top OS 2 page
    def generateTopOS2Page(self, matchedItems, matchedPosition):
        
        #top OS page ui components
        os2PageImageButton = [self.ui.OS2Image1, self.ui.OS2Image2, self.ui.OS2Image3, self.ui.OS2Image4, self.ui.OS2Image5, self.ui.OS2Image6]  #ui objects for top OS products images
        os2ItemNames = [self.ui.OS2name1, self.ui.OS2name2, self.ui.OS2name3, self.ui.OS2name4, self.ui.OS2name5, self.ui.OS2name6] #ui objects for top OS products names
        os2ItemPrice = [self.ui.OS2price1, self.ui.OS2price2, self.ui.OS2price3, self.ui.OS2price4, self.ui.OS2price5, self.ui.OS2price6] #ui objects for top OS products prices
        addCartButtons = [self.ui.OS2cartbutton1, self.ui.OS2cartbutton2, self.ui.OS2cartbutton3, self.ui.OS2cartbutton4, self.ui.OS2cartbutton5, self.ui.OS2cartbutton6]
    
        #if any of the add to cart buttons on OS page are pressed then the item is displayed is then added to the cart
        self.ui.OS2cartbutton1.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name1, self.ui.OS2price1))
        self.ui.OS2cartbutton2.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name2, self.ui.OS2price2))
        self.ui.OS2cartbutton3.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name3, self.ui.OS2price3))
        self.ui.OS2cartbutton4.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name4, self.ui.OS2price4))
        self.ui.OS2cartbutton5.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name5, self.ui.OS2price5))
        self.ui.OS2cartbutton6.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS2name6, self.ui.OS2price6))
        
        
        #will match the OS items images to their information
        self.matchOS( self.ui.OS2name1, self.ui.OS2price1, self.ui.OS2Image1, matchedItems[0], matchedPosition[0], self.ui.OS2cartbutton1)
        self.matchOS(self.ui.OS2name2, self.ui.OS2price2, self.ui.OS2Image2, matchedItems[1], matchedPosition[1], self.ui.OS2cartbutton2)
        self.matchOS(self.ui.OS2name3, self.ui.OS2price3, self.ui.OS2Image3, matchedItems[2], matchedPosition[2], self.ui.OS2cartbutton3)
        self.matchOS(self.ui.OS2name4, self.ui.OS2price4, self.ui.OS2Image4, matchedItems[3], matchedPosition[3], self.ui.OS2cartbutton4)
        self.matchOS(self.ui.OS2name5, self.ui.OS2price5, self.ui.OS2Image5, matchedItems[4], matchedPosition[4], self.ui.OS2cartbutton5)
        self.matchOS(self.ui.OS2name6, self.ui.OS2price6, self.ui.OS2Image6, matchedItems[5], matchedPosition[5], self.ui.OS2cartbutton6)
        
    #generates top OS 3 page
    def generateTopOS3Page(self, matchedItems, matchedPosition):
        #top OS page ui components
        os3PageImageButton = [self.ui.OS3Image1, self.ui.OS3Image2, self.ui.OS3Image3, self.ui.OS3Image4, self.ui.OS3Image5, self.ui.OS3Image6]  #ui objects for top OS products images
        os3ItemNames = [self.ui.OS3name1, self.ui.OS3name2, self.ui.OS3name3, self.ui.OS3name4, self.ui.OS3name5, self.ui.OS3name6]  #ui objects for top OS products names
        os3ItemPrice = [self.ui.OS3price1, self.ui.OS3price2, self.ui.OS3price3, self.ui.OS3price4, self.ui.OS3price5, self.ui.OS3price6]  #ui objects for top OS products prices
        addCartButtons = [self.ui.OS3cartbutton1, self.ui.OS3cartbutton2, self.ui.OS3cartbutton3, self.ui.OS3cartbutton4, self.ui.OS3cartbutton5, self.ui.OS3cartbutton6]
        
        #if any of the add to cart buttons on OS page are pressed then the item is displayed is then added to the cart
        self.ui.OS3cartbutton1.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name1, self.ui.OS3price1))
        self.ui.OS3cartbutton2.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name2, self.ui.OS3price2))
        self.ui.OS3cartbutton3.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name3, self.ui.OS3price3))
        self.ui.OS3cartbutton4.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name4, self.ui.OS3price4))
        self.ui.OS3cartbutton5.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name5, self.ui.OS3price5))
        self.ui.OS3cartbutton6.clicked.connect(lambda x: self.generateItemInfo4(self.ui.OS3name6, self.ui.OS3price6))

        #will match the OS items images to their information
        self.matchOS(self.ui.OS3name1, self.ui.OS3price1, self.ui.OS3Image1, matchedItems[0], matchedPosition[0], self.ui.OS3cartbutton1)
        self.matchOS(self.ui.OS3name2, self.ui.OS3price2, self.ui.OS3Image2, matchedItems[1], matchedPosition[1], self.ui.OS3cartbutton2)
        self.matchOS(self.ui.OS3name3, self.ui.OS3price3, self.ui.OS3Image3, matchedItems[2], matchedPosition[2], self.ui.OS3cartbutton3)
        self.matchOS(self.ui.OS3name4, self.ui.OS3price4, self.ui.OS3Image4, matchedItems[3], matchedPosition[3], self.ui.OS3cartbutton4)
        self.matchOS(self.ui.OS3name5, self.ui.OS3price5, self.ui.OS3Image5, matchedItems[4], matchedPosition[4], self.ui.OS3cartbutton5)
        self.matchOS(self.ui.OS3name6, self.ui.OS3price6, self.ui.OS3Image6, matchedItems[5], matchedPosition[5], self.ui.OS3cartbutton6)
  
    def matchOS(self, uiName, uiPrice, uiImage, matchedItem, matchedPosition, addCartButton):
           
        itemsArray = self.readInventoryTextFile()
       
        index = matchedPosition
        itemObject = itemsArray[index]

        itemName = itemObject.getName() #refers to the name
        uiName.setText(itemName)
        uiName.setStyleSheet("font-size: 25pt;")

        itemPrice = itemObject.getPrice() #refers to the price
        uiPrice.setText(itemPrice) #refers to the price
        uiPrice.setStyleSheet("font-size: 25pt;")

        itemImage= itemObject.getImage() #refers to the image
        uiImage.setIcon(QtGui.QIcon(itemImage))
        uiImage.setIconSize(QtCore.QSize(300, 200))
        
        uiImage.clicked.connect(lambda x: self.show_item_page(itemObject))
        
        addCartButton.setText("ADD TO CART")
        addCartButton.setStyleSheet("font-size: 13pt;")

        
        addCartButton.setStyleSheet("QPushButton{\n"
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
        self.ui.topsellerbutton1.clicked.connect(lambda x: self.generateItemInfo1())
        self.ui.topsellerbutton1.setStyleSheet("QPushButton{\n"
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
                


    #will record the second top seller product information to write on the homepage
    def generateTopSeller2Page(self, item):
        self.matchTopSeller(item, self.ui.topsellername2, self.ui.topSellerPrice2, self.ui.topSellerImage2)
        ##-----homepage top seller button leads to cart page through the generateItemInfo2 function
        self.ui.topsellerbutton2.clicked.connect(lambda x: self.generateItemInfo2())
        self.ui.topsellerbutton2.setStyleSheet("QPushButton{\n"
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
                


    #will record the third top seller product information to write on the homepage
    def generateTopSeller3Page(self, item):
        self.matchTopSeller(item, self.ui.topsellername3, self.ui.topSellerPrice3, self.ui.topSellerImage3)
        ##-----homepage top seller button leads to cart page through the generateItemInfo3 function
        self.ui.topsellerbutton3.clicked.connect(lambda x: self.generateItemInfo3())
        self.ui.topsellerbutton3.setStyleSheet("QPushButton{\n"
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
        myfile = open(self.filepath + "/Products/products.txt", "r")
        next(myfile)
        lines = myfile.readlines()
        allProductsData = []

        for singleLine in lines:
            newline = singleLine.strip()
            product = newline.split(", ")
            allProductsData.append(product)
     
        myfile.close()

        # ID, images
        myfile = open(self.filepath + "/Products/products_images.txt", "r")
        next(myfile)
        lines = myfile.readlines()
        allProductsImages = []

        for singleLine in lines:
            newline = singleLine.strip()
            productImages = newline.split(", ")
#            del productImages[0]
            imageName = productImages[1]
            allProductsImages.append(imageName)

        myfile.close()
    
        # ID, description
        myfile = open(self.filepath+ "/Products/products_descriptions.txt", "r")
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

        path = self.filepath+ "/ProductsImages/"
        allProducts = []
        for pData in allProductsData:
            #ID, name, price, OS, quantity, sold, profit, boughtPrice, images, description
            allProducts.append(storeProduct(pData[0], pData[1], pData[2], pData[3], pData[4], pData[5], pData[6], pData[7],  pData[8], pData[9]))

        return allProducts




#will display the cart with the items that have been added to it
    def showCartTable(self, file):
        l=[] #to store the different items
        total = 0
        with open(file, "r") as myfile:
            lines = myfile.readlines()
            for singleLine in lines: #breaks the list down to lines
                newline = singleLine.strip() #strips the "\n" from the strings line
                item = newline.split(", ") #strips strings by the ", " delimiter
                total += int(item[3]) # will update the total cost of the items in a cart
                l.append(item)

        self.ui.cartTotalCostAmount.setText(str(total)) # will update the total on the ui object
        self.ui.cartTableWidget.setSortingEnabled(False)
        self.ui.cartTableWidget.setRowCount(len(l))
        self.ui.cartTableWidget.setColumnCount(len(l[0]))

        
        for i in range(len(l)):
            for j in range(len(l[0])):
                item = QtWidgets.QTableWidgetItem(l[i][j])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ui.cartTableWidget.setItem(i,j,item)
        self.ui.cartTableWidget.setSortingEnabled(0)
        
        #--users will have to finalize order when they press place order on their cart page or buy on an item page
        self.ui.placeorderbutton.clicked.connect(lambda x: self.show_finalize_order_page(file))
#

    #will read the user input for the number of items
    def readComboBox(self, comboBoxName):
        # finding the content of current item in combo box
        content = comboBoxName.currentText()
        return content
        
    
    def rateItem(self):
        name = self.ui.profilePageItem1.text()
        itemsArray = self.readInventoryTextFile()
        index = 0
        for item in itemsArray: #breaks the list down to seperate product objects
            if (item.getName() == name): #checks if the product object in the inventory list
                ID = item.getID()
                break
        
        rating = self.readComboBox(self.ui.profilePageItem1comboBox)
        
        sum = item.getTotalRatingSum() + rating
        newRate = item.setTotalRatingSum(sum)
        item.setRate(newRate)
        #next will write into inventory textfile
        return item
   


        
        
class storeProduct:
    def __init__(self, ID, name, price, OS, quantity, sold, profit, boughtPrice, image, description):
        self.name = name
        self.ID = ID
        self.price = price
        self.description = description
        self.image = image
        self.OS = OS
        self.sold = sold
        self.quantity = quantity
        self.rate = 0
        self.totalRatingSum = 0
        self.profit = profit

    
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
    def getProfit(self):
        return self.profit

        
        
        
        
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
    def setProfit(self, profit):
        self.profit = profit
      
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
    main_win = registered()
    main_win.show()

    sys.exit(app.exec_())
    


