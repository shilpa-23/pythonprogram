n=int(input("enter limit:"))
i=1
x=0
while True:
    c=0;
    for j in range(1,i+1,1):
        a=i%j
        if a==0:
            c=c+1
    if c==2:
        print(i)
        x=x+1
        if x>=n:
          break
    i=i+1
