linkedlist=[]
def insert_at_beginning(linkedlist,data):
    linkedlist.insert(0,data)
def insert_at_end(linkedlist,data): 
    linkedlist.append(data)
def insert_at_position(linkedlist,data,position):
    linkedlist.insert(position-1,data)
def delete_at_beginning(linkedlist,data):
    linkedlist.pop(0)
def delete_at_End(linkedlist,data):
    linkedlist.pop(-1)
def delete_at_position(linkedlist,data,position):
    linkedlist.pop(position-1,data)
def search(linkedlist,data):
    if(data in linkedlist):
        print("the data is found")
    else:
        print("the data is not found")
def update(linkedlist,oldvalue):
    if(oldvalue in linkedlist):
        for i in range(0,len(linkedlist)):
            if(linkedlist[i]==oldvalue):
                print("enter the new value")
                newvalue=int(input())
                linkedlist[i]=newvalue
            else:
                print("not in list")
def display(linkedlist):
    for value in linkedlist:
        print(value,end="")
dict1={1:("insert",{1:("insert beginning",insert_at_beginning),2:("insert end",insert_at_end),3:("insert position",insert_at_position)}),
       2:("delete",{1:("delete beginning",delete_at_beginning),2:("delete end",delete_at_End),3:("delete position",delete_at_position)}),
       3:("search",search),
       4:("update",update)}
for key,value in dict1.items():
    print(key,"->",value[0])
choice1=int(input("Enter choice"))
for key,value in dict1[choice1][1].items():
    print(key,"->",value[0])
choice2=int(input("Enter choice"))
data=input("Enter data to insert")
if(choice2!=3):
 dict1[choice1][1][choice2][1](linkedlist,data)
else:
 pos=int(input("Enter position"))
 dict1[choice1][1][choice2][1](data,position)
print(linkedlist)
