def binary(lst, size, key):
    start = 0
    end = size- 1
    while start <= end:
        mid = int((start + end) / 2)
        if key == lst[mid]:
            print("Element present at" , mid+1)
            return -1
        elif key < lst[mid]:
            end = mid - 1
        elif key > lst[mid]:
            start = mid + 1
    print("Element not found!")
    return -1


lst = []

size = int(input("Enter size of list: "))

for n in range(size):
    numbers = int(input("Enter any number: "))
    lst.append(numbers)

lst.sort()
print('The sorted list is:', lst)

key = int(input("Enter the number to search: "))

binary(lst, size, key)