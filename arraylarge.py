n=int(input("enter the size of array:"))
a=[]
flag=0
for i in range(0,n):
    a.append(int(input("enter elements")))
print("array is:",a)
large=a[0]
for i in range(0,n):
    if(a[i]>large):
        large=a[i]
print("largest element is",large)