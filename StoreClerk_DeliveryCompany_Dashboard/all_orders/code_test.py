import os
def return_file_content(filename):
    l=[]
    with open(filename, "r") as myfile:
        lines=myfile.readlines()
        l=lines
    return l
def get_order(filename):
    selectedOrderno = "1122350"
    ordercountorder = return_file_content("order_count.txt")
    print(ordercountorder)
    temp=[]
    for i in range(len(ordercountorder)):
        a = ordercountorder[i].split(" ")
        temp.append(a)
    ordercountorder_temp = temp

    for i in range(len(ordercountorder_temp)):
        if(ordercountorder_temp[i][0]==selectedOrderno):
            #ordercountorder[i]=ordercountorder_temp[i][0]+" "+ordercountorder_temp[i][1]+" "+ordercountorder_temp[i][2]+" "+"Processing\n"
            ordercountorder[i]=""

    with open("order_count.txt") as file:
            file.writelines(ordercountorder)
            file.close()
get_order("order_count.txt")
