l=[]
w=input("enter string:")
str=w.split()
for i in str:
    if i not in l:
        l.append(i)
for i in range(0,len(l)):
    print("word ",l[i],"occurs",str.count(l[i]),"time")