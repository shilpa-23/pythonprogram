x=int(input("enter number:"))
sum=0
for i in range (1,x):
    if(x%i==0):
        sum=sum+i
if(sum==x):
    print("perfect number")
else:
    print("not perfect")