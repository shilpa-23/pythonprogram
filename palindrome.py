n=int(input("enter a number:"))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("this is a palindrome number")
else:
    print("not pal indrome")