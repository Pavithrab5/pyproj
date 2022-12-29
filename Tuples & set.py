#print(set([1,2,3]))
#remove duplicates
list_input=list(map(int,input("").strip().split()))
print(list_input)
res=set(list_input)
print(list(res))
#to remove a list of numbers if present in the set
list_input1=list(map,int(input("").strip().split()))
print(list_input1)
for i in range(len(list_input1)):
    if str(list_input1[i].isdigit()):
        list_input1.remove(i)
print(list_input1)





           list_input1.remove(i)
print(list_input1)


list_a=['1','$','*','#']
for i in list_a:
    if i not in list_a:
        list_a.remove(i)
print(list)

set_input1=set(list(map(int,(input("").strip().split()))))
set_input2=set(list(map(int,(input("").strip().split()))))
res=set_input1.intersection(set_input2)
print(res)

#set_input1=set(list(map(int,(input("").strip().split()))))
#write a program to remove the elements other than numbers in the list.ex:1,2,3,#,5,2,@,5,7,#,^
list_input1=[1,#,$,2]
list_input2=list_input1.copy()
for i in list_input1:
     if str(list_input1[i]).isdigit:
         print(list_input1[i])

     else:
         list_input2.remove(list_input1)
print(list_input2)


#or
list_a=list(map(int,input("").strip().split()))
list_b=[]
for i in list_a:
    if i.isdigit()==True:
list_b.append(i)
print(list_b)















