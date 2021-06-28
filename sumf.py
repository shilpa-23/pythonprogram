def sum(n):
    sum = 0
    for i in range(1, n + 1):
     sum = int(sum + i)
    return sum
n=int(input("enter limit:"))
print("sum is=",sum(n))