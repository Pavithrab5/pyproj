#write a program to check superset,subset,disjoint set
set_a={1,2,3,4,5,6,7,8,9}
set_b={1,4,9,5}
set_c={10,11}
is_subset=set_b.issubset(set_a)
print(is_subset)
is_superset=set_a.issuperset(set_b)
print(is_superset)
is_disjoint=set_a.isdisjoint(set_c)
print(is_disjoint)

#write a program to print common elements in the 3 sets
set_a={1,2,3,4,5,6,7,8,9}
set_b={1,4,9,5}
set_c={1,4}
res=set_a & set_b & set_c
print(res)
#First line contains comma separated integers.the second line of inpur will contains an integer (K),
list_input=list(map(int,input("").strip().split()))
k=int(input())
#left shifting
list_a=list(map(int,input().split()))
n=int(input())
for i in range(n):
    t=list_a[0]
    list_a.remove(t)
    list_a.append(t)
    print(list_a)
#right shifting
list_a=list(map(int,input().split()))
n=int(input())
c=0
for i in range(n):
    t=list_a[-1]
    list_a.remove(t)
    list_a.insert(0,t)
    c=c+1
    print(c)
    print(list_a)
#read N lines from inputs and create a nested list




