p = input("Enter word:"  )
l1=[]
le=len(p)
for i in range(le):
    l1.append(p[i])
od=[ord(l1[i]) for i in range(le)]
print("ordinal value:",od)