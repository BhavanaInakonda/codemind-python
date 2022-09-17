n=int(input())
t=n
k=0
while n>0:
    m=n%10
    s=1
    for i in range(1,m+1):
        s=s*i
    k=k+s
    n=n//10
if(k==t):
    print("The number",t,"is a strong number")
else:
     print("The number",t,"is not a strong number")
    