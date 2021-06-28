def pow(n,r):
    if r==1:
        return n
    else:
        return (n*pow(n,r-1))
n=int(input("enter the number:"))
r=int(input("enter the power:"))
print(n,"raise to ",r,"is=",pow(n,r))