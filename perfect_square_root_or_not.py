n=int(input())
count=0
for i in range(n):
    if(i*i==n):
        count=1
if(count==1):
    print("True")
else:
    print("False")
        