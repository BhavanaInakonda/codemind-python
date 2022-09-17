n=int(input())
k=n*n
r=0
while n>0:
    m=n%10
    r=r*10+m
    n=n//10
l=r*r
h=0
while l>0:
    g=l%10
    h=h*10+g
    l=l//10
if(k==h):
    print("True")
else:
    print("False")