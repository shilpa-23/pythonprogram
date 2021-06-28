n=int(input("enter the 1st limit:"))
e=int(input("enter the ending limit:"))
print("Result is:")
for i in range(n,e+1):
    for j in range(1,i):

        if i==j*j:
            st=str(i)
            if int(st[0])%2==0 and int(st[1])%2==0 and int(st[2])%2==0 and int(st[3])%2==0:
             print(i)