num = int(input("Enter The Number"))
if num > 1:
    for i in range(2,num):
        if (num % i == 0):
            print(num, "not  a Prime Number")
            break
    else:
            print(num,"is a Prime number")
else:
    print(num,"is not prime")
