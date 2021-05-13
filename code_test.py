import os
def return_file_content(filename):
    l=[]
    with open(filename, "r") as myfile:
        lines=myfile.readlines()
        l=lines
    return l

def remove_n(some_list):
    for i in range(len(some_list)):
        some_list[i]=some_list[i].replace('\n','')
    return some_list
filepath=os.getcwd()
row=0
column=0
orderinfolist = return_file_content(filepath+'/all_orders/orders/1122350/info.txt')
orderinfolist = remove_n(orderinfolist)
productidlist = []
for i in range(8,len(orderinfolist)):
    productidlist.append(orderinfolist[i].split(","))
packageweight,packageprice = 0,0
#productidlist = remove_n(productidlist)
#print(productidlist)
print(orderinfolist)
orderinfolist[3] = "processing\n"
print(orderinfolist)