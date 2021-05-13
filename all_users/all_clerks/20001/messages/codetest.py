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
        for i in range(len(l)-1):
            if (l[i]=='customer'):
                messageline=''    
                item1 = QtWidgets.QTableWidgetItem('C')
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                for j in range(i+1,len(l)-1):
                    if ((l[j]=='customer') or (l[j]=='clerk')):
                        break;
                    messageline+=l[j]+" "
                item2 = QtWidgets.QTableWidgetItem(messageline)
                item2.setTextAlignment(QtCore.Qt.AlignLeft)
                item2.setTextAlignment(QtCore.Qt.AlignVCenter)
                self.ui.message_table.setItem(i/2,0,item1)
                self.ui.message_table.item(i/2, 0).setForeground(QtGui.QColor(177,177,177))
                self.ui.message_table.setItem(i/2,1,item2)
                self.ui.message_table.resizeRowsToContents()
                self.ui.message_table.item(i/2, 1).setBackground(QtGui.QColor(233,211,202))
                self.ui.message_table.item(i/2, 1).setForeground(QtGui.QColor(177,177,177))
get_messages('messagecount')

'''for i in range(len(l)):
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
'''