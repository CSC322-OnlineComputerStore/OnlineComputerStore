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
        self.main_win = QMainWindow() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.bet_page)
        self.ui.header_label.setText("View Bets")

        self.ui.view_order_button.clicked.connect(self.show_order_page)
        self.ui.view_bets_button.clicked.connect(self.show_bet_page)
        self.ui.account_info_button.clicked.connect(self.show_account_info_page)
        self.ui.view_complaint_button.clicked.connect(self.show_complaint_page)
        self.ui.view_warning_button.clicked.connect(self.show_warning_page)
        self.ui.add_bet_button.clicked.connect(self.set)
        self.ui.order_bet_table.selectionModel().selectionChanged.connect(self.set_selectedorder_info)

    def set(self):
        self.set_bets(self.filepath+'all_orders'+'/all_bets/'+self.selectedOrderno)
        self.get_bets(self.filepath+'all_orders'+'/all_bets/'+self.selectedOrderno)

    def show(self):
        self.main_win.show()

    def show_order_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.order_page)
        self.ui.header_label.setText("View Order")


    def show_bet_page(self):
        self.get_order(self.filepath+'/all_orders/'+'order_count')
        self.ui.stackedWidget.setCurrentWidget(self.ui.bet_page)
        self.ui.header_label.setText("View Bets")

    def show_account_info_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.account_info_page)
        self.ui.header_label.setText("Account Info")

    def show_complaint_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.complaint_page)

    def show_warning_page(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.warning_page)

    def set_bets(self,filename):
        l=[]
        k=[]
        bet=self.ui.bet_enter.text()
        company="delivery"
        with open(filename, "r") as myfile:
            lines=myfile.readlines()
            l.append(lines)
        for i in range(len(l)):
            if (i==(len(l)-1)):
                l[i]+="\n"
            k+=l[i]
        if not("." in bet):
            bet=bet+".00"
        k.append(bet+" "+company)
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
        self.get_bets(self.filepath+'/all_orders/all_bets/'+self.selectedOrderno)
        self.set_customer_info(self.filepath+'/all_users/'+'/all_customers/'+self.selectedCustomerno+'/info')
        self.set_product_info(self.filepath+'/all_products/'+self.selectedProductno+'/info')
        self.set_order_info(self.filepath+'/all_orders/orders/'+self.selectedOrderno)
       


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
        l=[]
        k=[]
        with open(filename, "r") as myfile:
            lines=myfile.read().split()
            l.append(lines)
        for i in range(len(l)):
            k+=l[i]
        l=[k[i:i+2] for i in range (0, len(k),2)]
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
        with open(filename, "r") as myfile:
            lines=myfile.read().split(",")
            l.append(lines)
        for i in range(len(l)):
            k+=l[i]
        l=[k[i:i+5] for i in range (0, len(k),5)]
        for i in range(len(l)):
            if(l[i][len(l[i])-1]=="0"):
                for j in range(len(l[i])-1):
                    if (j==0):
                        l[i][j]=l[i][j].replace('\n','')
                    m.append(l[i][j])
        n=[m[i:i+4] for i in range (0, len(m),4)]
        self.ui.order_bet_table.setRowCount(len(n))
        for i in range(len(n)):
            for j in range(len(n[i])):
                item = QtWidgets.QTableWidgetItem(n[i][j])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.order_bet_table.setItem(i,j,item)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = test_main()
    main_win.show()
    sys.exit(app.exec_()) 