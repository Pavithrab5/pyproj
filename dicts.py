dict_a={"name":"Teja","age":"15"}
print(dict_a)
print(dict_a['name'])
print(dict_a.get('name'))
#updating
dict_a['age']=24
print(dict_a)

#mxn

m,n=map(int,input().split())
x=[[int(input())for j in range(n)]for i in range(m)]
print(x)


n=input()
lis=list(n)
print(lis)
for i in range(lis):
    s=s+i
print(s)
l=len(lis)
avg=s/l
print(avg)

