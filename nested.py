x=int(input("Enter a number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if(x>y):
    if(x>z):
        print(x,"greatest ")
elif y>z:
        print(y,"greatest")
else:
        print(z,"is greatest")