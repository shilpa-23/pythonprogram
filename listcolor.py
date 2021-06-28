n=int(input("Enter the size of list"))
l1=[]
print("Enter Colours:")
for i in range(n):
    l1.append((input()))
print("List is:",l1)
n=int(input("Enter the size of list"))
l2=[]
print("Enter Colours:")
for i in range(n):
    l2.append((input()))
print("List is:",l2)
r=[]
for i in l1:
    if i not in l2:
        r.append(i)
print("List After :",r)
