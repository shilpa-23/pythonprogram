n=int(input("enter the no of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=' ')
    print("\r")
for i in range(n,1,-1):
    for j in range(1,i):
        print("*",end=' ')
    print("\r")