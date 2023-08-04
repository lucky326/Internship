list1=[]
list2=[]
Dic={}
n=int(input("Enter the size of both lists"))
for i in range(0,n):
    element=input("Enter elemnts you want in list1")
    list1.append(element)
for i in range(0,n):
    element=input("Enter elements you want in list2")
    list2.append(element)

for x in list1:
    for y in list2:
        Dic[x]=y
        list2.remove(y)
        break

print(Dic)