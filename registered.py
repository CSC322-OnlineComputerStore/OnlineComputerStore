import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from customer import Ui_Homepage


class registered:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_Homepage()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)

#-----homepage navigation bar, home, profile, cart, help
        self.ui.homebutton.clicked.connect(self.show_home_page)
        self.ui.profilebutton.clicked.connect(self.show_profile_page)
        self.ui.helpButton.clicked.connect(self.show_help_page)
        self.ui.cartbutton.clicked.connect(self.show_cart_page)

#-----homepage OS systems browsing more items
        self.ui.seeProductsButton1.clicked.connect(self.show_OS1_page)
        self.ui.seeProductsButton2.clicked.connect(self.show_OS2_page)
        self.ui.seeProductsButton3.clicked.connect(self.show_OS3_page)

#-----homepage OS systems image button leads to item page
        self.ui.OSimagbutton1.clicked.connect(self.show_OS1_page)
        self.ui.OSimagbutton2.clicked.connect(self.show_OS2_page)
        self.ui.OSimagbutton3.clicked.connect(self.show_OS3_page)

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
   
    def show_topSeller_image1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
    def show_topSeller_image2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
    def show_topSeller_image3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.itempage)
        
       
    def show_OS3_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.chromepage)
    
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
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = registered()
    main_win.show()
    sys.exit(app.exec_())

