n=int(input())
k=n*n
a=len(str(n))
l=[]
c=0
for i in str(k):
    l.append(i)
for i in str(n):
    if i in l:
        c+=1

if(c==len(str(n))):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    