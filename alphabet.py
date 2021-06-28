n=int(input("enter number of rows:"))
for i in range (65+n,65,-1):
    for j in range(65,i):
        print(chr(j),end=' ')
    print()