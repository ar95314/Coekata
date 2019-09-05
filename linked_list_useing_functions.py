def delbeg(ll,data):
    ll.pop(0)
def delend(ll,data):
    ll.pop(-1)
def delany(ll,data,position):
    ll.pop(position-1,data)
def insbeg(data):
    ll.insert(0,data)
def insend(data):
    ll.append(data)
def insany(data,pos):
    ll.insert(pos-1,data)
ll=[]
menu={1:("insert",{1:("ins beg",insbeg),2:("ins end",insend),3:("ins any pos",insany)}),2:("delete",{1:("del beg",delbeg),2:("del end",delend),3:("del any pos",delany)})}
for key,value in menu.items():
    print(key,"->",value[0])
choice1=int(input("Enter choice"))
for key,value in menu[choice1][1].items():
    print(key,"->",value[0])
choice2=int(input("Enter choice"))
data=input("Enter data to insert")
if(choice2!=3):
    menu[choice1][1][choice2][1](data)
else:
    pos=int(input("Enter position"))
    menu[choice1][1][choice2][1](data,pos)
print(ll)
