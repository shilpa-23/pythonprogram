n=int(input("enter the size of Array:"))
a=[]
for i in range(0,n):
    a.append(int(input("enter elements:")))
print("Array is:",a)
for i in range(n-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j + 1] = temp
print(" Sorted array is:",a)

