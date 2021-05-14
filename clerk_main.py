import sys
import os
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


from clerk import Ui_MainWindow

class clerk_main:
    def __init__(self):
        self.filepath = os.getcwd()
        self.selectedOrderno, self.selectedCustomerno, self.selectedProductno = 0,0,0
        self.main_win = QMainWindow() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        #global variables
        self.selectedmessage = 0;self.userid='20001'

        #messages tab
        self.ui.message_button.clicked.connect(self.message_set)
        self.ui.pending_message_button.clicked.connect(self.show_pending_message_page)
        self.ui.conversation_button.clicked.connect(self.show_conversation_page)
        
        #orderstab
        self.ui.view_order_button.clicked.connect(self.show_order_page)
        self.ui.completed_order_table.selectionModel().selectionChanged.connect(self.set_selectedcompleteorder_info)

        #betstab
        self.ui.order_bet_table.selectionModel().selectionChanged.connect(self.set_selectedorder_info)
        self.ui.view_bets_button.clicked.connect(self.show_bet_page)
        self.ui.select_bet_button.clicked.connect(self.select_bet)

        #conversations
        self.ui.conversation_table.selectionModel().selectionChanged.connect(self.set_selected_message)

        #conversations dimension
        self.ui.conversation_table.setColumnWidth(0,179)
        self.ui.conversation_table.setColumnWidth(1,1)
        self.ui.conversation_table.horizontalHeader().setStretchLastSection(True)

        #message table dimensions
        self.ui.message_table.setColumnWidth(0, 50)
        self.ui.message_table.setColumnWidth(1, 336)
        self.ui.message_table.setColumnWidth(2, 100)
        self.ui.message_table.setColumnWidth(3, 336)
        self.ui.message_table.setColumnWidth(4, 50)

        self.ui.view_complaint_button.clicked.connect(self.show_complaint_page)
        self.ui.view_warning_button.clicked.connect(self.show_warning_page)
        self.ui.account_info_button.clicked.connect(self.show_account_info_page)
        self.show_account_info_page

        #send message
        self.ui.send_button.clicked.connect(self.newmessage_set)

    def show_account_info_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.account_info_page)
        self.ui.header_label.setText("Account Info")
    def show_complaint_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.complaint_page)

    def show_warning_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.warning_page)


    #ordertab code        
    def show_order_page(self):
        self.get_completed_order(self.filepath+"/all_users/all_clerks/"+self.userid+"/orders/ordercount.txt")
        self.ui.stackedWidget.setCurrentWidget(self.ui.order_page)
        self.ui.header_label.setText("View Order")

    #ordertab code
    def get_completed_order(self,filename):
        l=[]
        k=[]
        m=[]
        n=[]
        lines = self.return_file_content(filename)
        lines = self.remove_n(lines)
        for i in range(len(lines)):
            l.append(self.return_file_content(self.filepath+"/all_users/all_clerks/"+self.userid+"/orders/"+lines[i]+".txt"))
            
        for i in range(len(l)):
            k.append(l[i][0].replace("\n",""))
            k.append(l[i][2].replace("\n",""))
            k.append(l[i][1].replace("\n",""))
            k.append((l[i][7]).split(" ")[0])
            k.append(l[i][3].replace("\n",""))
            n.append(k)
            k=[]
        self.ui.completed_order_table.setRowCount(len(n))
        for i in range(len(n)):
            for j in range(len(n[i])):
                item = QtWidgets.QTableWidgetItem(n[i][j])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.completed_order_table.setItem(i,j,item)

    def set_selectedcompleteorder_info(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
        deliveryid = self.ui.completed_order_table.item(row,3).text().replace('\n','')
        customerid = self.ui.completed_order_table.item(row,2).text().replace('\n','')
        orderno = self.ui.completed_order_table.item(row,0).text().replace("\n","")
        
        orderinfolist = self.return_file_content(self.filepath+'/all_users/all_clerks/'+self.userid+'/orders/'+orderno+'.txt')
        orderinfolist = self.remove_n(orderinfolist)
        deliverycharge = (orderinfolist[7].split(" ")[1]).replace('\n','')
        productidlist = []
        for i in range(8,len(orderinfolist)):
            productidlist.append(orderinfolist[i].split(","))
        packageweight,packageprice = 0,0
        #productidlist = self.remove_n(productidlist)

        self.ui.ordernoc_label.setText(orderno)

            #packageweight += float((self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[2]).replace('\n',''))
            #packageprice += float((self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[3]).replace('\n',''))
        for i in range(len(productidlist)):
            packageprice_temp =self.return_file_content(self.filepath+'/all_products/'+productidlist[i][1].replace(" ","")+'/info.txt')[3].replace('\n','')
            packageprice = packageprice + float(packageprice_temp.replace('$','')) 
            #packageprice_temp =self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[3].replace('\n','')
            #packageprice = packageprice + float(packageprice_temp.replace('$','')) 
        #self.ui.packageweight_label.setText("Package Weight: "+ str (packageweight))
        self.ui.packagepricec_label.setText("Price: $"+ str (packageprice))
        self.ui.numberofproductsc_label.setText("Number of Products:"+str(len(productidlist)))

        self.ui.orderdate_label.setText("Date: "+orderinfolist[2].replace("\n",""))

        customerinfolist = self.return_file_content(self.filepath+'/all_users/'+'/all_customers/'+customerid+'/info.txt')
        customerinfolist = self.remove_n(customerinfolist)
        self.ui.customernamec_label.setText(customerinfolist[1])
        self.ui.addressline1c_label.setText(customerinfolist[6])
        self.ui.addressline2c_label.setText(customerinfolist[7])
        self.ui.cityc_label.setText(customerinfolist[8])
        self.ui.statec_label.setText(customerinfolist[9])
        self.ui.zipc_label.setText(customerinfolist[10])

        self.ui.deliverycompanyc_label.setText("Delivery Company:"+((self.return_file_content(self.filepath+"/all_users/all_deliverys/"+deliveryid+"/info.txt"))[1]).replace("\n",""))
        self.ui.deliverychargec_label.setText("Delivery Charge: $"+deliverycharge)
        self.ui.trackingidc_label.setText("Tracking ID: "+orderinfolist[4])
        self.ui.statusc_label.setText("Status: "+orderinfolist[3])
        self.ui.clerkc_label.setText("Clerk: "+((self.return_file_content(self.filepath+"/all_users/all_clerks/"+orderinfolist[6]+"/info.txt"))[1]).replace("\n",""))

    #betstab code
    def show_bet_page(self):
        self.get_order(self.filepath+'/all_orders/'+'order_count.txt')
        self.ui.stackedWidget.setCurrentWidget(self.ui.bet_page)
        self.ui.header_label.setText("View Bets")

    def select_bet(self):
        indexes = self.ui.all_bets_table.selectionModel().selectedRows()
        row=0
        row2=0
        for index in sorted(indexes):
            row=index.row()
        deliveryid = self.ui.all_bets_table.item(row,2).text()
        price = self.ui.all_bets_table.item(row,0).text()
        customerid = self.ui.customerid_label.text()
        selectedOrderno = self.ui.orderno_label.text()
        
        orderinfolist = self.return_file_content(self.filepath+'/all_orders/orders/'+selectedOrderno+'/info.txt')
        orderinfolist[1] = customerid+"\n"
        orderinfolist[3] = "Processing\n"
        orderinfolist[6] = self.userid+"\n"
        orderinfolist[7] = deliveryid+" "+price+"\n"

        ordercountdelivery = self.return_file_content(self.filepath+"/all_users/all_deliverys/"+deliveryid+"/orders/ordercount.txt")
        ordercountclerk = self.return_file_content(self.filepath+"/all_users/all_clerks/"+self.userid+"/orders/ordercount.txt")
        ordercountorder = self.return_file_content(self.filepath+"/all_orders/order_count.txt")
        
        ordercountdelivery.append(selectedOrderno+"\n");ordercountclerk.append(selectedOrderno+"\n") 

        temp=[]
        for i in range(len(ordercountorder)):
            a = ordercountorder[i].split(" ")
            temp.append(a)
        ordercountorder_temp = temp

        for i in range(len(ordercountorder_temp)):
            if(ordercountorder_temp[i][0]==selectedOrderno):
                ordercountorder[i]=ordercountorder_temp[i][0]+" "+ordercountorder_temp[i][1]+" "+ordercountorder_temp[i][2]+" "+"Processing\n"

        filename_delivery=self.filepath+"/all_users/all_deliverys/"+deliveryid+"/orders/"+selectedOrderno+".txt"
        filename_clerk=self.filepath+"/all_users/all_clerks/"+self.userid+"/orders/"+selectedOrderno+".txt"
        
        with open(filename_delivery,"w") as file:
            file.writelines(orderinfolist)
            file.close()
        with open(filename_clerk,"w") as file:
            file.writelines(orderinfolist)
            file.close()
        with open(self.filepath+"/all_users/all_deliverys/"+deliveryid+"/orders/ordercount.txt","w") as file:
            file.writelines(ordercountdelivery)
            file.close()
        with open(self.filepath+"/all_users/all_clerks/"+self.userid+"/orders/ordercount.txt","w") as file:
            file.writelines(ordercountclerk)
            file.close()
        with open(self.filepath+"/all_orders/order_count.txt","w") as file:
            file.writelines(ordercountorder)
            file.close()
        self.show_bet_page
        

    def set_selectedorder_info(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
        selectedOrderno = self.ui.order_bet_table.item(row,0).text()
        selectedCustomerno= self.ui.order_bet_table.item(row,1).text()
        orderinfolist = self.return_file_content(self.filepath+'/all_orders/orders/'+selectedOrderno+'/info.txt')
        orderinfolist = self.remove_n(orderinfolist)
        productidlist = []
        for i in range(8,len(orderinfolist)):
            productidlist.append(orderinfolist[i].split(","))
        packageweight,packageprice = 0,0
        #productidlist = self.remove_n(productidlist)

        self.ui.orderno_label.setText(selectedOrderno)

            #packageweight += float((self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[2]).replace('\n',''))
            #packageprice += float((self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[3]).replace('\n',''))
        for i in range(len(productidlist)):
            packageprice_temp =self.return_file_content(self.filepath+'/all_products/'+productidlist[i][1].replace(" ","")+'/info.txt')[3].replace('\n','')
            packageprice = packageprice + float(packageprice_temp.replace('$','')) 
            #packageprice_temp =self.return_file_content(self.filepath+'/all_products/'+productidlist[i]+'/info.txt')[3].replace('\n','')
            #packageprice = packageprice + float(packageprice_temp.replace('$','')) 
        #self.ui.packageweight_label.setText("Package Weight: "+ str (packageweight))
        self.ui.packageprice_label.setText("Price: $"+ str (packageprice))
        self.ui.numberofproducts_label.setText("Number of Products:"+str(len(productidlist)))

        self.ui.orderdate_label.setText("Date: "+orderinfolist[2].replace("\n",""))

        customerinfolist = self.return_file_content(self.filepath+'/all_users/'+'/all_customers/'+selectedCustomerno+'/info.txt')
        customerinfolist = self.remove_n(customerinfolist)
        self.ui.customername_label.setText(customerinfolist[1])
        self.ui.addressline1_label.setText(customerinfolist[6])
        self.ui.addressline2_label.setText(customerinfolist[7])
        self.ui.addresscity_label.setText(customerinfolist[8])
        self.ui.addressstate_label.setText(customerinfolist[9])
        self.ui.addresszip_label.setText(customerinfolist[10])
        self.ui.customerid_label.setText(selectedCustomerno)


        self.get_bets(self.filepath+'/all_orders/orders/'+selectedOrderno+'/bet.txt')

    def set_customer_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        self.ui.customername_label.setText(l[0][1].replace('\n',''))
        self.ui.addressline1_label.setText(l[0][2].replace('\n',''))
        self.ui.addressline2_label.setText(l[0][3].replace('\n',''))
        self.ui.addresscity_label.setText(l[0][4].replace('\n',''))
        self.ui.addressstate_label.setText(l[0][5].replace('\n',''))
        self.ui.addresszip_label.setText(l[0][6].replace('\n',''))

    def set_product_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        self.ui.productid_label.setText(l[0][0].replace('\n',''))
        self.ui.productname_label.setText(l[0][1].replace('\n',''))
        self.ui.productweight_label.setText(l[0][2].replace('\n',''))
        self.ui.productprice_label.setText(l[0][3].replace('\n',''))


    def set_order_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        self.ui.orderno_label.setText(l[0][0].replace('\n',''))
        self.ui.orderdate_label.setText(l[0][1].replace('\n',''))
        self.ui.orderstatus_label.setText(l[0][2].replace('\n',''))

    def get_bets(self,filename):
        a= self.return_file_content(filename)
        k=[]
        l=[]
        for i in range(len(a)):
            b = a[i].split(' ')
            b = self.remove_n(b)
            l.append(b)
            k=[]
        self.ui.all_bets_table.setSortingEnabled(False)
        self.ui.all_bets_table.setRowCount(len(l))
        self.ui.all_bets_table.setColumnCount(len(l[0]))
        for i in range(len(l)):
            for j in range(len(l[i])):
                item = QtWidgets.QTableWidgetItem(l[i][j])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.all_bets_table.setItem(i,j,item)
        self.ui.all_bets_table.setSortingEnabled(True)
        self.ui.all_bets_table.sortItems(0,QtCore.Qt.AscendingOrder)

    def get_order(self,filename):
        l=[]
        k=[]
        m=[]
        n=[]
        lines = self.return_file_content(filename)
        for i in range(len(lines)):
            b=lines[i].split(" ")
            b=self.remove_n(b)
            l.append(b)
        for i in range(len(l)):
            if(l[i][len(l[i])-1]=="pending"):
                for j in range(len(l[i])-1):
                    l[i][j]=l[i][j].replace('\n','')
                    m.append(l[i][j])
        n=[m[i:i+3] for i in range (0, len(m),3)]
        self.ui.order_bet_table.setRowCount(0)
        self.ui.order_bet_table.setRowCount(len(n))
        for i in range(len(n)):
            for j in range(len(n[i])):
                item = QtWidgets.QTableWidgetItem(n[i][j])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.order_bet_table.setItem(i,j,item)

    def return_order_count(self,filename):
        l=[]
        k=[]
        m=[]
        n=[]
        with open(filename, "r") as myfile:
            lines=myfile.read().split(",")
            l.append(lines)
        for i in range(len(l)):
            k+=l[i]
        l=[k[i:i+4] for i in range (0, len(k),4)]
        return l            

    
    #messagetab code
    def message_set(self):
        #self.get_messages(self.filepath+'/all_users/all_clerks/messages/to00001')
        self.set_messagelist(self.filepath+'/all_users/all_clerks/'+self.userid+'/messages/messagecount.txt')
        self.ui.stackedWidget.setCurrentWidget(self.ui.message_page)
        self.ui.header_label.setText("Messages")

    def show_pending_message_page(self):
        self.ui.message_type_page.setCurrentWidget(self.ui.pending_message_page)

    def show_conversation_page(self):
        self.ui.message_type_page.setCurrentWidget(self.ui.conversation_page)

    def newmessage_set(self):
        self.set_message(self.filepath+'/all_users/all_clerks/'+self.userid+'/messages/to'+self.selectedmessage+'.txt')

    def get_messages(self,filename):
        l=[]
        k=[]
        self.ui.message_table.setRowCount(0)
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
        l=lines
        for i in range(len(l)):
            l[i]=l[i].replace('\n','')
        self.ui.message_table.setRowCount(len(l)/2)
        self.ui.message_table.setColumnCount(5)
        tablerow = 0
        for i in range(len(l)-1):
            if (l[i]=='customer'):
                messageline=''    
                item1 = QtWidgets.QTableWidgetItem('C')
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                for j in range(i+1,len(l)):
                    if ((l[j]=='customer') or (l[j]=='clerk')):
                        break;
                    messageline+=l[j]+" "
                item2 = QtWidgets.QTableWidgetItem(messageline)
                item2.setTextAlignment(QtCore.Qt.AlignLeft)
                item2.setTextAlignment(QtCore.Qt.AlignVCenter)
                self.ui.message_table.setItem(tablerow,0,item1)
                self.ui.message_table.item(tablerow, 0).setForeground(QtGui.QColor(177,177,177))
                self.ui.message_table.setItem(tablerow,1,item2)
                self.ui.message_table.resizeRowsToContents()
                self.ui.message_table.item(tablerow, 1).setBackground(QtGui.QColor(233,211,202))
                self.ui.message_table.item(tablerow, 1).setForeground(QtGui.QColor(177,177,177))
                tablerow = tablerow+1

            elif (l[i]=='clerk'):
                messageline =''    
                item1 = QtWidgets.QTableWidgetItem('M')
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                for j in range(i+1,len(l)):
                    if ((l[j]=='customer') or (l[j]=='clerk')):
                        break;
                    messageline+=l[j]+" "
                item2 = QtWidgets.QTableWidgetItem(messageline)
                item2.setTextAlignment(QtCore.Qt.AlignVCenter|QtCore.Qt.AlignRight)
                self.ui.message_table.setItem(tablerow,3,item2)
                self.ui.message_table.resizeRowsToContents()
                self.ui.message_table.item(tablerow, 3).setBackground(QtGui.QColor(255,255,255))
                self.ui.message_table.item(tablerow, 3).setForeground(QtGui.QColor(177,177,177))
                self.ui.message_table.setItem(tablerow,4,item1)
                self.ui.message_table.item(tablerow, 4).setForeground(QtGui.QColor(177,177,177))
                tablerow = tablerow+1

    def set_message(self,filename):
        l=[]
        k=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        message = self.ui.message_enter.toPlainText()
        for i in range(len(l)):
            if (i==(len(l)-1)):
                l[i]+='\n'
        l.append('clerk\n')
        l.append(message)
        with open(filename,"w") as file:
            file.writelines(l)
            file.close()
        self.ui.message_enter.clear()
        self.get_messages(filename)

    def set_selected_message(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
            column = 1
        self.selectedmessage = self.ui.conversation_table.item(row,column).text()
        self.get_messages(self.filepath+'/all_users/all_clerks/'+self.userid+'/messages/to'+self.selectedmessage+'.txt')

    def set_messagelist(self,filename):
        l=[]
        k=[]
        customerinfolist=[]
        with open(filename,"r") as myfile:
            lines=myfile.read().split()
            l.append(lines)
        for i in range(len(l)):
            k+=l[i]
        l=[k[i:i+2] for i in range (0, len(k),2)]
        self.ui.conversation_table.setRowCount(len(l))
        for i in range(len(l)):
            customerinfolist=self.return_customer_info(self.filepath+"/all_users/all_customers/"+l[i][0]+"/info.txt")
            customername = QtWidgets.QTableWidgetItem(customerinfolist[1])
            customerid = QtWidgets.QTableWidgetItem(l[i][0])
            date = QtWidgets.QTableWidgetItem(l[i][1])
            self.ui.conversation_table.setItem(i,0,customername)
            self.ui.conversation_table.setItem(i,1,customerid)
            self.ui.conversation_table.setItem(i,2,date)

    def return_customer_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        return l

    def return_file_content(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l=lines
        return l

    def remove_n(self,some_list):
        for i in range(len(some_list)):
            some_list[i]=some_list[i].replace('\n','')
        return some_list


    def show(self):
        self.main_win.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = clerk_main()
    main_win.show()
    
    sys.exit(app.exec_()) 