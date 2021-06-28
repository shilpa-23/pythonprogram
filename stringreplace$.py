str=input("Enter string:")
s=str[0]
for i in range (len(str)):
    str=str.replace(s,'$')
    str1=s+str[1:]
print(str1)
 