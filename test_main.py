import sys
import os
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow


from test import Ui_MainWindow

class test_main:
    def __init__(self):
        self.filepath = os.getcwd()
        self.selectedOrderno, self.selectedCustomerno, self.selectedProductno = 0,0,0
        self.userid='00001'
        self.main_win = QMainWindow() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.bet_page)
        self.ui.header_label.setText("View Bets")

        self.ui.view_order_button.clicked.connect(self.show_order_page)
        self.ui.completed_order_table.selectionModel().selectionChanged.connect(self.set_selectedcompleteorder_info)

        
        self.ui.view_bets_button.clicked.connect(self.show_bet_page)
        self.ui.account_info_button.clicked.connect(self.show_account_info_page)
        self.ui.view_complaint_button.clicked.connect(self.show_complaint_page)
        self.ui.view_warning_button.clicked.connect(self.show_warning_page)
        self.ui.add_bet_button.clicked.connect(self.set)
        self.ui.order_bet_table.selectionModel().selectionChanged.connect(self.set_selectedorder_info)
        self.ui.complaints_table.selectionModel().selectionChanged.connect(self.set_selectedcomplaint_info)

    #view order panel
    def show_order_page(self):
        self.get_completed_order(self.filepath+"/all_users/all_deliverys/"+self.userid+"/orders/ordercount.txt")
        self.ui.stackedWidget.setCurrentWidget(self.ui.order_page)
        self.ui.header_label.setText("View Order")

    def get_completed_order(self,filename):
        l=[]
        k=[]
        m=[]
        n=[]
        lines = self.return_file_content(filename)
        lines = self.remove_n(lines)
        for i in range(len(lines)):
            l.append(self.return_file_content(self.filepath+"/all_users/all_deliverys/"+self.userid+"/orders/"+lines[i]+".txt"))

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
        
        orderinfolist = self.return_file_content(self.filepath+'/all_users/all_deliverys/'+self.userid+'/orders/'+orderno+'.txt')
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


    #complaint banner
    def set_selectedcomplaint_info(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
        complaintid = self.ui.complaints_table.item(row,1).text()
        customerid = self.ui.completed_order_table.item(row,0).text()
        
        complaintinfolist = self.return_file_content(self.filepath+'/all_users/all_deliverys/'+self.userid+'/complaints/'+complaintid+'.txt')
        complaintinfolist = self.remove_n(complaintinfolist)
    
        self.ui.complaintheader_label.setText(complaintinfolist[3])
        self.ui.complaintfrom_label.setText(complaintinfolist[2])
        self.ui.complaintdate_label.setText(complaintinfolist[1])
        complainttext = ''
        for i in range(4,len(complaintinfolist)):
            complainttext+=complaintinfolist[i]
            complainttext+="\n"
        self.ui.complainttext_label.setText(complainttext)       

    def get_complaints(self,filename):
        l=[]
        k=[]
        m=[]
        n=[]
        lines=self.return_file_content(filename)
        lines = self.remove_n(lines)
        for i in range(len(lines)):
            b=lines[i].split(" ")
            l.append(b)
        

        self.ui.complaints_table.setRowCount(0)
        self.ui.complaints_table.setRowCount(len(l))
        for i in range(len(l)):
            for j in range(len(l[i])):
                item = QtWidgets.QTableWidgetItem(l[i][j])
                self.ui.complaints_table.setItem(i,j,item)

    #view bets panner
    def set(self):
        self.set_bets(self.filepath+'/all_orders/orders/'+self.selectedOrderno+'/bet.txt')
        self.get_bets(self.filepath+'/all_orders/orders/'+self.selectedOrderno+'/bet.txt')

    def show(self):
        self.main_win.show()

    


    def show_bet_page(self):
        self.get_order(self.filepath+'/all_orders/'+'order_count.txt')
        self.ui.stackedWidget.setCurrentWidget(self.ui.bet_page)
        self.ui.header_label.setText("View Bets")

    def show_account_info_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.account_info_page)
        self.ui.header_label.setText("Account Info")

    def show_complaint_page(self):
        self.get_complaints(self.filepath+'/all_users/all_deliverys/'+self.userid+'/complaints/ordercount.txt')
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.complaint_page)

    def show_warning_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.warning_page)

    def set_bets(self,filename):
        l=[]
        k=[]
        bet=self.ui.bet_enter.text()
        company = self.return_file_content(self.filepath+'/all_users/all_deliverys/'+self.userid+'/info.txt')[1].replace("\n","")
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        for i in range(len(l)):
            if (i==(len(l)-1)):
                l[i]+="\n"
            k+=l[i]
        if not("." in bet):
            bet=bet+".00"
        k.append(bet+" "+company+" "+self.userid)
        with open(filename,"w") as file:
            file.writelines(k)
            file.close()
        self.ui.bet_enter.clear()

    def set_selectedorder_info(self,selected):
        row=0
        column=0
        for ix in selected.indexes():
            row = ix.row()
            column = 0
        self.selectedOrderno = self.ui.order_bet_table.item(row,column).text()
        self.selectedProductno= self.ui.order_bet_table.item(row,2).text()
        self.selectedCustomerno= self.ui.order_bet_table.item(row,1).text()
        self.get_bets(self.filepath+'/all_orders/orders/'+self.selectedOrderno+'/bet.txt')
        self.set_customer_info(self.filepath+'/all_users/'+'/all_customers/'+self.selectedCustomerno+'/info.txt')
        #self.set_product_info(self.filepath+'/all_products/'+self.selectedProductno+'/info')
        self.set_order_info(self.filepath+'/all_orders/orders/'+self.selectedOrderno+'/info.txt')
               


    def set_customer_info(self,filename):
        l=[]
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        self.ui.customername_label.setText(l[0][1].replace('\n',''))
        self.ui.addressline1_label.setText(l[0][6].replace('\n',''))
        self.ui.addressline2_label.setText(l[0][7].replace('\n',''))
        self.ui.addresscity_label.setText(l[0][8].replace('\n',''))
        self.ui.addressstate_label.setText(l[0][9].replace('\n',''))
        self.ui.addresszip_label.setText(l[0][10].replace('\n',''))

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
        l=[]
        k=[]
        with open(filename, "r") as myfile:
            lines=myfile.read().split()
            l.append(lines)
        for i in range(len(l)):
            k+=l[i]
        l=[k[i:i+3] for i in range (0, len(k),3)]
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
        lines=self.return_file_content(filename)
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = test_main()
    main_win.show()
    main_win.show_account_info_page()
    sys.exit(app.exec_()) 