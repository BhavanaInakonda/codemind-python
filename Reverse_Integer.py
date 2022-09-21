n=int(input())
p=abs(n)
rev=0
while p>0:
    m=p%10
    rev=rev*10+m
    p=p//10
if(n<0):
    print(-rev)
else:
    print(rev)