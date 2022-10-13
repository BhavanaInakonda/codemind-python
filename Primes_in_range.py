from math import *
m=int(input())
n=int(input())
l=[0]*(n+1)
l[0],l[1]=1,1#print(l)
sq=int(sqrt(n))
for i in range(2,sq+1):
    for j in range(i*i,n+1,i):
        l[j]=1
c=0
for k in range(m,n+1):
    if l[k]==0:
        c+=1
print(c)
    